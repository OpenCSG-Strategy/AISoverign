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
    Chapter("01_第一部_当AI成为基础设施/00_序章_智能权力的重新分配.md", "01_第一部_当AI成为基础设施/00_序章_智能权力的重新分配", "第一部　当AI成为基础设施", "序章", "prologue"),
    Chapter("01_第一部_当AI成为基础设施/01_当选择悄悄消失.md", "01_第一部_当AI成为基础设施/01_第一章_Token工厂_AI怎样成为基础设施", "第一部　当AI成为基础设施", "第一章"),
    Chapter("01_第一部_当AI成为基础设施/02_模型走出工厂.md", "01_第一部_当AI成为基础设施/02_第二章_模型走出工厂_能力怎样扩散与组合", "第一部　当AI成为基础设施", "第二章"),
    Chapter("01_第一部_当AI成为基础设施/03_什么是AI主权.md", "01_第一部_当AI成为基础设施/03_第三章_为什么AI需要主权", "第一部　当AI成为基础设施", "第三章"),
    Chapter("01_第一部_当AI成为基础设施/04_AgenticOps.md", "01_第一部_当AI成为基础设施/04_第四章_AgenticOps_管理会行动的AI", "第一部　当AI成为基础设施", "第四章"),
    Chapter("02_第二部_主权是建出来的/05_个人_AI主权从自己开始.md", "02_第二部_主权是建出来的/05_第五章_个人_AI主权从自己开始", "第二部　主权是建出来的", "第五章"),
    Chapter("02_第二部_主权是建出来的/06_组织_让部门自治而能力协同.md", "02_第二部_主权是建出来的/06_第六章_组织_让部门自治而能力协同", "第二部　主权是建出来的", "第六章"),
    Chapter("02_第二部_主权是建出来的/07_企业_把智能变成可治理的能力.md", "02_第二部_主权是建出来的/07_第七章_企业_把智能变成可治理的能力", "第二部　主权是建出来的", "第七章"),
    Chapter("02_第二部_主权是建出来的/08_国家与城市_让智能沉淀为本地生态.md", "02_第二部_主权是建出来的/08_第八章_国家与城市_让智能沉淀为本地生态", "第二部　主权是建出来的", "第八章"),
    Chapter("03_第三部_在依赖中争取自由/09_安全协议与审计.md", "03_第三部_在依赖中争取自由/09_第九章_安全协议与审计_依赖怎样不变成支配", "第三部　在依赖中争取自由", "第九章"),
    Chapter("03_第三部_在依赖中争取自由/10_开放.md", "03_第三部_在依赖中争取自由/10_第十章_开放_力量代价与现实检验", "第三部　在依赖中争取自由", "第十章"),
    Chapter("03_第三部_在依赖中争取自由/11_协同与组织.md", "03_第三部_在依赖中争取自由/11_第十一章_协同与组织_让自由长成更大的整体", "第三部　在依赖中争取自由", "第十一章"),
    Chapter("04_结语/00_把选择留在自己手里.md", "04_结语/00_结语_把选择留在自己手里", "结语", "结语", "epilogue"),
]


PART_GUIDES_AFTER = {
    "序章": "01_第一部_当AI成为基础设施/00_第一部导读.md",
    "第四章": "02_第二部_主权是建出来的/00_第二部导读.md",
    "第八章": "03_第三部_在依赖中争取自由/00_第三部导读.md",
}


