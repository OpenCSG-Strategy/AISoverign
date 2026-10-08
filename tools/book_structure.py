#!/usr/bin/env python3
"""Validate and assemble the book: 序章＋三部七章＋结语＋附录."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PART_DIRS = ["01_第一部_依赖", "02_第二部_建造", "03_第三部_自由", "04_结语"]
APPENDIX_DIR = ROOT / "05_附录"
ENDNOTES = APPENDIX_DIR / "附录B_精选尾注.md"
UNIT_RE = re.compile(r"^\d\d_(序章|第.+章|结语)_")
SECTION_RE = re.compile(r"^(\d\d)_.+\.md$")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
REF_RE = re.compile(r"\[\^([^\]]+)\](?!:)")
DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.M)
HAN_RE = re.compile(r"[一-鿿]")


def manuscript() -> list[Path]:
    """Every body file in reading order: part guide, then each unit's intro and sections."""
    files: list[Path] = []
    for part in PART_DIRS:
        for entry in sorted((ROOT / part).iterdir()):
            if entry.is_file() and entry.suffix == ".md":
                files.append(entry)
            elif entry.is_dir() and UNIT_RE.match(entry.name):
                files.extend(sorted(entry.glob("*.md")))
    return files


def appendices() -> list[Path]:
    return sorted(APPENDIX_DIR.glob("附录*.md"))


def units() -> list[Path]:
    return [d for part in PART_DIRS for d in sorted((ROOT / part).iterdir()) if d.is_dir() and UNIT_RE.match(d.name)]


def validate() -> int:
    failures: list[str] = []

    for part in PART_DIRS[:3]:
        if not list((ROOT / part).glob("00_第*部导读.md")):
            failures.append(f"{part}: missing part guide")

    sections = 0
    for unit in units():
        intro = unit / "00_章节导读.md"
        if not intro.exists() or not intro.read_text(encoding="utf-8").startswith("# "):
            failures.append(f"{unit.relative_to(ROOT)}: 00_章节导读.md missing or lacks '# ' title")
        numbers = []
        for f in sorted(unit.glob("*.md")):
            if f.name == "00_章节导读.md":
                continue
            m = SECTION_RE.match(f.name)
            if not m:
                failures.append(f"{f.relative_to(ROOT)}: bad file name")
                continue
            numbers.append(int(m.group(1)))
            if not f.read_text(encoding="utf-8").lstrip().startswith("## "):
                failures.append(f"{f.relative_to(ROOT)}: section must open with '## '")
        if numbers != list(range(1, len(numbers) + 1)):
            failures.append(f"{unit.relative_to(ROOT)}: section numbers {numbers} not consecutive")
        sections += len(numbers)

    body = manuscript() + [p for p in appendices() if p != ENDNOTES]
    refs: set[str] = set()
    figures = 0
    for f in body:
        text = f.read_text(encoding="utf-8")
        refs.update(REF_RE.findall(text))
        for link in IMAGE_RE.findall(text):
            figures += 1
            if not (f.parent / link).resolve().exists():
                failures.append(f"{f.relative_to(ROOT)}: missing image {link}")

    defined = DEF_RE.findall(ENDNOTES.read_text(encoding="utf-8"))
    dupes = sorted({k for k in defined if defined.count(k) > 1})
    failures += [f"附录B: duplicate definition [^{k}]" for k in dupes]
    failures += [f"undefined footnote [^{k}]" for k in sorted(refs - set(defined))]
    failures += [f"附录B: unused definition [^{k}]" for k in sorted(set(defined) - refs)]

    han = sum(len(HAN_RE.findall(f.read_text(encoding="utf-8"))) for f in manuscript())
    for line in failures:
        print(f"FAIL {line}")
    print(f"{len(units())} units, {sections} sections, {figures} figures, "
          f"{len(set(defined))} endnotes, {han:,} 汉字 in body, {len(failures)} failures")
    return 1 if failures else 0


def assemble(output: Path) -> None:
    output = output.resolve()
    parts = []
    for f in manuscript() + appendices():
        text = f.read_text(encoding="utf-8").strip()
        text = IMAGE_RE.sub(
            lambda m: m.group(0).replace(m.group(1), os.path.relpath((f.parent / m.group(1)).resolve(), output.parent)),
            text,
        )
        parts.append(text)
    output.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"wrote {output}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    assemble_parser = sub.add_parser("assemble")
    assemble_parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.command == "validate":
        return validate()
    assemble(args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
