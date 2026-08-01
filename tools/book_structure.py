#!/usr/bin/env python3
"""Split, assemble, and validate the publication-oriented book structure."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Chapter:
    source: str
    target: str
    part: str
    number: str
    kind: str = "chapter"


CHAPTERS = [
    Chapter("01_第一部_看见依赖/00_序章_智能权力的重新分配.md", "01_第一部_看见依赖/00_序章_智能权力的重新分配", "第一部　看见依赖", "序章", "prologue"),
    Chapter("01_第一部_看见依赖/01_当选择悄悄消失.md", "01_第一部_看见依赖/01_第一章_Token工厂_AI怎样成为基础设施", "第一部　看见依赖", "第一章"),
    Chapter("01_第一部_看见依赖/02_什么是AI主权.md", "01_第一部_看见依赖/02_第二章_为什么AI需要主权", "第一部　看见依赖", "第二章"),
    Chapter("02_第二部_四级AI主权/03_个人_AI主权从自己开始.md", "02_第二部_四级AI主权/03_第三章_个人_AI主权从自己开始", "第二部　建设四级AI主权", "第三章"),
    Chapter("02_第二部_四级AI主权/04_组织_守住共同体的边界.md", "02_第二部_四级AI主权/04_第四章_组织_守住共同体的边界", "第二部　建设四级AI主权", "第四章"),
    Chapter("02_第二部_四级AI主权/05_企业_把智能变成可治理的能力.md", "02_第二部_四级AI主权/05_第五章_企业_把智能变成可治理的能力", "第二部　建设四级AI主权", "第五章"),
    Chapter("02_第二部_四级AI主权/06_政府与国家_智能基础设施由谁决定.md", "02_第二部_四级AI主权/06_第六章_政府与国家_让智能沉淀为共同能力", "第二部　建设四级AI主权", "第六章"),
    Chapter("03_第三部_在依赖中保持自由/07_在依赖中保持自由.md", "03_第三部_在依赖中保持自由/07_第七章_在依赖中保持自由", "第三部　在依赖中保持自由", "第七章"),
    Chapter("04_结语/00_把选择留在自己手里.md", "04_结语/00_结语_把选择留在自己手里", "结语", "结语", "epilogue"),
]


ARTWORK = {
    ("序章", "能力扩散与控制集中同时发生"): "图序-1",
    ("第一章", "一次回答，其实经过两条生产线"): "图1-1",
    ("第一章", "真正工作的不是一个模型，而是一张能力网络"): "图1-2",
    ("第一章", "开源打开的是哪一道门"): "图1-3",
    ("第二章", "一次请求，不等于一项任务"): "图2-1",
    ("第二章", "六种可以检验的能力"): "图2-2",
    ("第二章", "四个层级，一条责任链"): "图2-3",
    ("第三章", "三种隐私模式，而不是一种绝对安全"): "图3-1",
    ("第三章", "一套可搬走的个人智能栈"): "图3-2",
    ("第四章", "一项任务会跨过多个信任边界"): "图4-1",
    ("第四章", "一次批准不能覆盖整个生命周期"): "图4-2",
    ("第五章", "企业真正运行的是一张能力网络"): "图5-1",
    ("第五章", "执行凭证：让一次任务可以被复盘"): "图5-2",
    ("第五章", "企业版AgenticOps：管理智能体生命周期"): "图5-3",
    ("第六章", "国家能力藏在危机到来以后"): "图6-1",
    ("第六章", "宜昌：一座城市怎样从资源投入走向能力反哺"): "图6-2",
    ("第七章", "开放控制面：让驾驶舱不被发动机锁住"): "图7-1",
    ("第七章", "到二〇三五年：六个可以被未来检验的判断"): "图7-2",
}


def safe_name(title: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|]", "_", title)
    name = re.sub(r"\s+", "_", name.strip())
    return name.rstrip("._")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("Unclosed frontmatter")
    body = text[end + 5 :]
    if body.startswith("\n"):
        body = body[1:]
    return text[: end + 5], body


def normalize_file_body(body: str) -> str:
    """Keep one terminal newline in a standalone Markdown unit."""
    return body.rstrip() + "\n"


def frontmatter(chapter: Chapter, unit_type: str, section: str, title: str, order: int, artwork: str | None) -> str:
    fields = {
        "unit_type": unit_type,
        "part": chapter.part,
        "chapter": chapter.number,
        "section": section,
        "title": title,
        "order": order,
        "editorial_stage": "待出版初审",
        "fact_check": "沿用正文时间锚点，出版冻结前复核",
        "artwork": artwork or "无预设；编辑审读时复核",
    }
    body = "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in fields.items())
    return f"---\n{body}\n---\n\n"


def parse_monolith(text: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(re.finditer(r"(?m)^## ([^\n]+)\n", text))
    if not matches:
        raise ValueError("No level-2 section headings found")
    intro = text[: matches[0].start()]
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), text[match.start() : end]))
    return intro, sections


def title_from_intro(intro: str) -> str:
    match = re.search(r"(?m)^# ([^\n]+)", intro)
    if not match:
        raise ValueError("Missing chapter title")
    return match.group(1).strip()


def assembled_body(target: Path) -> str:
    chunks = []
    for path in sorted(target.glob("[0-9][0-9]_*.md")):
        _, body = split_frontmatter(path.read_text(encoding="utf-8"))
        chunks.append(body)
    return "\n".join(chunks)


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_all(apply: bool) -> None:
    plans = []
    for chapter in CHAPTERS:
        source = ROOT / chapter.source
        target = ROOT / chapter.target
        if not source.exists():
            if target.exists():
                print(f"skip: already split {chapter.number}")
                continue
            raise FileNotFoundError(source)
        if target.exists():
            raise FileExistsError(target)
        original = source.read_text(encoding="utf-8")
        intro, sections = parse_monolith(original)
        plans.append((chapter, source, target, original, intro, sections))

    for chapter, source, target, original, intro, sections in plans:
        print(f"{chapter.number}: {len(sections)} sections -> {target.relative_to(ROOT)}")
        if not apply:
            continue
        target.mkdir(parents=True)
        chapter_title = title_from_intro(intro)
        (target / "00_章节导读.md").write_text(
            frontmatter(chapter, "chapter", "章导读", chapter_title, 0, None) + normalize_file_body(intro),
            encoding="utf-8",
        )
        for index, (section_title, body) in enumerate(sections, 1):
            section_number = f"{chapter.number}.{index}" if chapter.kind == "chapter" else f"{chapter.number}-{index}"
            artwork = ARTWORK.get((chapter.number, section_title))
            marker = ""
            if artwork:
                marker = (
                    f"<!-- 图稿需求：{artwork}；具体形式、位置、构图、版权与交付要求见 "
                    "90_出版工作台/02_图稿清单.md。此注释不进入排版正文。 -->\n"
                )
                heading_end = body.find("\n") + 1
                body = body[:heading_end] + marker + body[heading_end:]
            filename = f"{index:02d}_{safe_name(section_title)}.md"
            (target / filename).write_text(
                frontmatter(chapter, "section", section_number, section_title, index, artwork) + normalize_file_body(body),
                encoding="utf-8",
            )

        rebuilt = assembled_body(target)
        expected = normalize_file_body(original)
        # Artwork comments are editorial metadata and are removed for the body-equivalence check.
        rebuilt_without_markers = re.sub(r"<!-- 图稿需求：.*?-->\n", "", rebuilt)
        if rebuilt_without_markers != expected:
            shutil.rmtree(target)
            raise RuntimeError(f"Body mismatch after splitting {chapter.number}")
        source.unlink()
        print(f"verified: {chapter.number} sha256={digest(expected)[:12]}")


def validate() -> int:
    failures = 0
    total_sections = 0
    for chapter in CHAPTERS:
        target = ROOT / chapter.target
        files = sorted(target.glob("[0-9][0-9]_*.md")) if target.exists() else []
        if not files or files[0].name != "00_章节导读.md":
            print(f"FAIL {chapter.number}: missing chapter directory or guide")
            failures += 1
            continue
        expected_orders = list(range(len(files)))
        actual_orders = [int(path.name[:2]) for path in files]
        if actual_orders != expected_orders:
            print(f"FAIL {chapter.number}: discontinuous file order {actual_orders}")
            failures += 1
        h1 = 0
        h2 = 0
        for path in files:
            _, body = split_frontmatter(path.read_text(encoding="utf-8"))
            h1 += len(re.findall(r"(?m)^# ", body))
            h2 += len(re.findall(r"(?m)^## ", body))
            if path.name.startswith("00_") and not re.search(r"(?m)^# ", body):
                print(f"FAIL {path.relative_to(ROOT)}: guide has no chapter title")
                failures += 1
            if not path.name.startswith("00_") and len(re.findall(r"(?m)^## ", body)) != 1:
                print(f"FAIL {path.relative_to(ROOT)}: section must contain exactly one H2")
                failures += 1
        total_sections += h2
        if h1 != 1 or h2 != len(files) - 1:
            print(f"FAIL {chapter.number}: H1={h1}, H2={h2}, files={len(files)}")
            failures += 1
        else:
            print(f"OK {chapter.number}: {h2} sections")
    print(f"summary: {len(CHAPTERS)} chapter units, {total_sections} sections, {failures} failures")
    return 1 if failures else 0


def assemble(output: Path) -> None:
    chunks = []
    for chapter in CHAPTERS:
        chunks.append(assembled_body(ROOT / chapter.target))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(chunks), encoding="utf-8")
    print(output)


def promote_h3_units() -> None:
    """Promote publication-sized H3 blocks in known overloaded sections."""
    targets = {
        "第六章": {"国家能力要在产业和公共任务中持续增值"},
        "第七章": {"开放的力量与代价"},
    }
    for chapter in CHAPTERS:
        wanted = targets.get(chapter.number)
        if not wanted:
            continue
        target = ROOT / chapter.target
        source_files = sorted(target.glob("[0-9][0-9]_*.md"))[1:]
        units: list[tuple[str, str]] = []
        promoted = 0
        _, guide_body = split_frontmatter((target / "00_章节导读.md").read_text(encoding="utf-8"))
        expected_bodies = [guide_body]
        for path in source_files:
            _, body = split_frontmatter(path.read_text(encoding="utf-8"))
            h2 = re.search(r"(?m)^## ([^\n]+)", body)
            if not h2:
                raise ValueError(f"Missing H2 in {path}")
            title = h2.group(1).strip()
            if title not in wanted:
                units.append((title, body))
                expected_bodies.append(body)
                continue
            matches = list(re.finditer(r"(?m)^### ([^\n]+)\n", body))
            if not matches:
                units.append((title, body))
                expected_bodies.append(body)
                continue
            intro = body[: matches[0].start()]
            units.append((title, intro))
            expected_bodies.append(intro)
            for index, match in enumerate(matches):
                end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
                block = body[match.start() : end]
                promoted_title = match.group(1).strip()
                promoted_body = re.sub(r"^### ", "## ", block, count=1)
                units.append((promoted_title, promoted_body))
                expected_bodies.append(promoted_body)
                promoted += 1

        if promoted == 0:
            print(f"skip: {chapter.number} publication-sized H3 units already promoted")
            continue
        temp = target.with_name(target.name + ".__optimize_tmp")
        backup = target.with_name(target.name + ".__before_optimize")
        if temp.exists() or backup.exists():
            raise FileExistsError(f"Temporary optimization path exists for {chapter.number}")
        temp.mkdir()
        shutil.copy2(target / "00_章节导读.md", temp / "00_章节导读.md")
        for order, (title, body) in enumerate(units, 1):
            artwork_match = re.search(r"图稿需求：(图[^；]+)；", body)
            artwork = artwork_match.group(1) if artwork_match else None
            section_number = f"{chapter.number}.{order}"
            filename = f"{order:02d}_{safe_name(title)}.md"
            (temp / filename).write_text(
                frontmatter(chapter, "section", section_number, title, order, artwork) + normalize_file_body(body),
                encoding="utf-8",
            )
        rebuilt = assembled_body(temp)
        expected = "\n".join(normalize_file_body(body) for body in expected_bodies)
        if rebuilt != expected:
            shutil.rmtree(temp)
            raise RuntimeError(f"Optimized body mismatch in {chapter.number}")
        target.rename(backup)
        try:
            temp.rename(target)
        except Exception:
            backup.rename(target)
            raise
        shutil.rmtree(backup)
        print(f"optimized {chapter.number}: promoted {promoted} H3 units; now {len(units)} sections")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    split_parser = sub.add_parser("split")
    split_parser.add_argument("--apply", action="store_true")
    sub.add_parser("validate")
    sub.add_parser("optimize")
    assemble_parser = sub.add_parser("assemble")
    assemble_parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.command == "split":
        split_all(args.apply)
        return 0
    if args.command == "validate":
        return validate()
    if args.command == "optimize":
        promote_h3_units()
        return validate()
    if args.command == "assemble":
        assemble(args.output)
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