ARTWORK = {
    ("序章", "能力扩散与控制集中同时发生"): "图序-1",
    ("序章", "智能正在从答案进入生产关系"): "图序-2",
    ("序章", "智能正在改变企业的最小规模"): "图序-3",
    ("序章", "世界正在从模型竞赛转向能力体系竞争"): "图序-4",
    ("序章", "主权为什么在这个时代重新出现"): "图序-5",
    ("序章", "四级主权是一条能力与责任链"): "图序-6",
    ("序章", "控制能力比模型排名更重要"): "图序-7",
    ("第一章", "Token工厂有多重"): "图1-2",
    ("第一章", "训练阶段：模型怎样建成"): "图1-3",
    ("第一章", "一枚Token是什么"): "图1-4",
    ("第一章", "一次回答，其实经过两条生产线"): "图1-1",
    ("第一章", "一座Token工厂里有什么"): "图1-5",
    ("第二章", "章导读"): "图2-0",
    ("第二章", "模型为什么同时变大又变小"): "图2-1",
    ("第二章", "一条可追溯的能力谱系"): "图2-2",
    ("第二章", "开源打开的是哪一道门"): "图2-3",
    ("第二章", "模型之外的能力网络"): "图2-4",
    ("第二章", "本地与云端，不是一场只能选一边的战争"): "图2-5",
    ("第二章", "当输出越过屏幕"): "图2-6",
    ("第三章", "六种可以检验的能力"): "图3-1",
    ("第三章", "四个层级，一条责任链"): "图3-2",
    ("第三章", "一个Agent由什么组成"): "图3-3",
    ("第三章", "一次请求正在变成一项任务"): "图3-4",
    ("第三章", "当机器进入现实"): "图3-5",
    ("第三章", "为什么这会成为主权问题"): "图3-6",
    ("第三章", "主权怎样容纳委托与合作"): "图3-7",
    ("第三章", "主权必须在运行中成立"): "图3-8",
    ("第三章", "谁仍是行动的作者"): "图3-9",
    ("第三章", "最低可行主权"): "图3-10",
    ("第四章", "三个循环和一个控制面"): "图4-1",
    ("第四章", "任务契约：先约定什么才算完成"): "图4-2",
    ("第四章", "交付循环：先定义失败，再允许上线"): "图4-3",
    ("第四章", "运行循环：看见过程，也要核验结果"): "图4-4",
    ("第四章", "从DevOps到AgenticOps"): "图4-5",
    ("第四章", "管理八类相互关联的对象"): "图4-6",
    ("第四章", "身份必须跟着任务走"): "图4-7",
    ("第四章", "失败以后怎样停止与恢复"): "图4-8",
    ("第四章", "学习循环：反馈怎样进入改进"): "图4-9",
    ("第四章", "一张订单怎样穿过一家工厂"): "图4-10",
    ("第四章", "最低可行AgenticOps"): "图4-11",
    ("第五章", "本地、受控云与公共云"): "图5-1",
    ("第五章", "一套可搬走的个人智能栈"): "图5-2、图5-9",
    ("第五章", "个人智能资产怎样形成"): "图5-3、图5-4",
    ("第五章", "注意力与判断不能一起外包"): "图5-5、图5-7",
    ("第五章", "从回答问题到代表你行动"): "图5-6、图5-8",
    ("第五章", "怎样判断个人系统仍然可控"): "图5-10",
    ("第五章", "OPC：企业的最小有效规模正在下降"): "图5-11、图5-12",
    ("第五章", "OPC的一天：效率如何变成秩序"): "图5-13",
    ("第六章", "每个部门都应有自己的AI域"): "图6-1",
    ("第六章", "一次产品发布怎样穿过五个部门"): "图6-2",
    ("第六章", "企业内部也有主权边界"): "图6-3",
    ("第六章", "最小披露必须写成数据契约"): "图6-4",
    ("第六章", "联邦检索与属地执行"): "图6-5",
    ("第六章", "智能体怎样发现彼此并获得委托"): "图6-6",
    ("第六章", "共享控制面怎样保持分权"): "图6-7",
    ("第六章", "冲突、例外与六项压力测试"): "图6-8",
    ("第七章", "企业运行的是一张能力网络"): "图7-1",
    ("第七章", "租用结果，还是吸收能力"): "图7-2",
    ("第七章", "一项生产任务会在哪里断裂"): "图7-3",
    ("第七章", "错误怎样进入行业现场"): "图7-4",
    ("第七章", "当“聪明”不再是唯一稀缺品"): "图7-6",
    ("第七章", "模型网关：把选择留在应用之外"): "图7-7",
    ("第七章", "从Token成本到任务经济学"): "图7-8",
    ("第七章", "七天测试：让三本账对上现实"): "图7-9",
    ("第八章", "国家与城市主权必须同时过两道关"): "图8-1",
    ("第八章", "宜昌：一座城市怎样把绿色算力接上生态"): "图8-2",
    ("第九章", "开放控制面：让驾驶舱不被发动机锁住"): "图9-1",
    ("第十一章", "到二〇三五年：六项可验证预测"): "图11-1",
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
    for part_guide in PART_GUIDES_AFTER.values():
        path = ROOT / part_guide
        if not path.exists():
            print(f"FAIL part guide: missing {part_guide}")
            failures += 1
            continue
        _, body = split_frontmatter(path.read_text(encoding="utf-8"))
        if len(re.findall(r"(?m)^# ", body)) != 1:
            print(f"FAIL part guide: expected one H1 in {part_guide}")
            failures += 1
        else:
            print(f"OK part guide: {part_guide}")
    print(f"summary: {len(CHAPTERS)} chapter units, {total_sections} sections, {failures} failures")
    return 1 if failures else 0


def assemble(output: Path) -> None:
    chunks = []
    for chapter in CHAPTERS:
        chunks.append(assembled_body(ROOT / chapter.target))
        part_guide = PART_GUIDES_AFTER.get(chapter.number)
        if part_guide:
            _, body = split_frontmatter((ROOT / part_guide).read_text(encoding="utf-8"))
            chunks.append(normalize_file_body(body))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(chunks), encoding="utf-8")
    print(output)


