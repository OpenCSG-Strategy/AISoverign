#!/usr/bin/env python3
"""Keep one Feishu doc in step with the book, figures included.

Every write ends with a check value in the doc's header line. Before the next write the doc is read back;
if its text no longer matches that value, someone edited it in Feishu, so nothing is overwritten. The
changed paragraphs are written to --report instead, to be carried back into the markdown by hand.

Environment:
  FEISHU_APP_ID, FEISHU_APP_SECRET  self-built app credentials
  FEISHU_DOC                        optional, the target doc's URL or token, default DEFAULT_DOC
  FEISHU_BASE                       optional, default https://open.feishu.cn (Lark: https://open.larksuite.com)
  FEISHU_FORCE                      optional, 1 overwrites even when the doc has unsynced edits
  GITHUB_SHA                        optional, printed in the doc's header line

`--dry-run` only writes the markdown that would be uploaded, so it needs no credentials.
`--check` only looks for edits made in Feishu and writes nothing.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import subprocess
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
DEFAULT_DOC = "https://opencsg-china.feishu.cn/wiki/IWEIwQby4iGx19kiCiCcGMBpnAc"
HEADER_MARK = "最后同步于"
HEADER_RE = re.compile(r"提交 ([0-9a-f]{7,40}).*?校验 ([0-9a-f]{12})")


# ---------- markdown ----------

def book_markdown(sha: str, root: Path = ROOT) -> str:
    """The upload markdown for the checkout at root (another commit's worktree when comparing)."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "book.md"
        subprocess.run([sys.executable, str(root / "tools/book_structure.py"), "assemble", str(out)],
                       check=True, stdout=subprocess.DEVNULL)
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
        f"本文档与 GitHub 仓库双向同步，{HEADER_MARK} {stamp}（提交 {sha[:7] or '本地'}）。"
        "可以直接在这里修改，下次同步前会先把这里的改动拉回书稿。\n\n"
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


def doc_id_from(target: str, api: Feishu) -> tuple[str, dict]:
    match = re.search(r"/(docx|wiki)/([A-Za-z0-9]+)", target)
    kind, token = match.groups() if match else ("docx", target.strip())
    if kind == "wiki":
        node = api.call("GET", "/open-apis/wiki/v2/spaces/get_node", query={"token": token})["node"]
        if node["obj_type"] != "docx":
            raise SystemExit(f"wiki node is a {node['obj_type']}, not a docx document")
        return node["obj_token"], node
    return token, {}


def block_text(block: dict) -> str:
    for value in block.values():
        if isinstance(value, dict) and isinstance(value.get("elements"), list):
            return "".join(e.get("text_run", {}).get("content", "")
                           or e.get("mention_doc", {}).get("title", "")
                           or e.get("equation", {}).get("content", "") for e in value["elements"])
    return ""


def texts_in_order(roots: list[str], by_id: dict) -> list[str]:
    """Text of every block under roots, depth first, empty ones dropped."""
    out = []
    for root in roots:
        for block in subtree(root, by_id):
            text = block_text(block).strip()
            if text:
                out.append(text)
    return out


def doc_texts(api: Feishu, doc: str) -> list[str]:
    by_id, page = {}, ""
    while True:
        query = {"page_size": 500, **({"page_token": page} if page else {})}
        data = api.call("GET", f"/open-apis/docx/v1/documents/{doc}/blocks", query=query)
        by_id.update({b["block_id"]: b for b in data.get("items", [])})
        page = data.get("page_token", "")
        if not data.get("has_more"):
            break
    return texts_in_order(by_id[doc].get("children", []), by_id)


def check_value(texts: list[str]) -> str:
    body = "\n".join(re.sub(r"\s+", "", t) for t in texts if HEADER_MARK not in t)
    return hashlib.sha256(body.encode()).hexdigest()[:12]


def edits_report(api: Feishu, texts: list[str], sha: str, node: dict) -> str:
    """The paragraphs that differ from what was written at commit sha."""
    with tempfile.TemporaryDirectory() as tmp:
        tree = Path(tmp) / "tree"
        subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "--detach", str(tree), sha],
                       check=True, capture_output=True)
        try:
            markdown = book_markdown(sha, tree)
        finally:
            subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(tree)], check=False)
    converted = api.call("POST", "/open-apis/docx/v1/documents/blocks/convert",
                         {"content_type": "markdown", "content": markdown})
    by_id = {b["block_id"]: b for b in converted["blocks"]}
    before = [t for t in texts_in_order(converted["first_level_block_ids"], by_id) if HEADER_MARK not in t]
    after = [t for t in texts if HEADER_MARK not in t]

    edited = ""
    if node.get("obj_edit_time"):
        when = datetime.fromtimestamp(int(node["obj_edit_time"]), timezone(timedelta(hours=8)))
        edited = f"，飞书文档最后修改于 {when:%Y-%m-%d %H:%M}"
    lines = [f"# 飞书上有待拉回的修改\n\n对照提交 {sha[:7]} 写入时的内容{edited}。\n"]
    norm = lambda xs: [re.sub(r"\s+", "", x) for x in xs]
    matcher = difflib.SequenceMatcher(None, norm(before), norm(after), autojunk=False)
    for op, i1, i2, j1, j2 in matcher.get_opcodes():
        if op == "equal":
            continue
        lines.append(f"## 第 {j1 + 1} 段附近（{ {'replace': '改动', 'delete': '删除', 'insert': '新增'}[op] }）\n")
        context = after[j1 - 1] if j1 else ""
        if context:
            lines.append(f"前一段：{context[:60]}\n")
        lines += [f"- 原文：{t}" for t in before[i1:i2]]
        lines += [f"+ 现在：{t}" for t in after[j1:j2]]
        lines.append("")
    return "\n".join(lines)


