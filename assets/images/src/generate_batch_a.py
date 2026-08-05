from pathlib import Path

OUT = Path(__file__).parent.parent
FONT = "Noto Sans CJK SC, PingFang SC, sans-serif"

def svg(name, title, body, width=1600, height=900):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>{title}</title><desc>《AI主权》原创信息图，v0.1，2026-08-03。纸书黑白和彩色电子版均可使用。</desc>
<rect width="100%" height="100%" fill="#fbfaf7"/>
<style>text{{font-family:{FONT};fill:#1f2933}} .title{{font-size:34px;font-weight:700}} .label{{font-size:23px;font-weight:700}} .small{{font-size:18px}} .tiny{{font-size:15px}} .box{{stroke:#34495e;stroke-width:3;rx:18}} .muted{{fill:#f0eee8}} .accent{{fill:#dbeafe}} .warm{{fill:#fef3c7}} .green{{fill:#dcfce7}} .line{{stroke:#506273;stroke-width:4;fill:none}} .dash{{stroke:#8795a1;stroke-width:3;stroke-dasharray:12 10;fill:none}}</style>
{body}
<text x="60" y="{height-35}" class="tiny">原创信息图 · v0.1 · 2026-08-03 · 适配单色印刷</text></svg>'''
    p = OUT / name
    p.write_text(content, encoding="utf-8")

def text(x,y,s,cls="small",anchor="middle"):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{s}</text>'

def box(x,y,w,h,cls="muted",label="",sub=""):
    if h < 80:
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="box {cls}"/>{text(x+w/2,y+h/2+8,label,"small")}'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="box {cls}"/>{text(x+w/2,y+42,label,"label")}{text(x+w/2,y+78,sub,"small") if sub else ""}'

def arrow(x1,y1,x2,y2,label=""):
    return f'<path d="M{x1},{y1} L{x2},{y2}" class="line" marker-end="url(#arrow)"/>{text((x1+x2)/2,(y1+y2)/2-12,label,"tiny") if label else ""}'

def defs():
    return '<defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,0 L12,6 L0,12 z" fill="#506273"/></marker></defs>'


def figxu1():
    b = defs() + text(60, 65, "图序-1　能力扩散与控制集中同时发生", "title", "start")
    b += text(800, 118, "同一时代出现两个方向相反的运动；可治理委托是中间的接缝", "label")
    b += text(800, 158, "← 能力向外扩散　　　　　控制向关键节点集中 →", "small")
    # Left side: 能力扩散 (arrows point right)
    b += box(80, 220, 380, 130, "accent", "开放权重", "下载 · 检查 · 微调")
    b += box(80, 380, 380, 130, "muted", "蒸馏与量化", "大模型能力向小设备迁移")
    b += box(80, 540, 380, 130, "accent", "论文与代码", "方法进入公共知识")
    b += box(80, 700, 380, 120, "muted", "小模型与端侧", "MMLU 60% 最小模型已降至 38 亿参数")
    # Right side: 控制集中 (arrows point left)
    b += box(1140, 220, 380, 130, "warm", "先进芯片", "制造集中在少数代工厂")
    b += box(1140, 380, 380, 130, "warm", "数据中心与电力", "用电需求快速上升")
    b += box(1140, 540, 380, 130, "warm", "长期资本", "五大科技企业 2025 资本支出 > 4000 亿美元")
    b += box(1140, 700, 380, 120, "warm", "持续前沿创新", "关键训练能力持续集中")
    # Arrows from each side converging on center (end at rect left/right edges)
    for sy, ey in [(285, 380), (445, 470), (605, 560), (760, 680)]:
        b += f'<path d="M460,{sy} L700,{ey}" class="line" marker-end="url(#arrow)"/>'
    for sy, ey in [(285, 380), (445, 470), (605, 560), (760, 680)]:
        b += f'<path d="M1140,{sy} L900,{ey}" class="line" marker-end="url(#arrow)"/>'
    # Center: 可治理委托
    b += '<rect x="700" y="380" width="200" height="300" rx="22" fill="#1f4e79" stroke="#34495e" stroke-width="3"/>'
    b += text(800, 440, "可治理", "label")
    b += '<text x="800" y="478" fill="white" class="label" text-anchor="middle">委托</text>'
    b += '<text x="800" y="520" fill="white" class="tiny" text-anchor="middle">任务边界清楚</text>'
    b += '<text x="800" y="546" fill="white" class="tiny" text-anchor="middle">状态可见</text>'
    b += '<text x="800" y="572" fill="white" class="tiny" text-anchor="middle">授权可撤</text>'
    b += '<text x="800" y="598" fill="white" class="tiny" text-anchor="middle">结果可复盘</text>'
    b += '<text x="800" y="640" fill="#dbeafe" class="tiny" text-anchor="middle">扩散不等于控制权普及</text>'
    # Bottom takeaway
    b += text(800, 855, "判断标准：能力能否被选择、替换、迁移、审计、组合与演进", "label")
    svg("figxu-1_diffusion-vs-concentration.svg", "图序-1 能力扩散与控制集中", b)


def fig11():
    b = defs() + text(60, 65, "图1-1　一次回答，其实经过两条生产线", "title", "start")
    b += text(800, 118, "Prefill 读题 → KV Cache 工作台 → Decode 作答", "label")
    # Input cluster (left)
    b += box(60, 200, 280, 80, "muted", "提示词", "用户输入")
    b += box(60, 295, 280, 80, "muted", "历史对话", "上下文累积")
    b += box(60, 390, 280, 80, "muted", "检索材料", "RAG 结果")
    b += box(60, 485, 280, 80, "muted", "工具返回", "函数 / 设备")
    b += box(60, 600, 280, 80, "muted", "输入组合", "全部送入 Prefill")
    # arrows from inputs to Prefill
    for y in (240, 335, 430, 525, 640):
        b += f'<path d="M340,{y} L420,{y}" class="line" marker-end="url(#arrow)"/>'
    # Prefill block
    b += box(420, 200, 340, 480, "accent", "", "")
    b += text(590, 248, "Prefill", "label")
    b += text(590, 286, "读题阶段", "small")
    b += text(590, 340, "并 行 计 算", "small")
    b += text(590, 380, "受计算能力约束", "tiny")
    b += text(590, 408, "输入越长，首 Token", "tiny")
    b += text(590, 428, "出现得越慢", "tiny")
    b += text(590, 485, "→ 建立 KV Cache", "small")
    b += text(590, 520, "（供后续生成复用", "tiny")
    b += text(590, 540, "的中间状态）", "tiny")
    b += text(590, 605, "PagedAttention", "small")
    b += text(590, 635, "像操作系统那样分页", "tiny")
    b += text(590, 658, "vLLM 吞吐 2–4×", "small")
    # arrow to KV Cache strip
    b += f'<path d="M760,440 L820,440" class="line" marker-end="url(#arrow)"/>'
    # KV Cache working bench
    b += box(820, 200, 280, 480, "muted", "", "")
    b += text(960, 248, "KV Cache", "label")
    b += text(960, 286, "工作台", "small")
    # small cache cells (4 cols x 5 rows = 20 cells)
    for i in range(5):
        for j in range(4):
            x = 850 + j * 56
            y = 330 + i * 56
            b += f'<rect x="{x}" y="{y}" width="46" height="44" rx="6" fill="#fef3c7" stroke="#506273" stroke-width="2"/>'
    b += text(960, 660, "被 Decode 反复读取", "tiny")
    # arrow to Decode
    b += f'<path d="M1100,440 L1160,440" class="line" marker-end="url(#arrow)"/>'
    # Decode block
    b += box(1160, 200, 380, 480, "warm", "", "")
    b += text(1350, 248, "Decode", "label")
    b += text(1350, 286, "作答阶段", "small")
    b += text(1350, 340, "逐 Token 生成", "small")
    b += text(1350, 380, "受显存 / 带宽约束", "tiny")
    b += text(1350, 408, "后一个 Token 必须建立", "tiny")
    b += text(1350, 428, "在前一个之上", "tiny")
    b += text(1350, 485, "→ 输出 Token 流", "small")
    # token stream visualization
    for i in range(5):
        x = 1190 + i * 64
        b += f'<rect x="{x}" y="560" width="50" height="50" rx="8" fill="#dcfce7" stroke="#34495e" stroke-width="2"/>'
        b += text(x + 25, 592, f"T{i+1}", "tiny")
    b += text(1350, 660, "Token 间隔 = 生成节奏", "tiny")
    # 4 performance cards at bottom
    b += text(800, 720, "四种性能术语", "label")
    b += box(80, 740, 350, 80, "green", "首 Token 延迟", "反应是否快")
    b += box(450, 740, 350, 80, "green", "Token 间延迟", "回答是否流")
    b += box(820, 740, 350, 80, "green", "系统吞吐量", "单位时间产能")
    b += box(1190, 740, 350, 80, "green", "单用户速度", "个体实际体验")
    svg("fig1-1_prefill-decode.svg", "图1-1 Prefill 与 Decode", b)


def fig13():
    b = defs() + text(60, 65, "图1-3　开源打开的是哪一道门", "title", "start")
    b += text(800, 118, "门从窄到宽；每多开一层，既多获得一些，也仍缺一些", "label")
    # 4 horizontal layers stacked, color progression muted → accent → warm → green
    layers = [
        (200, "muted", "开放 API", "购买产出", "输出结果", "训练数据 · 权重 · 部署位置"),
        (340, "accent", "开放权重", "取得训练后的设备", "权重 · 微调权", "训练数据来源 · 复现材料"),
        (480, "warm", "开放模型", "查看权重 + 文档", "查看权 · 检查权", "完整数据说明 · 训练代码"),
        (620, "green", "开源 AI", "训练代码 + 数据 + 流程", "复现 · 改造 · 共同维护", "硬件 · 能源 · 人才 · 持续运维"),
    ]
    # header for two right columns
    b += text(960, 190, "获得", "label", "middle")
    b += text(1320, 190, "仍缺", "label", "middle")
    for y, cls, label, sub, gain, lacks in layers:
        b += box(60, y, 720, 110, cls, label, sub)
        b += text(960, y + 60, gain, "small", "middle")
        b += text(1320, y + 60, lacks, "small", "middle")
    # Arrow on the right showing openness increasing
    b += '<path d="M1540,260 L1540,670" class="line" marker-end="url(#arrow)"/>'
    b += text(1505, 460, "开放", "tiny", "middle")
    b += text(1505, 488, "程度", "tiny", "middle")
    # bottom note
    b += text(800, 770, "“可以下载”只是开放起点，不是终点", "label")
    b += text(800, 808, "依据 OSI Open Source AI Definition 1.0 与 Linux Foundation Model Openness Framework", "small")
    svg("fig1-3_open-source-doors.svg", "图1-3 开源四道门", b)


def fig22():
    b = defs() + text(60, 65, "图2-2　六种可以检验的能力", "title", "start")
    b += text(800, 118, "可治理委托 = 任务边界清楚 + 状态可见 + 授权可撤 + 结果可复盘", "label")
    import math
    cx, cy = 800, 510
    R = 300  # orbit radius
    nodes = [
        ("选择", "能否看见不同方案的成本、限制与风险", 90),
        ("替换", "条件变化后，另一套系统能否接手", 30),
        ("迁移", "带走的不只是文件，还有提示、评测、习惯", -30),
        ("演进", "五年后仍能控制，需要版本与维护", -90),
        ("组合", "不把所有问题都变成同一种生成问题", -150),
        ("审计", "证据在模型之外，并能沿链条回到原始材料", 150),
    ]
    # Center
    b += '<circle cx="800" cy="510" r="115" fill="#1f4e79" stroke="#34495e" stroke-width="3"/>'
    b += text(800, 498, "可治理", "label")
    b += '<text x="800" y="528" fill="white" class="label" text-anchor="middle">委托</text>'
    b += '<text x="800" y="558" fill="white" class="tiny" text-anchor="middle">任务 · 状态 · 授权</text>'
    for label, q, deg in nodes:
        rad = math.radians(deg)
        x = cx + R * math.cos(rad)
        y = cy - R * math.sin(rad)
        cls = "warm" if label in ("选择", "审计") else "muted"
        b += box(x - 130, y - 60, 260, 120, cls, label, q)
        # arrow from node to center
        ex = cx + 115 * math.cos(rad)
        ey = cy - 115 * math.sin(rad)
        sx = x - 130 * math.cos(rad)
        sy = y - 60 * math.sin(rad)
        b += f'<path d="M{sx},{sy} L{ex},{ey}" class="line" marker-end="url(#arrow)"/>'
    b += text(800, 870, "六种能力不会自动和谐；控制必须与影响相称", "label")
    svg("fig2-2_six-capabilities.svg", "图2-2 六种可以检验的能力", b)


for f in (figxu1, fig11, fig13, fig22):
    f()
    print(f"done: {f.__name__}")
