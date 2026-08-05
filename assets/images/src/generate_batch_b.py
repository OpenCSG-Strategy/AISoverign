"""Batch b: 4 张图 fig2-3 / fig3-2 / fig4-1 / fig4-2。复用 generate_v01.py 风格基线。"""
from pathlib import Path

OUT = Path(__file__).parent.parent
FONT = "Noto Sans CJK SC, PingFang SC, sans-serif"

# ---- 复用基线辅助函数(与 generate_v01.py 同源) ----

def svg(name, title, body, width=1600, height=900):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>{title}</title><desc>《AI主权》原创信息图，v0.1，2026-08-03。纸书黑白和彩色电子版均可使用。</desc>
<rect width="100%" height="100%" fill="#fbfaf7"/>
<style>text{{font-family:{FONT};fill:#1f2933}} .title{{font-size:34px;font-weight:700}} .label{{font-size:23px;font-weight:700}} .small{{font-size:18px}} .tiny{{font-size:15px}} .box{{stroke:#34495e;stroke-width:3;rx:18}} .muted{{fill:#f0eee8}} .accent{{fill:#dbeafe}} .warm{{fill:#fef3c7}} .green{{fill:#dcfce7}} .line{{stroke:#506273;stroke-width:4;fill:none}} .dash{{stroke:#8795a1;stroke-width:3;stroke-dasharray:12 10;fill:none}} .redline{{stroke:#b91c1c;stroke-width:4;stroke-dasharray:10 8;fill:none}}</style>
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

# ============================================================
# 图 2-3:四个层级,一条责任链(嵌套方框)
# ============================================================
def fig23():
    b = defs()
    b += text(60, 65, "图2-3　四个层级,一条责任链", "title", "start")
    b += text(800, 115, "责任向外传递,选择与救济向内提供;四层嵌套,不能互相取代", "label")
    # 4 层嵌套方框(从外到内画)
    # 政府/国家 600,130, 1200,640
    # 企业     660,180, 1080,540
    # 组织     720,230,  960,440
    # 个人     780,280,  840,340
    cx, cy = 800, 450
    b += '<rect x="240" y="160" width="1120" height="580" class="box warm" rx="24"/>'
    b += text(800, 195, "政府 / 国家  ·  公共规则与长期基础设施", "label")
    b += '<rect x="320" y="220" width="960" height="460" class="box accent" rx="22"/>'
    b += text(800, 253, "企业  ·  商业生产者与系统运营", "label")
    b += '<rect x="400" y="280" width="800" height="340" class="box green" rx="20"/>'
    b += text(800, 311, "组织单元  ·  部门数据隔离 / 模型自治 / 有限协同", "label")
    b += '<rect x="480" y="340" width="640" height="220" class="box muted" rx="18"/>'
    b += text(800, 371, "个人  ·  记忆 / 表达 / 身份 / 职业能力", "label")
    # 中心:一个 AI 任务节点
    b += '<rect x="700" y="430" width="200" height="80" class="box" fill="#1f4e79" stroke="#1f4e79" rx="14"/>'
    b += text(800, 470, "一次 AI 任务", "label", "middle")
    b += text(800, 492, "四层共同面对的对象", "tiny", "middle")
    # 责任方向(向外的箭头,从内向外,沿左上方走)
    b += '<path d="M700,440 L260,200" class="redline" marker-end="url(#arrow)"/>'
    b += text(420, 165, "责任外推(向外)", "small", "middle")
    # 选择与救济方向(向内的箭头,从外向内,沿右下方走)
    b += '<path d="M1340,650 L900,510" class="line" marker-end="url(#arrow)"/>'
    b += text(1180, 730, "选择 · 救济(向内)", "small", "middle")
    # 4 句话总结
    b += box(60, 760, 360, 100, "muted", "个人保留", "自我决定与撤回")
    b += box(440, 760, 360, 100, "green", "组织连接", "部门自治与有限协同")
    b += box(820, 760, 360, 100, "accent", "企业建设", "可持续运行能力")
    b += box(1200, 760, 360, 100, "warm", "国家维护", "公共规则与基础设施")
    svg("fig2-3_four-levels-responsibility.svg", "图2-3 四个层级责任链", b)


# ============================================================
# 图 3-2:一套可搬走的个人智能栈(分层栈)
# ============================================================
def fig32():
    b = defs()
    b += text(60, 65, "图3-2　一套可搬走的个人智能栈", "title", "start")
    b += text(800, 115, "助手可以换,抽屉和笔记本还在;分层让每层都能被独立迁移", "label")
    # 5 层堆叠栈(从顶到底:界面 → 模型 → 工具 → 身份 → 数据/记忆)
    layers = [
        ("界面 / 行动权限", "可拆卸,易更换", "accent"),
        ("模型层", "可替换的推理能力", "muted"),
        ("工具 / 自动化", "可调用的外部动作", "muted"),
        ("身份 / 凭据", "谁能用什么", "warm"),
        ("数据 / 记忆", "原始资产与长期偏好", "green"),
    ]
    # 栈主体居左:x=240..960, y=200..760
    sx, sy, sw, sh = 240, 200, 720, 560
    h_each = 105
    gap = 7
    for i, (l, s, cls) in enumerate(layers):
        y = sy + i * (h_each + gap)
        b += box(sx, y, sw, h_each, cls, l, s)
    # 右侧"个人" 圆角节点(右下,作为主)
    b += '<rect x="1060" y="640" width="200" height="120" class="box" fill="#1f4e79" stroke="#1f4e79" rx="18"/>'
    b += text(1160, 695, "个人", "label", "middle")
    b += text(1160, 725, "谁能换、谁能搬", "tiny", "middle")
    # 4 个"导出"箭头,从栈底/侧出来,指向"个人"
    # 记忆 / 配置 / 凭据 / 记录
    b += '<path d="M960,517 L1060,680" class="line" marker-end="url(#arrow)"/>'
    b += text(990, 590, "记忆", "tiny")
    b += '<path d="M960,372 L1080,650" class="line" marker-end="url(#arrow)"/>'
    b += text(1010, 510, "配置", "tiny")
    b += '<path d="M960,300 L1090,640" class="line" marker-end="url(#arrow)"/>'
    b += text(1015, 470, "凭据", "tiny")
    b += '<path d="M960,228 L1100,630" class="line" marker-end="url(#arrow)"/>'
    b += text(1015, 430, "记录", "tiny")
    # 右上"可搬走"小标记
    b += box(1300, 200, 260, 60, "green", "导出自带", "")
    b += box(1300, 280, 260, 60, "muted", "云服务可承担计算", "只要你持有导出路径")
    # 1-2 个"不可带走"反例(虚线)
    b += '<rect x="1300" y="370" width="260" height="60" class="box" stroke="#8795a1" stroke-dasharray="6 4" fill="none" rx="14"/>'
    b += text(1430, 408, "专有私有云等级", "small", "middle")
    b += '<rect x="1300" y="445" width="260" height="60" class="box" stroke="#8795a1" stroke-dasharray="6 4" fill="none" rx="14"/>'
    b += text(1430, 483, "平台绑定的内部关联", "small", "middle")
    b += text(1430, 525, "(不可独立导出)", "tiny", "middle")
    # 顶部:可搬走 = 实线
    b += text(60, 800, "实线 = 通用格式 / 可独立持有;虚线 = 平台绑定 / 不可独立导出", "small", "start")
    svg("fig3-2_personal-stack.svg", "图3-2 个人智能栈", b)


# ============================================================
# 图 4-1:一项任务会跨过多个信任边界(泳道)
# ============================================================
def fig41():
    b = defs()
    b += text(60, 65, "图4-1　一项任务会跨过多个信任边界", "title", "start")
    b += text(800, 115, "学校用 AI 帮助分析作文,一次看似简单的批改已跨过五个边界", "label")
    # 5 个水平泳道:y 起点 180, 每行 110
    lanes = [
        ("成员(学生)", "muted"),
        ("组织(学校)", "green"),
        ("供应商(语言模型)", "accent"),
        ("供应商(内容安全)", "accent"),
        ("外部工具与门户", "warm"),
    ]
    lx0, ly0, lw, lh = 200, 180, 1340, 110
    gap_y = 8
    for i, (l, cls) in enumerate(lanes):
        y = ly0 + i * (lh + gap_y)
        b += f'<rect x="{lx0}" y="{y}" width="{lw}" height="{lh}" class="box {cls}" rx="14"/>'
        b += text(lx0 + 30, y + 45, l, "label", "start")
        b += text(lx0 + 30, y + 80, ("受托关系中" if i == 1 else ("数据流节点" if i in (2, 3) else ("行动渠道" if i == 4 else "原始与受影响方"))), "tiny", "start")
    # 4 阶段标签
    phases = ["数据", "权限", "推断", "责任"]
    for j, p in enumerate(phases):
        px = 380 + j * 290
        b += text(px, 165, p, "label", "middle")
    # 横向流(各泳道之间有数据 / 权限 / 推断 / 责任流)
    # 简化画法:在每个 phase 中心位置,画从成员到组织 / 组织到供应商 / 供应商到安全 / 安全到外部工具 的链
    # 4 段箭头,跨 4 段(从成员 → 组织,组织 → 模型,模型 → 内容安全,内容安全 → 外部工具/门户)
    # 第一段:数据
    b += '<path d="M540,290 L540,400" class="line" marker-end="url(#arrow)"/>'
    b += text(560, 350, "提交作文", "tiny", "start")
    # 权限
    b += '<path d="M830,400 L830,510" class="line" marker-end="url(#arrow)"/>'
    b += text(850, 460, "合同授权", "tiny", "start")
    # 推断
    b += '<path d="M1120,510 L1120,620" class="line" marker-end="url(#arrow)"/>'
    b += text(1140, 570, "风险标签", "tiny", "start")
    # 责任 / 反馈回流(从最底回到组织,然后到成员)
    b += '<path d="M1410,730 L1410,620" class="line" marker-end="url(#arrow)"/>'  # 反馈回到内容安全/学校
    b += text(1320, 690, "家长门户收到", "tiny", "end")
    b += '<path d="M1410,400 L1410,290" class="line" marker-end="url(#arrow)"/>'  # 教师把反馈给成员
    b += text(1430, 350, "教师反馈", "tiny", "start")
    # 框边界注
    b += text(800, 825, "每个节点只看见自己职责所需的视图;数据流 ≠ 责任流", "label")
    svg("fig4-1_trust-boundaries.svg", "图4-1 信任边界", b)


# ============================================================
# 图 4-2:一次批准不能覆盖整个生命周期(6 阶段流水线)
# ============================================================
def fig42():
    b = defs()
    b += text(60, 65, "图4-2　一次批准不能覆盖整个生命周期", "title", "start")
    b += text(800, 115, "采购时签字,只能证明当时的版本、用途与条件;变化之后需要持续治理", "label")
    # 6 阶段
    stages = [
        ("采购", "合同与披露", "accent"),
        ("上线", "灰度 / 影子", "accent"),
        ("变更", "重新评测", "warm"),
        ("监测", "漂移与成本", "warm"),
        ("事故", "隔离与补救", "warm"),
        ("退出", "证据与交接", "green"),
    ]
    x0, y0, w, h = 90, 380, 220, 130
    gap = 30
    for i, (l, s, cls) in enumerate(stages):
        x = x0 + i * (w + gap)
        b += box(x, y0, w, h, cls, l, s)
        # 4 个小标记(授权/通知/申诉/证据)
        # 阶段名下四个小圆点(实心/空心)
        b += text(x + 25, y0 + h + 50, "授权", "tiny", "middle")
        b += text(x + 80, y0 + h + 50, "通知", "tiny", "middle")
        b += text(x + 135, y0 + h + 50, "申诉", "tiny", "middle")
        b += text(x + 190, y0 + h + 50, "证据", "tiny", "middle")
        # 实心圆点表示"已要求";空心表示"未必有"
        # 第 1 阶段(采购):全部实心,代表一次批准覆盖到这里
        if i == 0:
            for dx in (25, 80, 135, 190):
                b += f'<circle cx="{x+dx}" cy="{y0+h+30}" r="8" fill="#1f4e79" stroke="#1f4e79"/>'
        else:
            for dx in (25, 80, 135, 190):
                b += f'<circle cx="{x+dx}" cy="{y0+h+30}" r="8" fill="none" stroke="#506273" stroke-width="3"/>'
        # 阶段间箭头
        if i < len(stages) - 1:
            nx = x + w + gap - 10
            b += f'<path d="M{x+w},{y0+h/2} L{nx},{y0+h/2}" class="line" marker-end="url(#arrow)"/>'
    # 顶部"一次批准覆盖到这里" 红色虚线(从左侧到第 1 阶段结束,即上线之前)
    arrow_end_x = x0 + (w + gap)  # 第 1 阶段(上线)之前
    b += f'<path d="M90,260 L{arrow_end_x-10},{y0-10}" class="redline" marker-end="url(#arrow)"/>'
    b += text(420, 230, "一次批准覆盖到这里(到上线之前)", "label", "start")
    b += text(420, 260, "(采购签字 = 一次性证明当时的版本与条件)", "tiny", "start")
    # 上方批注:之后阶段变化类型
    b += text(800, 165, "之后的变化会触发复核,而不是沿用旧签字", "label", "middle")
    # 底部:5 类变化(看得更多 / 想得更多 / 做得更多 / 影响更多 / 依赖更深)
    b += box(80, 720, 280, 80, "accent", "看得更多", "新增数据 / 扩大保留")
    b += box(380, 720, 280, 80, "warm", "想得更多", "从整理到预测 / 评价")
    b += box(680, 720, 280, 80, "green", "做得更多", "从建议到改变资格")
    b += box(980, 720, 280, 80, "muted", "影响更多", "试点扩到脆弱群体")
    b += box(1280, 720, 280, 80, "warm", "依赖更深", "人工流程消失")
    # 5 类变化与 6 阶段的关系提示
    b += text(800, 825, "这五类变化比“是否更换模型”更值得触发复核", "label", "middle")
    svg("fig4-2_lifecycle.svg", "图4-2 一次批准不能覆盖整个生命周期", b)


# ---- 跑 ----
for f in (fig23, fig32, fig41, fig42):
    f()
    print("done:", f.__name__)
