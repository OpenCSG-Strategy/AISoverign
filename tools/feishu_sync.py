#!/usr/bin/env python3
"""Overwrite one Feishu doc with the assembled book, figures included.

Environment:
  FEISHU_APP_ID, FEISHU_APP_SECRET  self-built app credentials
  FEISHU_DOC                        the target doc's URL or token (docx/... or wiki/...)
  FEISHU_BASE                       optional, default https://open.feishu.cn (Lark: https://open.larksuite.com)
  GITHUB_SHA                        optional, printed in the doc's header line

`--dry-run` only writes the markdown that would be uploaded, so it needs no credentials.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import book_structure  # noqa: E402

ROOT = book_structure.ROOT
FIGURES = ROOT / "assets/figures"
IMAGE_LINK_RE = re.compile(r"!\[([^\]]*)\]\([^)\s]*?([^/)\s]+)\.svg\)")
FIGURE_URL = "https://figures.invalid/{}.png"
BATCH = 400  # blocks per descendant call; the API allows 1000


# ---------- markdown ----------

def book_markdown(sha: str) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "book.md"
        book_structure.assemble(out)
        text = out.read_text(encoding="utf-8")

    # Feishu has no footnotes: number them by first reference and keep each definition where it stands.
    numbers: dict[str, int] = {}
    for key in book_structure.REF_RE.findall(text):
        numbers.setdefault(key, len(numbers) + 1)
    text = book_structure.DEF_RE.sub(lambda m: f"［{numbers.get(m.group(1), '?')}］", text)
    text = book_structure.REF_RE.sub(lambda m: f"［{numbers[m.group(1)]}］", text)

    # Figures point at a placeholder URL that sync() maps back to the PNG; the caption stays visible.
    text = IMAGE_LINK_RE.sub(lambda m: f"![{m.group(1)}]({FIGURE_URL.format(m.group(2))})\n\n*{m.group(1)}*", text)

    stamp = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M")
    header = (
        f"> 本文档由 GitHub 仓库自动同步，最后同步于 {stamp}（提交 {sha[:7] or '本地'}）。"
        "请在仓库里修改书稿，在这里直接改动的内容会在下次同步时被覆盖。\n\n"
    )
    return header + text


# ---------- Feishu API ----------

class Feishu:
    def __init__(self, base: str, app_id: str, secret: str) -> None:
        self.base = base.rstrip("/")
        self.token = ""
        self.token = self.call("POST", "/open-apis/auth/v3/tenant_access_token/internal",
                               {"app_id": app_id, "app_secret": secret}, raw=True)["tenant_access_token"]

    def call(self, method: str, path: str, body=None, query=None, raw=False, data=None, ctype=None):
        url = self.base + path + ("?" + urllib.parse.urlencode(query) if query else "")
        if data is None and body is not None:
            data, ctype = json.dumps(body).encode(), "application/json; charset=utf-8"
        for attempt in range(6):
            req = urllib.request.Request(url, data=data, method=method)
            if ctype:
                req.add_header("Content-Type", ctype)
            if self.token:
                req.add_header("Authorization", f"Bearer {self.token}")
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    payload = json.loads(resp.read())
            except urllib.error.HTTPError as err:
                payload = json.loads(err.read() or b"{}")
                if err.code == 429 or payload.get("code") == 99991400:
                    time.sleep(2 ** attempt)
                    continue
            if payload.get("code", 0) != 0:
                raise SystemExit(f"{method} {path} failed: {payload.get('code')} {payload.get('msg')}")
            time.sleep(0.35)  # per-document edit limit is 3 requests a second
            return payload if raw else payload.get("data", {})
        raise SystemExit(f"{method} {path}: still rate limited after retries")

    def upload_image(self, doc_id: str, block_id: str, png: Path) -> str:
        content = png.read_bytes()
        boundary = uuid.uuid4().hex
        fields = {
            "file_name": png.name,
            "parent_type": "docx_image",
            "parent_node": block_id,
            "size": str(len(content)),
            "extra": json.dumps({"drive_route_token": doc_id}),
        }
        parts = [f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
                 for k, v in fields.items()]
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{png.name}"\r\n'
                     "Content-Type: image/png\r\n\r\n".encode() + content + b"\r\n")
        parts.append(f"--{boundary}--\r\n".encode())
        data = self.call("POST", "/open-apis/drive/v1/medias/upload_all", data=b"".join(parts),
                         ctype=f"multipart/form-data; boundary={boundary}")
        return data["file_token"]


def doc_id_from(target: str, api: Feishu) -> str:
    match = re.search(r"/(docx|wiki)/([A-Za-z0-9]+)", target)
    kind, token = match.groups() if match else ("docx", target.strip())
    if kind == "wiki":
        node = api.call("GET", "/open-apis/wiki/v2/spaces/get_node", query={"token": token})["node"]
        if node["obj_type"] != "docx":
            raise SystemExit(f"wiki node is a {node['obj_type']}, not a docx document")
        return node["obj_token"]
    return token


def subtree(root: str, by_id: dict) -> list[dict]:
    out, stack = [], [root]
    while stack:
        block = by_id[stack.pop()]
        if block.get("block_type") == 31:  # table: merge_info is read-only and rejected on insert
            block.get("table", {}).get("property", {}).pop("merge_info", None)
        out.append(block)
        stack.extend(reversed(block.get("children", [])))
    return out


def sync(markdown: str) -> None:
    for var in ("FEISHU_APP_ID", "FEISHU_APP_SECRET", "FEISHU_DOC"):
        if not os.environ.get(var):
            raise SystemExit(f"{var} is not set")
    api = Feishu(os.environ.get("FEISHU_BASE", "https://open.feishu.cn"),
                 os.environ["FEISHU_APP_ID"], os.environ["FEISHU_APP_SECRET"])
    doc = doc_id_from(os.environ["FEISHU_DOC"], api)
    rev = {"document_revision_id": -1}

    converted = api.call("POST", "/open-apis/docx/v1/documents/blocks/convert",
                         {"content_type": "markdown", "content": markdown})
    by_id = {b["block_id"]: b for b in converted["blocks"]}
    images = {i["block_id"]: i["image_url"] for i in converted.get("block_id_to_image_urls", [])}

    existing = api.call("GET", f"/open-apis/docx/v1/documents/{doc}/blocks/{doc}")["block"].get("children", [])
    if existing:
        api.call("DELETE", f"/open-apis/docx/v1/documents/{doc}/blocks/{doc}/children/batch_delete",
                 {"start_index": 0, "end_index": len(existing)}, query=rev)

    real_ids: dict[str, str] = {}
    index, group, blocks = 0, [], []
    tops = converted["first_level_block_ids"]
    for n, top in enumerate(tops):
        tree = subtree(top, by_id)
        group.append(top)
        blocks.extend(tree)
        if n == len(tops) - 1 or len(blocks) + len(subtree(tops[n + 1], by_id)) > BATCH:
            made = api.call("POST", f"/open-apis/docx/v1/documents/{doc}/blocks/{doc}/descendant",
                            {"children_id": group, "index": index, "descendants": blocks}, query=rev)
            real_ids.update({r["temporary_block_id"]: r["block_id"] for r in made.get("block_id_relations", [])})
            index += len(group)
            group, blocks = [], []
    print(f"wrote {index} top-level blocks")

    for temp_id, url in images.items():
        name = url.rsplit("/", 1)[-1]
        png = FIGURES / name
        block_id = real_ids.get(temp_id)
        if not png.exists() or not block_id:
            print(f"skipped figure {name}", file=sys.stderr)
            continue
        token = api.upload_image(doc, block_id, png)
        api.call("PATCH", f"/open-apis/docx/v1/documents/{doc}/blocks/{block_id}",
                 {"replace_image": {"token": token}}, query=rev)
    print(f"uploaded {len(images)} figures to {doc}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", type=Path, metavar="OUT", help="write the upload markdown here and stop")
    args = parser.parse_args()
    markdown = book_markdown(os.environ.get("GITHUB_SHA", ""))
    if args.dry_run:
        args.dry_run.write_text(markdown, encoding="utf-8")
        print(f"wrote {args.dry_run}")
        return 0
    sync(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