def subtree(root: str, by_id: dict) -> list[dict]:
    out, stack = [], [root]
    while stack:
        block = by_id[stack.pop()]
        if block.get("block_type") == 31:  # table: merge_info is read-only and rejected on insert
            block.get("table", {}).get("property", {}).pop("merge_info", None)
        out.append(block)
        stack.extend(reversed(block.get("children", [])))
    return out


def connect() -> tuple[Feishu, str, dict]:
    for var in ("FEISHU_APP_ID", "FEISHU_APP_SECRET"):
        if not os.environ.get(var):
            raise SystemExit(f"{var} is not set")
    api = Feishu(os.environ.get("FEISHU_BASE", "https://open.feishu.cn"),
                 os.environ["FEISHU_APP_ID"], os.environ["FEISHU_APP_SECRET"])
    doc, node = doc_id_from(os.environ.get("FEISHU_DOC") or DEFAULT_DOC, api)
    return api, doc, node


def unsynced_edits(api: Feishu, doc: str, node: dict) -> str:
    """A report of edits made in Feishu since the last write, or "" when there are none."""
    texts = doc_texts(api, doc)
    header = next((t for t in texts if HEADER_MARK in t), "")
    match = HEADER_RE.search(header)
    if match:
        sha, value = match.groups()
        return "" if check_value(texts) == value else edits_report(api, texts, sha, node)
    if any(HEADER_MARK not in t for t in texts):
        return "# 飞书文档里已有内容\n\n文档里有不是同步写入的内容，没有覆盖。确认可以覆盖后，设 FEISHU_FORCE=1 再运行。\n"
    return ""


def sync(markdown: str, api: Feishu, doc: str) -> None:
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

    # Seal the header with a check value of what Feishu now holds, so the next run can spot edits.
    header = block_text(by_id[tops[0]]).strip()
    value = check_value(doc_texts(api, doc))
    api.call("PATCH", f"/open-apis/docx/v1/documents/{doc}/blocks/{real_ids[tops[0]]}",
             {"update_text_elements": {"elements": [{"text_run": {"content": f"{header}（校验 {value}）"}}]}},
             query=rev)
    print(f"check value {value}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", type=Path, metavar="OUT", help="write the upload markdown here and stop")
    parser.add_argument("--check", action="store_true", help="only look for edits made in Feishu")
    parser.add_argument("--report", type=Path, default=Path("feishu-edits.md"),
                        help="where to write found edits (default feishu-edits.md)")
    args = parser.parse_args()
    if args.dry_run:
        args.dry_run.write_text(book_markdown(os.environ.get("GITHUB_SHA", "")), encoding="utf-8")
        print(f"wrote {args.dry_run}")
        return 0
    api, doc, node = connect()
    report = unsynced_edits(api, doc, node)
    if report:
        if len(report) > 60000:  # GitHub issue bodies stop at 65536 characters
            report = report[:60000] + "\n\n（修改太多，后面的省略了，请直接对照飞书文档。）\n"
        args.report.write_text(report, encoding="utf-8")
        print(report)
        if args.check or os.environ.get("FEISHU_FORCE") != "1":
            print(f"edits found in Feishu, nothing overwritten; see {args.report}", file=sys.stderr)
            return 2
    if args.check:
        print("no edits in Feishu since the last sync")
        return 0
    sync(book_markdown(os.environ.get("GITHUB_SHA", "")), api, doc)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
