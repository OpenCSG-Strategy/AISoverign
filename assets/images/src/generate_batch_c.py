"""Batch c: 4 张图 fig5-1 / fig5-2 / fig7-2 / fig8-2。复用 generate_v01.py 风格基线。"""
from pathlib import Path

OUT = Path(__file__).parent.parent
FONT = "Noto Sans CJK SC, PingFang SC, sans-serif"

# ---- 复用基线辅助函数(与 generate_v01.py / generate_batch_b.py 同源) ----

def svg(name, title, body, width=1600, height=900):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>{title}</title><desc>《AI主权》原创信息图，v0.1，2026-08-03。纸书黑白和彩色电子版均可使用。</desc>
<rect width="100%" height="100%" fill="#fbfaf7"/>
<style>text{{font-family:{FONT};fill:#1f2933}} .title{{font-size:34px;font-weight:700}} .label{{font-size:23px;font-weight:700}} .small{{font-size:18px}} .tiny{{font-size:15px}} .box{{stroke:#34495e;stroke-width:3;rx:18}} .muted{{fill:#f0eee8}} .accent{{fill:#dbeafe}} .warm{{fill:#fef3c7}} .green{{fill:#dcfce7}} .line{{stroke:#506273;stroke-width:4;fill:none}} .dash{{stroke:#8795a1;stroke-width:3;stroke-dasharray:12 10;fill:none}}</style>
{body}
<text x="60" y="{height-35}" class="tiny">原创信息图 · v0.1 · 2026-08-03 · 适配单色印刷</text></svg>'''
    p = OUT / name
    p.write_text(content, encoding="utf-8")

def text(x, y, s, cls="small", anchor="middle"):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{s}</text>'

def box(x, y, w, h, cls="muted", label="", sub=""):
    if h < 80:
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="box {cls}"/>{text(x+w/2, y+h/2+8, label, "small")}'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="box {cls}"/>{text(x+w/2, y+42, label, "label")}{text(x+w/2, y+78, sub, "small") if sub else ""}'

def arrow(x1, y1, x2, y2, label="", cls="line"):
    return f'<path d="M{x1},{y1} L{x2},{y2}" class="{cls}" marker-end="url(#arrow)"/>{text((x1+x2)/2, (y1+y2)/2-12, label, "tiny") if label else ""}'

def defs():
    return '<defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,0 L12,6 L0,12 z" fill="#506273"/></marker></defs>'

def cell(x, y, w, h, cls, lines, anchor="middle", line_h=22, text_cls="small"):
    """表格单元:圆角矩形 + 多行居中文字。"""
    n = len(lines)
    pad_top = 8
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="box {cls}"/>'
    cx = x + w/2
    if anchor == "start":
        cx_text = x + 12
        first_y = y + 24
    else:
        cx_text = cx
        total = (n - 1) * line_h
        first_y = y + (h - total) / 2 + 16
    spans = "".join(
        f'<tspan x="{cx_text}" dy="{line_h if i>0 else 0}">{l}</tspan>'
        for i, l in enumerate(lines)
    )
    txt = f'<text x="{cx_text}" y="{first_y}" class="{text_cls}" text-anchor="{anchor}">{spans}</text>'
    return rect + txt

# ============================================================
# 图 5-1:企业控制面(3 层堆叠)
# ============================================================
def fig51():
    b = defs()
    b += text(60, 65, "图5-1　企业的AI能力网络", "title", "start")
    b += text(800, 115, "业务任务交给一张能力网络;中间层是企业可治理的边界,下层是随时可替换的资源", "label")

    # ---- 顶层:3 个业务任务示例(实线) ----
    # 3 boxes 380 wide, 110 tall; 3*380+2*30=1200, 两侧 margin 200
    top_boxes = [
        (200, "退款审批", "跨客服·模型·支付"),
        (610, "供应商尽调", "跨检索·模型·批准"),
        (1020, "合同建议", "跨知识·模型·人工"),
    ]
    for x, l, s in top_boxes:
        b += box(x, 180, 380, 110, "accent", l, s)
    b += text(390, 165, "业务任务", "small", "middle")
    b += text(800, 165, "(3 个常见示例)", "tiny", "middle")

    # ---- 中层:6 项治理能力(实线,核心区) ----
    # 6 boxes 220 wide, 140 tall; 6*220+5*30=1470, 两侧 margin 65
    mid_boxes = [
        (65,   "身份", "谁可以发起"),
        (315,  "策略", "什么条件下允许"),
        (565,  "评测", "结果是否合格"),
        (815,  "路由", "任务交给谁"),
        (1065, "凭证", "发生了什么"),
        (1315, "成本", "用了多少资源"),
    ]
    for x, l, s in mid_boxes:
        b += box(x, 410, 220, 140, "muted", l, s)
    b += text(800, 395, "能力 / 治理面", "label", "middle")

    # ---- 顶层 → 中层:3 条实线(业务任务落到治理面) ----
    # 退款审批(390) → 策略(425); 供应商尽调(800) → 路由(925); 合同建议(1210) → 凭证(1175)
    b += '<path d="M390,290 L425,410" class="line" marker-end="url(#arrow)"/>'
    b += '<path d="M800,290 L925,410" class="line" marker-end="url(#arrow)"/>'
    b += '<path d="M1210,290 L1175,410" class="line" marker-end="url(#arrow)"/>'
    b += text(380, 360, "落地", "tiny", "middle")
    b += text(865, 360, "落地", "tiny", "middle")
    b += text(1190, 360, "落地", "tiny", "middle")

    # ---- 中层 → 底层:6 条虚线(治理面调用可替换资源) ----
    # 6 middle box bottom centers → 4 bottom box top centers
    # 身份(175)→模型(245); 策略(425)→算力(615); 评测(675)→算力(615)
    # 路由(925)→数据(985); 凭证(1175)→工具(1355); 成本(1425)→工具(1355)
    pairs = [
        (175, 245), (425, 615), (675, 615),
        (925, 985), (1175, 1355), (1425, 1355),
    ]
    for mc, tc in pairs:
        b += f'<path d="M{mc},550 L{tc},690" class="dash" marker-end="url(#arrow)"/>'

    # ---- 底层:4 个可替换资源(虚线描边) ----
    # 4 boxes 330 wide, 140 tall; 4*330+3*40=1440, 两侧 margin 80
    bottom_boxes = [
        (80,   "模型", "通用·专业·开源"),
        (450,  "算力", "云·本地·边缘"),
        (820,  "数据", "内部·外部·检索"),
        (1190, "工具", "API·代码·人工"),
    ]
    for x, l, s in bottom_boxes:
        # 虚线描边表示"可替换"
        b += f'<rect x="{x}" y="690" width="330" height="140" fill="#f0eee8" stroke="#8795a1" stroke-width="3" stroke-dasharray="12 10" rx="18"/>'
        b += text(x+165, 690+42, l, "label")
        b += text(x+165, 690+78, s, "small")
    b += text(800, 675, "资源层  ·  随时可替换", "label", "middle")

    # ---- 底部小结 ----
    b += text(800, 855, "实线 = 治理边界稳定保留 / 虚线 = 资源层可替换 / 治理面不绑死任何一类资源", "small", "middle")

    svg("fig5-1_enterprise-control-plane.svg", "图5-1 企业控制面", b)


# ============================================================
# 图 5-2:执行凭证剖面图
# ============================================================
def fig52():
    b = defs()
    b += text(60, 65, "图5-2　执行凭证:让一次任务可以被复盘", "title", "start")
    b += text(800, 115, "凭证不是把全部对话永久复制,而是按风险留下足够回答现实问题的字段", "label")

    # ---- 左侧:大卡片"执行凭证" ----
    # x=60, y=180, w=900, h=580
    b += '<rect x="60" y="180" width="900" height="580" class="box accent" rx="18"/>'
    b += text(510, 218, "执行凭证", "label")
    b += text(510, 248, "一次任务的批次记录  ·  按风险取舍字段", "small")

    # 9 个字段 3x3 网格,内部间距 20
    # 内部可用区: w=820, h=480
    # 3 列: 260 宽 + 20 间距 * 2 = 820
    # 3 行: 140 顶 + 20 间距 * 2 + 底 60 = 480 (实际 row 140)
    # header 60 高: y=260-320, then rows y=320, 480, 640
    cells = [
        (120, 320, "任务 ID", "标识 · 发起人 · 目的"),
        (400, 320, "版本", "计划 · 模型 · 知识版本"),
        (680, 320, "来源", "输入资料 · 摘要 · 受控标识"),
        (120, 480, "权限", "谁授权 · 范围 · 期限"),
        (400, 480, "批准", "人工身份 · 时间 · 条件"),
        (680, 480, "工具调用", "参数范围 · 状态 · 重试"),
        (120, 640, "外部结果", "对账编号 · 影响对象"),
        (400, 640, "失败", "降级路径 · 退出原因"),
        (680, 640, "补救", "撤销 · 回滚 · 通知"),
    ]
    for x, y, l, s in cells:
        b += f'<rect x="{x}" y="{y}" width="260" height="140" class="box muted" rx="18"/>'
        b += text(x+130, y+45, l, "label")
        b += text(x+130, y+82, s, "small")
        b += text(x+130, y+115, "保存", "tiny")

    # ---- 右侧:三类内容(已保存 / 可选 / 不保存) ----
    # x=990, y=180, w=550, h=580
    # 三段
    rx, rw = 990, 550
    # 段1:已保存 (绿色)
    b += '<rect x="990" y="180" width="550" height="190" class="box green" rx="18"/>'
    b += text(1005, 215, "已保存", "label", "start")
    b += text(1005, 244, "9 个核心字段,默认全留", "small", "start")
    saved = ["任务 ID / 版本 / 计划", "来源(摘要+受控标识)", "权限 / 批准 / 工具调用", "外部结果 / 失败 / 补救"]
    for i, s in enumerate(saved):
        b += text(1005, 285 + i*22, "·  " + s, "small", "start")

    # 段2:可选 (暖色)
    b += '<rect x="990" y="390" width="550" height="120" class="box warm" rx="18"/>'
    b += text(1005, 425, "可选", "label", "start")
    b += text(1005, 454, "取决于风险等级与合规要求", "small", "start")
    optional = ["·  记忆点 / 上下文节选", "·  关键判断的对话摘要"]
    for i, s in enumerate(optional):
        b += text(1005, 485 + i*22, s, "small", "start")

    # 段3:不保存 (虚线描边)
    b += '<rect x="990" y="530" width="550" height="230" fill="#fbfaf7" stroke="#b91c1c" stroke-width="3" stroke-dasharray="10 6" rx="18"/>'
    b += text(1005, 565, "不保存", "label", "start")
    b += text(1005, 594, "默认丢弃  ·  避免新的敏感数据库", "small", "start")
    notsaved = [
        "·  完整提示词(原文)",
        "·  客户原始材料 / 个人敏感字段",
        "·  中间推理 / 完整思维轨迹",
        "·  未触发的备选方案细节",
    ]
    for i, s in enumerate(notsaved):
        b += text(1005, 625 + i*22, s, "small", "start")

    # ---- 底部小结 ----
    b += text(800, 805, "凭证 ≠ 免责文件:它记录事件,不能替代对输入事实、模型结论与公平性的独立判断", "small", "middle")
    b += text(800, 838, "思维轨迹 = 不保存  ·  记忆点 = 可选  ·  外部结果 = 保存", "small", "middle")

    svg("fig5-2_execution-credential.svg", "图5-2 执行凭证", b)


# ============================================================
# 图 7-2:宜昌城市运行架构(6 节点流水线 + 飞轮回流)
# ============================================================
def fig62():
    b = defs()
    b += text(60, 65, "图7-2　宜昌:一座城市怎样从资源投入走向能力反哺", "title", "start")
    # 利益关系披露条(warm 背景)
    b += '<rect x="60" y="100" width="1480" height="38" fill="#fef3c7" stroke="#8795a1" stroke-width="2" rx="10"/>'
    b += text(80, 126, "⚠  作者所在机构参与当地相关平台建设;案例数据出版前复核  ·  省级场景清单利用率等数字仍来自申报材料,不作效果结论", "small", "start")

    b += text(800, 168, "资源 → 共同底座 → 控制面 → 场景任务 → 公共责任 → 能力反哺", "label", "middle")
    b += text(800, 200, "成熟度不是总分;防止\"某一部件存在\"替整套系统领取结论", "small", "middle")

    # ---- 6 节点水平流水线 ----
    # y=240-380 (140 tall)
    # 6 boxes 220 wide, 5 gaps of 24: 6*220+5*24=1440, 两侧 margin 80
    nodes = [
        (80,   "资源",       "算力·电力·网络·人才"),
        (324,  "共同底座",   "纳管·调度·计量·标准"),
        (568,  "控制面",     "身份·路由·AgenticOps"),
        (812,  "场景任务",   "政务·制造·农业·科研"),
        (1056, "公共责任",   "授权·分区·申诉·监督"),
        (1300, "能力反哺",   "技术·产业·公共"),
    ]
    for x, l, s in nodes:
        b += box(x, 240, 220, 140, "muted", l, s)

    # 节点间实线箭头
    for i in range(5):
        x1 = 80 + i*244 + 220  # right edge of current
        x2 = 80 + (i+1)*244 - 8  # left edge of next minus marker
        b += f'<path d="M{x1},310 L{x2},310" class="line" marker-end="url(#arrow)"/>'

    # ---- 5 种证据状态标签(每个节点下方 1 个) ----
    # 5 状态: 规划 / 建设 / 上线 / 运行 / 独立成效
    # 6 节点分配: 资源=建设, 共同底座=建设, 控制面=上线, 场景任务=运行, 公共责任=规划, 能力反哺=独立成效
    states = [
        (190,  "建设"),
        (434,  "建设"),
        (678,  "上线"),
        (922,  "运行"),
        (1166, "规划"),
        (1410, "独立成效"),
    ]
    for cx, st in states:
        b += '<rect x="' + str(cx-46) + '" y="395" width="92" height="34" fill="#fbfaf7" stroke="#8795a1" stroke-width="2" stroke-dasharray="6 4" rx="10"/>'
        b += text(cx, 418, "证据状态:" + st, "small")

    # ---- 飞轮回流(从能力反哺弯回资源) ----
    # 从 (1410, 380) 即能力反哺底部 出发, 弯到 (190, 380) 即资源底部
    b += '<path d="M1410,380 C1500,560 1500,720 800,720 C100,720 100,560 190,380" class="dash" marker-end="url(#arrow)"/>'
    b += text(800, 690, "能力反哺 → 资源(沉淀回流,飞轮闭合)", "label", "middle")
    b += text(800, 718, "持续回流 ≠ 一次性招商", "tiny", "middle")

    # ---- 右侧证据状态图例(简化) ----
    # 已藏在节点下方,这里加一个简短说明在底部
    b += box(80, 770, 480, 70, "muted", "判断标准", "飞轮是否持续运转 / 资产是否沉淀 / 退出后能否继续")
    b += box(580, 770, 480, 70, "warm", "成熟度差异", "同一项目,数据中心已运行,模型平台刚上线,孵化仍在规划")
    b += box(1080, 770, 460, 70, "green", "真正问题", "不是建成多少 P 算力,而是能否把运行变成资产、产业与人才")

    svg("fig7-2_yichang-architecture.svg", "图7-2 宜昌城市运行架构", b)


# ============================================================
# 图 8-2:六项可验证预测(6×3 矩阵)
# ============================================================
def fig72():
    b = defs()
    b += text(60, 65, "图8-2　到二〇三五年：六项可验证预测", "title", "start")
    b += text(800, 115, "每项判断都列出依据、观察指标和反证条件", "label")

    # ---- 表头 ----
    # y=170, h=50
    # 4 列:判断 / 驱动力 / 可观测指标 / 反证条件
    col_x = [60, 430, 800, 1170]   # left edges
    col_w = [360, 360, 360, 370]
    col_label = ["六个判断", "驱动力 ·  为什么可能成立", "可观测指标 ·  看什么能确认", "反证条件 ·  看到什么就推翻"]

    for i, (x, w, l) in enumerate(zip(col_x, col_w, col_label)):
        cls = "warm" if i == 0 else "muted"
        b += f'<rect x="{x}" y="170" width="{w}" height="50" class="box {cls}"/>'
        b += text(x + w/2, 202, l, "small")

    # ---- 6 行数据 ----
    # row 起始 y=232, 每行 96 高, 5 gap 4: 6*96+5*4=596
    row_h = 96
    row_gap = 4
    row_y0 = 232
    rows = [
        (["智能更便宜", "可信行动更昂贵"],
         ["生成单价下降", "验证与恢复成本上升"],
         ["端到端任务成本", "验证成本占比"],
         ["验证成本接近于零", "且广泛应用未出现"]),
        (["模型同时向更大", "和更小发展"],
         ["大模型探索前沿", "小模型承接成熟能力"],
         ["能力能否压缩", "迁移后能否维护"],
         ["关键能力长期", "无法压缩或复现"]),
        (["Agent进入", "生产关系"],
         ["持续身份与预算", "跨Agent委托链"],
         ["持续任务数量", "授权与再委托路径"],
         ["长期只能完成", "短时低风险任务"]),
        (["企业最小有效", "规模下降"],
         ["搜索、协调和执行", "部分成本下降"],
         ["小团队存活率", "生产率与创新质量"],
         ["关键成本仍须", "大型组织承担"]),
        (["主权从系统位置", "转向决定权归属"],
         ["任务跨云跨模型", "学习资产可迁移"],
         ["谁路由、签发身份", "谁停止与取回反馈"],
         ["本地部署仍受", "单一外部入口控制"]),
        (["AI能力形成", "多个中心"],
         ["算力、能源、模型", "协议与治理分散"],
         ["关键能力是否仍", "分布在不同节点"],
         ["各项长期收敛到", "同一不可替代中心"]),
    ]
    for i, (judgment, driver, obs, ref) in enumerate(rows):
        y = row_y0 + i * (row_h + row_gap)
        # 判断列(2 行短句)
        b += cell(col_x[0], y, col_w[0], row_h, "warm", judgment, anchor="middle", line_h=28)
        # 驱动力 / 可观测 / 反证
        b += cell(col_x[1], y, col_w[1], row_h, "muted", driver, line_h=21, text_cls="tiny")
        b += cell(col_x[2], y, col_w[2], row_h, "muted", obs, line_h=21, text_cls="tiny")
        b += cell(col_x[3], y, col_w[3], row_h, "muted", ref, line_h=21, text_cls="tiny")

    # ---- 底部小结 ----
    b += text(800, 855, "这些判断可以分别验证；出现反证时，应当修改或放弃", "small", "middle")

    svg("fig8-2_2035-forecasts.svg", "图8-2 六个可被未来检验的判断", b)


# ---- 跑 ----
for f in (fig51, fig52, fig62, fig72):
    f()
    print("done:", f.__name__)