def promote_h3_units() -> None:
    """Promote publication-sized H3 blocks in known overloaded sections."""
    targets = {
        "第十章": {"开放的力量与代价"},
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


PART2_COMPACTION = {
    "第五章": [
        ("个人智能资产怎样形成", [1, 2]),
        ("本地、受控云与公共云", [3]),
        ("注意力与判断不能一起外包", [4, 6]),
        ("从回答问题到代表你行动", [5, 8]),
        ("一套可搬走的个人智能栈", [7, 9]),
        ("怎样判断个人系统仍然可控", [10]),
        ("OPC：企业的最小有效规模正在下降", [11, 12]),
        ("OPC的一天：效率如何变成秩序", [13]),
    ],
    "第六章": [
        ("企业内部也有主权边界", [1, 2]),
        ("每个部门都应有自己的AI域", [3, 4]),
        ("数据契约先于数据流动", [5, 6]),
        ("联邦检索与属地执行", [7, 8]),
        ("智能体怎样发现彼此并获得委托", [9, 11]),
        ("一次产品发布怎样穿过五个部门", [10]),
        ("共享控制面怎样保持分权", [12, 13]),
        ("冲突、例外与六项压力测试", [14, 15]),
    ],
    "第七章": [
        ("租用结果，还是吸收能力", [1]),
        ("一项生产任务会在哪里断裂", [2, 3]),
        ("错误怎样进入行业现场", [4, 5]),
        ("企业运行的是一张能力网络", [6, 7]),
        ("当“聪明”不再是唯一稀缺品", [8]),
        ("模型网关：把选择留在应用之外", [9]),
        ("从Token成本到任务经济学", [10]),
        ("七天测试：让三本账对上现实", [11, 12]),
    ],
}


PUBLIC_SOVEREIGNTY_MERGE = [
    ("国家与城市主权必须同时过两道关", [("government", 1), ("country", 1)]),
    ("三条国家路径，最后都要回答能力留在哪里", [("country", 2), ("country", 3), ("country", 4)]),
    ("城市是AI生态的落地接口", []),
    ("算力必须走进任务，才会留下能力", []),
    ("模型社区是城市的第二种基础设施", []),
    ("宜昌：一座城市怎样把绿色算力接上生态", [("country", 5)]),
    ("公共AI必须允许人申诉，也必须记得自己做过什么", [("government", 2), ("government", 3)]),
    ("数据、底座与替换构成公共边界", [("government", 4), ("government", 5), ("government", 6)]),
    ("智能体进入城市以后，谁有资格定义问题", [("government", 7), ("government", 8)]),
    ("生产主体决定生态会不会生长", [("country", 6)]),
    ("合作不能取消重新选择", [("country", 7), ("country", 8)]),
]


def merge_public_sovereignty() -> None:
    """Build one country/city sovereignty chapter from the former government and country chapters."""
    sources = {
        "government": ROOT / "02_第二部_主权是建出来的/08_第八章_政府_让公共权力接受约束",
        "country": ROOT / "02_第二部_主权是建出来的/09_第九章_国家_让智能沉淀为共同能力",
    }
    target = ROOT / "02_第二部_主权是建出来的/08_第八章_国家与城市_让智能沉淀为本地生态"
    if target.exists():
        print("skip: merged country/city sovereignty chapter already exists")
        return
    for source in sources.values():
        if not source.exists():
            raise FileNotFoundError(source)

    chapter = Chapter(
        "02_第二部_主权是建出来的/08_国家与城市_让智能沉淀为本地生态.md",
        str(target.relative_to(ROOT)),
        "第二部　主权是建出来的",
        "第八章",
    )
    by_source = {
        name: {
            int(path.name[:2]): path
            for path in directory.glob("[0-9][0-9]_*.md")
            if not path.name.startswith("00_")
        }
        for name, directory in sources.items()
    }
    target.mkdir()
    guide_title = "第八章　国家与城市：让智能沉淀为本地生态"
    guide_body = f"# {guide_title}\n\n待补：国家能力、城市生态与公共责任的合章导读。\n"
    (target / "00_章节导读.md").write_text(
        frontmatter(chapter, "chapter", "章导读", guide_title, 0, None) + guide_body,
        encoding="utf-8",
    )

    for new_order, (new_title, source_units) in enumerate(PUBLIC_SOVEREIGNTY_MERGE, 1):
        chunks = []
        artwork_ids = []
        for index, (source_name, old_order) in enumerate(source_units):
            path = by_source[source_name][old_order]
            _, body = split_frontmatter(path.read_text(encoding="utf-8"))
            artwork_ids.extend(re.findall(r"图稿需求：(图[^；]+)；", body))
            if index == 0:
                body = re.sub(r"(?m)^## [^\n]+$", f"## {new_title}", body, count=1)
            else:
                body = re.sub(r"(?m)^### ", "#### ", body)
                body = re.sub(r"(?m)^## ", "### ", body, count=1)
            chunks.append(body.rstrip())
        combined = "\n\n".join(chunks) + "\n" if chunks else f"## {new_title}\n"
        artwork = "、".join(dict.fromkeys(artwork_ids)) or None
        filename = f"{new_order:02d}_{safe_name(new_title)}.md"
        (target / filename).write_text(
            frontmatter(chapter, "section", f"第八章.{new_order}", new_title, new_order, artwork)
            + combined,
            encoding="utf-8",
        )
    print(f"created merged country/city sovereignty chapter: {len(PUBLIC_SOVEREIGNTY_MERGE)} sections")


def compact_part2() -> None:
    """Merge short Part II sections into eight progressive units per chapter."""
    chapters = {chapter.number: chapter for chapter in CHAPTERS}
    for number, groups in PART2_COMPACTION.items():
        chapter = chapters[number]
        target = ROOT / chapter.target
        files = sorted(target.glob("[0-9][0-9]_*.md"))
        if len(files) == 9:
            print(f"skip: {number} already compacted to 8 sections")
            continue
        by_order = {int(path.name[:2]): path for path in files if not path.name.startswith("00_")}
        expected = sorted(order for _, orders in groups for order in orders)
        if sorted(by_order) != expected:
            raise RuntimeError(
                f"{number}: expected source orders {expected}, found {sorted(by_order)}"
            )

        temp = target.with_name(target.name + ".__compact_tmp")
        backup = target.with_name(target.name + ".__before_compact")
        if temp.exists() or backup.exists():
            raise FileExistsError(f"Temporary compaction path exists for {number}")
        temp.mkdir()
        shutil.copy2(target / "00_章节导读.md", temp / "00_章节导读.md")

        for new_order, (new_title, source_orders) in enumerate(groups, 1):
            chunks = []
            artwork_ids = []
            for index, old_order in enumerate(source_orders):
                _, body = split_frontmatter(by_order[old_order].read_text(encoding="utf-8"))
                artwork_ids.extend(re.findall(r"图稿需求：(图[^；]+)；", body))
                if index == 0:
                    body = re.sub(r"(?m)^## [^\n]+$", f"## {new_title}", body, count=1)
                else:
                    body = re.sub(r"(?m)^### ", "#### ", body)
                    body = re.sub(r"(?m)^## ", "### ", body, count=1)
                chunks.append(body.rstrip())
            combined = "\n\n".join(chunks) + "\n"
            artwork = "、".join(dict.fromkeys(artwork_ids)) or None
            filename = f"{new_order:02d}_{safe_name(new_title)}.md"
            (temp / filename).write_text(
                frontmatter(chapter, "section", f"{number}.{new_order}", new_title, new_order, artwork)
                + combined,
                encoding="utf-8",
            )

        target.rename(backup)
        try:
            temp.rename(target)
        except Exception:
            backup.rename(target)
            raise
        shutil.rmtree(backup)
        print(f"compacted {number}: {len(files) - 1} -> {len(groups)} sections")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    split_parser = sub.add_parser("split")
    split_parser.add_argument("--apply", action="store_true")
    sub.add_parser("validate")
    sub.add_parser("optimize")
    sub.add_parser("compact-part2")
    sub.add_parser("merge-public-sovereignty")
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
    if args.command == "compact-part2":
        compact_part2()
        return validate()
    if args.command == "merge-public-sovereignty":
        merge_public_sovereignty()
        return 0
    if args.command == "assemble":
        assemble(args.output)
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
