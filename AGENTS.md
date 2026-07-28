# AGENTS.md — 《AI 主权》仓库的 AI 协作入口

> 任何 AI (Mavis / Claude / Codex / 其他) 接手本仓库, **先读这份文件**, 再决定下一步。

## 这是什么

Frank Chen 主理的中文书籍《AI 主权》原稿, 10 章 + 序章 + 结语 + 附录（2026-07 第三轮结构性合并后：3 部分→2 部分，8 章→10 章）。书稿结构见 `00_书稿导航.md`, 章节文件物理路径见 `README.md`。

## AI 进来看这三份索引, 别通读全书

| 索引 | 用途 | 文件 |
|------|------|------|
| **章节内容索引** | 每章一句话摘要 + 关键论点 + 最近更新时间 | `.content-index.md` |
| **主题标签索引** | 跨章节主题(开源/出口管制/AGI/协议/...) 在哪几章哪几节 | `.topic-tag-index.md` |
| **数据时间锚点** | 所有数据/政策/事件的"截至日期"标签 | `.data-source-index.md` |
| **待更新清单** | 当前最该补 / 改 / 删的章节段落, Frank 审核中 | `.update-todo.md` |

## 工作流: 增量更新三步

1. **先**看 `.update-todo.md` —— 找到当前最需要更新的具体段落(带文件:行号)
2. **再**用 `.content-index.md` 定位章节, 用 `.topic-tag-index.md` 找跨章节影响
3. **最后**才读 `99_本章参考文献.md` 核对脚注和数据来源

> **不要**从 `01_第一部分_AI主权的觉醒/00_第一部分导读.md` 一路读到尾。每次都从索引开始, 单章深读, 避免重复劳动。

## 调研档案

`/Users/fangchen/Baidu/GitHub/AISoverignBook/.research/`

- `YYYY-MM-update/` —— 每次调研开新目录(如 `2026-07-update/`)
- 每个目录里: `0X-xxx.md` 子报告 + `99-summary.md` 综合
- 调研目录不进 git, 但索引文件进(便于 Frank 和 AI 协作)

## 数据/政策/事件标注规范

任何写到书稿里的事实, 必须同时标:

- **截至日期** (YYYY-MM-DD) —— 何时数据/政策/事件的有效性
- **来源 URL + 媒体** —— 一手 > 权威转述 > 二手报道
- **置信度** —— 已确认 / 多源一致 / 待确认 / 单一来源

参考 `.data-source-index.md` 已建立的锚点。

## Frank 的工作偏好(摘要, 全文见 Mavis MEMORY.md)

- **沟通**: 直接、省字、可以开点玩笑, 不要客套
- **audit 报告**: 纯观察 + 缺口, **不写"建议"段**(下游有 synthesis 任务单独做)
- **commit 流程**: OAuth token 限制, 不能 `git add .`, 显式列文件; 不动 `.github/workflows/`
- **OAuth 推不上的文件**: Frank 自己 commit
- **不要问"你该做 X 吗?"**: 看到错的、过时的、坏的, 直接修, 写报告

## 编辑规范

- 章内文件: `00_章节导读.md` → `01_*.md` 起 → `90_本章核心要点.md` → `91_本章决策清单.md` → `99_本章参考文献.md`
- 脚注引用: 正文里 `[^chXX-N]`, 定义在 `99_本章参考文献.md`
- 修改优先: 段落级补丁 → 整节重写 → 整章重写(慎用)

## 提交前自检

每次写完补丁, 跑这五步:

1. `git status` —— 没动 working dir 里**不该动**的文件
2. `git diff` —— 改动范围符合本任务 scope
3. 行号引用 —— `[^chXX-N]` 都在 `99_本章参考文献.md` 有定义
4. 时间锚点 —— 新加的事实标了"截至 YYYY-MM-DD"
5. Frank 审 —— 提交前让他过目(除非他明确授权 auto)

## 已知陷阱(写在这里防重复踩)

- **不要改书稿到 working tree dirty 后再 commit 含 workflow 文件** —— OAuth 没 workflow scope, push 会被拒
- **不要用 `git add .` 或 `-A`** —— Frank 的 untracked 文件会被一起 commit 进去
- **sub-agent 派活前必带 4 条不约束** —— 不 restore / 不 commit / 不 add 新功能 / 不续做历史 commit 的工作
- **OpenAI/Anthropic/Google 在 open weights 上的缺席不是"还没签"** —— 7-24 声明是已签字 vs 拒绝签字的明牌, 别搞混
