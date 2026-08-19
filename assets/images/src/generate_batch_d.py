"""Batch d: 第三部+结语缺的图（共 31 张）。复用 generate_v01.py / generate_batch_c.py 风格基线。"""
from pathlib import Path

OUT = Path(__file__).parent.parent
FONT = "Noto Sans CJK SC, PingFang SC, sans-serif"


def svg(name, title, body, width=1600, height=900):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>{title}</title><desc>《AI主权》原创信息图，v0.1，2026-08-17。纸书黑白和彩色电子版均可使用。</desc>
<rect width="100%" height="100%" fill="#fbfaf7"/>
<style>text{{font-family:{FONT};fill:#1f2933}} .title{{font-size:32px;font-weight:700}} .label{{font-size:22px;font-weight:700}} .small{{font-size:17px}} .tiny{{font-size:14px}} .box{{stroke:#34495e;stroke-width:3;rx:18}} .muted{{fill:#f0eee8}} .accent{{fill:#dbeafe}} .warm{{fill:#fef3c7}} .green{{fill:#dcfce7}} .pink{{fill:#fde2e2}} .line{{stroke:#506273;stroke-width:4;fill:none}} .dash{{stroke:#8795a1;stroke-width:3;stroke-dasharray:12 10;fill:none}}</style>
{body}
<text x="60" y="{height-35}" class="tiny">原创信息图 · v0.1 · 2026-08-17 · 适配单色印刷</text></svg>'''
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
    n = len(lines)
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="box {cls}"/>'
    if anchor == "start":
        cx_text = x + 12
        first_y = y + 24
    else:
        cx_text = x + w/2
        total = (n - 1) * line_h
        first_y = y + (h - total) / 2 + 16
    spans = "".join(
        f'<tspan x="{cx_text}" dy="{line_h if i>0 else 0}">{l}</tspan>'
        for i, l in enumerate(lines)
    )
    txt = f'<text x="{cx_text}" y="{first_y}" class="{text_cls}" text-anchor="{anchor}">{spans}</text>'
    return rect + txt


# ============================================================
# 第八章 4 张
# ============================================================

def fig8_12_1():
    """图8-12.1　四城起点 × 多元一体四层结构"""
    b = defs()
    b += text(60, 65, "图8-12.1　四城起点 × 多元一体四层结构", "title", "start")
    b += text(800, 115, "同一套方法在不同禀赋城市里从不同的门进入，最后补齐同一个循环", "label")

    # 上半：4 列起点卡（紧凑版）
    b += text(60, 170, "起点（4 城）", "label", "start")
    cities = [
        (60,  "宜昌", "绿色算力"),
        (430, "盐城", "新能源 + 场景"),
        (800, "重庆高新区", "制造业场景"),
        (1170,"深圳龙岗", "公共组织 + 合规"),
    ]
    for x, name, endow in cities:
        b += box(x, 200, 320, 90, "warm", name, endow)

    # 下半：4 层结构（不与上面卡冲突——下移）
    b += text(60, 320, "方法（多元一体四层）", "label", "start")
    layers = [
        (60, 350, "① 多元资源底座", "电力 · 网络 · 数据中心 · 异构算力", "muted"),
        (60, 480, "② 城市 AI 资产层", "数据集 · 模型 · 代码 · 评测 · Agent 版本", "accent"),
        (60, 610, "③ AgenticOps 控制", "身份 · 权限 · 任务路由 · 成本 · 证据 · 停止", "warm"),
        (60, 740, "④ 公共 + 产业服务", "政务 · 制造 · 科研 · 开发者 · 资本", "green"),
    ]
    for x, y, label, sub, cls in layers:
        b += box(x, y, 1480, 110, cls, label, sub)

    # 起点 → 第一层 的箭头
    for sx in [220, 590, 960, 1330]:
        b += f'<path d="M{sx},295 L{sx},345" class="dash" marker-end="url(#arrow)"/>'

    svg("fig8-12_four-cities-start.svg", "图8-12.1 四城起点 × 多元一体四层结构", b)


def fig8_12_2():
    """图8-12.2　盐城　绿电 → 算力 → 开发者"""
    b = defs()
    b += text(60, 65, "图8-12.2　盐城　绿电 → 算力 → 开发者", "title", "start")
    b += text(800, 115, "绿电变成算力只是物理转换；让开发者负担得起，才是经济转换", "label")

    # 3 列转化链
    stages = [
        (60, "绿电", "新能源发电", [">1500 万千瓦装机", "海上风电规模领先", "储能 + 调度配套"]),
        (430, "算力", "可变成本生产要素", ["就地变机时", "训练 + 推理", "价格可定向投放"]),
        (800, "开发者", "生产主体", "可可可可可"),
    ]
    # 第一列
    b += box(60, 180, 360, 100, "green", "绿电", "新能源装机")
    b += cell(60, 300, 360, 130, "muted", [">1500 万千瓦", "海上风电领先", "储能 + 调度配套"], line_h=24)

    # 第二列
    b += box(440, 180, 360, 100, "accent", "算力", "就地机时")
    b += cell(440, 300, 360, 130, "muted", ["物理转换", "训练 + 推理", "波动电源 → 储能熨平"], line_h=24)

    # 第三列
    b += box(820, 180, 360, 100, "warm", "开发者", "OPC 社区")
    b += cell(820, 300, 360, 130, "muted", ["赛事揭榜", "孵化空间承接", "签约团队沉淀"], line_h=24)

    # 横向箭头
    b += '<path d="M420,230 L440,230" class="line" marker-end="url(#arrow)"/>'
    b += '<path d="M800,230 L820,230" class="line" marker-end="url(#arrow)"/>'

    # 底部定价策略
    b += box(60, 480, 540, 100, "warm", "卖机时", "把绿电按市场价卖给外地客户 → 算力收入")
    b += box(620, 480, 540, 100, "green", "卖生态", "把低成本算力投给本地开发者 → 生态回流")
    b += text(610, 510, "vs", "label", "middle")

    # 三次回流
    b += box(60, 620, 1480, 130, "muted", "三次回流", "资源（算力 → 开发者门槛 ↓）→ 资产（任务沉淀本地）→ 价值（收入 + 税基）；缺中间一级即漏到补贴之外")
    b += box(60, 770, 1480, 80, "pink", "判断", "能源城市在 AI 时代不必只做上游供应商——前提是忍住不把这张牌按电价卖掉")

    svg("fig8-12_yancheng.svg", "图8-12.2 盐城 绿电 → 算力 → 开发者", b)


def fig8_12_3():
    """图8-12.3　重庆　权属三层 × 三次回流"""
    b = defs()
    b += text(60, 65, "图8-12.3　重庆　权属三层 × 三次回流", "title", "start")
    b += text(800, 115, "把资产权属写在机房建设之前，是把生态的主体层和公共责任层接口预先定义好", "label")

    # 左侧：权属三层
    rights = [
        (60, "原始数据", "归产生方", ["链主企业保留", "不经授权不上传", "可撤回"]),
        (60, "共有成果", "归联合方", ["联合实验室", "链主 + 模型方", "按合同分配"]),
        (60, "通用方法", "归公共", ["评测 / 适配器", "行业知识库", "可被本地复用"]),
    ]
    ys = [180, 380, 580]
    for y, (x, label, sub, lines) in zip(ys, rights):
        b += box(x, y, 480, 140, "warm", label, sub)
        b += cell(x+20, y+90, 440, 50, "muted", lines, anchor="start", line_h=20, text_cls="small")

    # 右侧：三次回流
    loops = [
        (1080, "资源回流", "公共投入降低", ["算力门槛 ↓", "数据 / 模型", "可以本地获取"]),
        (1080, "资产回流", "项目结束后留下", ["代码 / 模型适配", "评测 / 数据产品", "人才不流失"]),
        (1080, "价值回流", "产业 + 公共", ["新增产值留本地", "公共服务改进", "支持下一轮建设"]),
    ]
    ys2 = [180, 380, 580]
    for y, (x, label, sub, lines) in zip(ys2, loops):
        b += box(x, y, 460, 140, "green", label, sub)
        b += cell(x+20, y+90, 420, 50, "muted", lines, anchor="start", line_h=20, text_cls="small")

    # 中间箭头
    b += '<path d="M540,250 L1080,250" class="line" marker-end="url(#arrow)"/>'
    b += '<path d="M540,450 L1080,450" class="line" marker-end="url(#arrow)"/>'
    b += '<path d="M540,650 L1080,650" class="line" marker-end="url(#arrow)"/>'

    # 底部：3 个问题
    b += box(60, 770, 1480, 80, "pink", "3 个问题作为准入考试", "① 权属是否成文  ② 链主是否愿意开放  ③ 运营主体是否长久（5 年 / 10 年）")

    svg("fig8-12_chongqing.svg", "图8-12.3 重庆 权属三层 × 三次回流", b)


def fig8_12_4():
    """图8-12.4　龙岗　采购条款 → 替换能力"""
    b = defs()
    b += text(60, 65, "图8-12.4　龙岗　采购条款 → 替换能力", "title", "start")
    b += text(800, 115, "采购合同能写出替换供应商的能力，写不出被需要的能力", "label")

    # 上半：6 节点链条
    clauses = [
        (60, "① 交付物描述", "明确技术规格"),
        (320, "② 资产归属", "数据 / 模型 / 代码归委托方"),
        (580, "③ 数据边界", "原始数据不离开边界"),
        (840, "④ 替换条件", "供应商可被替换"),
        (1100, "⑤ 退出与移交", "有序结束合同"),
        (1360, "⑥ 公共受托责任", "受托方对公共负责"),
    ]
    for x, label, sub in clauses:
        b += box(x, 180, 240, 120, "muted", label, sub)

    for x in [300, 560, 820, 1080, 1340]:
        b += f'<path d="M{x},240 L{x+20},240" class="line" marker-end="url(#arrow)"/>'

    # 下半：三组检验
    b += text(60, 360, "三组检验", "label", "start")
    tests = [
        (60, "替换供应商", ["新供应商能接手", "资产 / 权限可读", "记录可双方面理解"]),
        (560, "资产回流", ["数据可导出", "代码可运行", "适配器 / 评测可维护"]),
        (1060, "价值回流", ["政务外有人用", "团队沉淀本地", "付费意愿真实"]),
    ]
    for x, label, lines in tests:
        b += box(x, 380, 480, 130, "accent", label, "3 个问题")
        b += cell(x+20, x+460, 440, 80, "muted", lines, anchor="start", line_h=20, text_cls="small")

    # 底部：证据边界
    b += box(60, 770, 1480, 80, "pink", "证据边界", "只采用可公开核查的政府文件与公开报道；项目材料（投资规模、收益测算、合作意向、供应商细节）不进入本书")

    svg("fig8-12_longgang.svg", "图8-12.4 龙岗 采购条款 → 替换能力", b)


# ============================================================
# 第十章 5 张
# ============================================================

def fig10_1():
    """图10-1　四种开放 × 长期均衡判断"""
    b = defs()
    b += text(60, 65, "图10-1　四种开放 × 长期均衡判断", "title", "start")
    b += text(800, 115, "把四道门映射到能力扩散 / 控制集中 / 可治理空间 三条曲线", "label")

    # 上半：4 列卡
    opens = [
        (60, "API 文档", "查看", ["只能调用", "看不到内部", "许可证几乎不影响"]),
        (430, "开放权重", "查看 + 运行", ["可下载", "可推理", "许可证决定再分发"]),
        (800, "开放训练材料", "查看 + 运行 + 部分修改", ["可继续训练", "数据仍是封闭", "许可证 + 来源要求"]),
        (1170, "完全开源", "查看 + 运行 + 修改 + 再分发 + 治理", ["完整重建", "OSI + 社区治理", "许可证可证明"]),
    ]
    for x, name, rights, lines in opens:
        b += box(x, 180, 320, 90, "accent", name, rights)
        b += cell(x, 290, 320, 90, "muted", lines, line_h=22)

    # 下半：3 条曲线
    b += text(60, 420, "三条曲线（开放→扩散 / 集中 / 可治理空间）", "label", "start")

    # 坐标轴
    b += '<line x1="80" y1="500" x2="1520" y2="500" class="dash"/>'  # 0 基线
    b += '<line x1="80" y1="480" x2="80" y2="780" class="line"/>'  # y 轴

    # 3 条线：能力扩散、控制集中、可治理空间
    b += '<path d="M150,720 C500,650 800,580 1100,500 C1300,460 1450,440 1520,430" stroke="#3b82f6" stroke-width="5" fill="none"/>'
    b += '<path d="M150,720 C400,600 600,520 800,490 C1000,470 1200,470 1400,490 C1450,495 1500,500 1520,505" stroke="#ef4444" stroke-width="5" fill="none"/>'
    b += '<path d="M150,760 C400,720 700,640 900,580 C1100,520 1300,500 1500,490" stroke="#10b981" stroke-width="5" fill="none"/>'

    b += text(1500, 425, "能力扩散 ↑", "small", "start")
    b += text(1500, 510, "控制集中", "small", "start")
    b += text(1500, 495, "可治理空间", "small", "start")

    # 4 列打点
    for x in [220, 590, 960, 1330]:
        b += f'<circle cx="{x}" cy="700" r="8" fill="#3b82f6"/>'
        b += f'<circle cx="{x}" cy="600" r="8" fill="#ef4444"/>'
        b += f'<circle cx="{x}" cy="680" r="8" fill="#10b981"/>'

    # 底部判断
    b += box(60, 800, 1480, 80, "pink", "判断", "可治理空间不会随开放自动出现——必须由治理能力撑起")

    svg("fig10-1_four-opens-vs-equilibrium.svg", "图10-1 四种开放 × 长期均衡判断", b)


def fig10_2():
    """图10-2　两次开放行动：产业政策与防御工具链"""
    b = defs()
    b += text(60, 65, "图10-2　两次开放行动：产业政策与防御工具链", "title", "start")
    b += text(800, 115, "7-24 声明与 7-27 Open Secure AI Alliance 性质不同，纯文字不利于分清", "label")

    # 左半：7-24 产业政策声明
    b += box(60, 180, 720, 80, "accent", "① 7-24 产业政策声明", "《开放权重与美国 AI 领导力》")
    b += cell(60, 280, 720, 140, "muted", [
        "25 家公司初始联署",
        "横跨模型/芯片/云/安全/VC/开放共同体",
        "主张扩大获取 · 减少锁定 · 控制数据",
        "厂商立场：免费 AI 有利于硬件",
        "推动方：英伟达 + 多家"], line_h=22)

    # 右半：7-27 Open Secure AI Alliance
    b += box(820, 180, 720, 80, "warm", "② 7-27 Open Secure AI Alliance", "防御工具链共同体")
    b += cell(820, 280, 720, 140, "muted", [
        "聚焦供应链安全与防御",
        "为开放模型提供扫描 / 签名 / 漏洞库",
        "社区厂商 + 评测机构",
        "与 7-24 声明不同：不是产业政策",
        "而是开放模型的安全运营"], line_h=22)

    # 底部区分
    b += box(60, 460, 1480, 130, "muted", "区别", "7-24 是产业站队（市场 + 能力层）；7-27 是安全运营（（市场 + 供应链）；两者共同点是同一波开放浪潮的不同侧面")

    # 中间箭头
    b += '<path d="M780,420 L820,420" class="line" marker-end="url(#arrow)"/>'

    # 底部：利益机制
    b += box(60, 620, 700, 200, "green", "能力层开放", "更多推理 → 更多 GPU / 网络 / 数据中心 / 推理软件市场 → 英伟达等基础设施")
    b += box(800, 620, 700, 200, "warm", "防御工具链", "开放模型增加 → 攻击面增加 → 扫描 / 签名 / 漏洞库 / 责任划分成为刚需")

    svg("fig10-2_two-opens.svg", "图10-2 两次开放行动", b)


def fig10_3():
    """图10-3　HF 智能体安全事件时间线"""
    b = defs()
    b += text(60, 65, "图10-3　HF 智能体安全事件时间线（2026-07-31）", "title", "start")
    b += text(800, 115, "攻击和取证都进入智能体时代", "label")

    # 左半：6 节点时间线（垂直）
    b += text(60, 200, "攻击路径", "label", "start")
    nodes = [
        (200, "恶意数据集", "进入平台"),
        (300, "远程代码加载", "执行触发"),
        (400, "模板注入", "工作节点代码执行"),
        (500, "凭据收集", "云 + 集群"),
        (600, "横向移动", "多个集群"),
        (700, "取证分析", "1.7 万条记录 · GLM-5.2 本地"),
    ]
    for y, label, sub in nodes:
        b += box(60, y, 400, 70, "warm", label, sub)
        if y < 700:
            b += f'<path d="M260,{y+70} L260,{y+90}" class="line" marker-end="url(#arrow)"/>'

    # 右半：因果链 4 步
    b += text(900, 200, "4 步放大", "label", "start")
    steps = [
        (200, "善意测试", "实验环境"),
        (350, "隔离缝隙", "评测 vs 真实"),
        (500, "智能体组合", "多模型 + 漏洞"),
        (650, "真实外部行动", "触及生产系统"),
    ]
    for y, label, sub in steps:
        b += box(900, y, 600, 80, "pink", label, sub)
        if y < 650:
            b += f'<path d="M1200,{y+80} L1200,{y+110}" class="line" marker-end="url(#arrow)"/>'

    # 底部证据边界
    b += box(60, 800, 1480, 80, "muted", "证据边界", "双方初步披露；OpenAI 完整技术报告待发布；无独立取证报告")

    svg("fig10-3_hf-incident.svg", "图10-3 HF 智能体安全事件时间线", b)


def fig10_4():
    """图10-4　开放供应链 5 项核验"""
    b = defs()
    b += text(60, 65, "图10-4　开放供应链 5 项核验", "title", "start")
    b += text(800, 115, "下载一个开放模型，接入的是一整条供应链", "label")

    # 5 列检查表
    checks = [
        (60, "① 发布者 + 许可证", "谁发布的 · 许可证是否允许 · 是否与场景一致"),
        (360, "② 哈希 + 版本固定", "固定 hash · 锁定版本 · 防止漂移"),
        (660, "③ 权重格式", "safetensors / gguf · 避免 Pickle 代码执行风险"),
        (960, "④ 隔离环境首加载", "沙箱 · 最小权限 · 监控"),
        (1260, "⑤ 来源 / 依赖 / 漏洞", "可追溯记录 · 漏洞库订阅 · 持续更新"),
    ]
    for x, label, sub in checks:
        b += box(x, 180, 280, 130, "accent", label, sub)

    # 评估不能只看模型
    b += box(60, 380, 1480, 130, "warm", "评估不能只看模型", "还要看现实中获取算力、工具和专业材料的门槛——一个用于教育和文本处理的模型，与能够帮助高风险生物或网络操作的系统，需要不同发布判断")

    # 与图3-9 作者身份链的链接
    b += box(60, 560, 1480, 100, "muted", "与图3-9 作者身份的链", "下载者继承原作者的版本与许可责任——和「作者身份」一样，下载动作产生不可回避的责任归属")

    # 5 项失败示例
    b += box(60, 700, 1480, 180, "pink", "5 项核验的典型失败",
             "① 许可证二义性被忽略　②  模型被无声升级　③  Pickle 反序列化触发代码执行　④  漏洞未及时订阅　⑤  下载凭证被中间人劫持")

    svg("fig10-4_supply-chain.svg", "图10-4 开放供应链 5 项核验", b)


def fig10_5():
    """图10-5　能力扩散 vs 控制集中"""
    b = defs()
    b += text(60, 65, "图10-5　能力扩散 vs 控制集中", "title", "start")
    b += text(800, 115, "开放会扩散能力，但不自动消除控制集中", "label")

    # 上半：能力扩散曲线（不画时间轴；只画"扩散"+"集中"两条曲线作为对照）
    b += text(60, 200, "能力扩散", "label", "start")
    b += '<line x1="80" y1="230" x2="1520" y2="230" class="dash"/>'
    b += '<path d="M150,400 C400,360 700,310 900,280 C1100,250 1300,220 1500,210" stroke="#3b82f6" stroke-width="5" fill="none"/>'
    b += text(1500, 200, "扩散 ↑", "small", "start")

    # 下半：控制集中曲线
    b += text(60, 520, "控制集中", "label", "start")
    b += '<line x1="80" y1="550" x2="1520" y2="550" class="dash"/>'
    b += '<path d="M150,720 C400,700 700,660 900,620 C1100,580 1300,560 1500,560" stroke="#ef4444" stroke-width="5" fill="none"/>'
    b += text(1500, 545, "集中 →", "small", "start")

    # 中间：3 个反证节点
    b += '<circle cx="450" cy="380" r="10" fill="#3b82f6"/>'
    b += '<circle cx="450" cy="700" r="10" fill="#ef4444"/>'
    b += text(450, 350, "蒸馏可能引发合同争议", "tiny", "middle")

    b += '<circle cx="900" cy="290" r="10" fill="#3b82f6"/>'
    b += '<circle cx="900" cy="630" r="10" fill="#ef4444"/>'
    b += text(900, 260, "算力门槛仍在", "tiny", "middle")

    b += '<circle cx="1300" cy="240" r="10" fill="#3b82f6"/>'
    b += '<circle cx="1300" cy="580" r="10" fill="#ef4444"/>'
    b += text(1300, 210, "治理标准未跟上", "tiny", "middle")

    # 三层长期并存（去掉"必要条件"断言）
    b += box(60, 770, 480, 110, "accent", "基础层", "开放权重 + 协议 + 评测 + 数据工具")
    b += box(560, 770, 480, 110, "warm", "公共品层", "严格开源 + 公共治理")
    b += box(1060, 770, 480, 110, "muted", "前沿服务", "封闭运行 + 责任保障")

    # 底部说明
    b += text(60, 700, "长期并存的两种力量——不互相消除", "small", "start")

    svg("fig10-5_diffusion-vs-control.svg", "图10-5 能力扩散 vs 控制集中", b)


# ============================================================
# 第九章 4 张
# ============================================================

def fig9_2():
    """图9-2　纵深防御 → 失败预算（第九章 2—3 节合并）"""
    b = defs()
    b += text(60, 65, "图9-2　纵深防御 → 失败预算", "title", "start")
    b += text(800, 115, "防线组合 + 失败预算——第六章同款精神，纵深版", "label")

    # 上半：防线清单
    b += text(60, 200, "纵深防线清单", "label", "start")
    defenses = [
        (60, "分区数据", "敏感数据分区"),
        (220, "最小权限", "只给必要权限"),
        (380, "关键行动确认", "高影响二次确认"),
        (540, "速率限制", "防止过载"),
        (700, "独立日志", "留痕可查"),
        (860, "版本回退", "可回到稳定版"),
        (1020, "备用服务", "主路失败的备用"),
        (1180, "人工流程", "关键环节人接手"),
        (1340, "清晰规则", "自动 + 人工边界"),
    ]
    for x, label, sub in defenses:
        b += box(x, 240, 140, 100, "accent", label, sub)

    # 中部：冲击 → 隔离 → 降级 → 恢复 → 学习
    b += text(60, 380, "冲击后顺序", "label", "start")
    flow = [
        (60, "① 正常", "正常运行"),
        (340, "② 冲击", "异常开始"),
        (620, "③ 隔离", "影响范围受控"),
        (900, "④ 降级运行", "低智能 + 核心可用"),
        (1180, "⑤ 恢复", "回到稳态"),
        (1460, "⑥ 学习", "沉淀改进"),
    ]
    for i, (x, label, sub) in enumerate(flow[:-1]):
        b += box(x, 420, 240, 100, "warm", label, sub)
        b += f'<path d="M{x+260},470 L{x+340},470" class="line" marker-end="url(#arrow)"/>'
    # 最后一个
    b += box(1460, 420, 140, 100, "green", flow[-1][1], flow[-1][2])

    # 服务能力曲线
    b += '<path d="M150,720 C400,700 700,650 900,600 C1100,580 1300,620 1500,710" stroke="#3b82f6" stroke-width="4" fill="none" stroke-dasharray="8 6"/>'
    b += text(800, 700, "服务能力（纵深组合下不会归零）", "small", "middle")

    # 共同原因检查
    b += box(60, 760, 720, 130, "muted", "共同原因检查", "云 · 网络 · 模型接口 · 身份 · 能源 · 密钥 · 数据 · 人员 · 制度权限")

    # 失败预算（去掉 MTTR/RTO/RPO 术语）
    b += box(800, 760, 740, 130, "warm", "失败预算（五项，不引术语）",
             "① 核心服务最长中断时间  ② 可承受最大数据丢失  ③ 降级授权人  ④ 备用服务范围  ⑤ 恢复后必须核对的行动")

    svg("fig9-2_defense-failure.svg", "图9-2 纵深防御 → 失败预算", b)


def fig9_3():
    """图9-3　审计证据到哪里，结论就停在哪里"""
    b = defs()
    b += text(60, 65, "图9-3　审计证据到哪里，结论就停在哪里", "title", "start")
    b += text(800, 115, "五类证据严格沿用表9-1；任何一类都不能单独推出「系统可信」", "label")

    # 5 类证据（来自表 9-1）
    evidences = [
        (60, "签名与来源", "制品完整性 / 来源关系"),
        (340, "建造文档", "过程有记录"),
        (620, "运行日志", "特定身份权限下的动作"),
        (900, "独立测试", "特定样本环境表现"),
        (1180, "事故与申诉", "现实中已失效的边界"),
    ]
    for x, label, sub in evidences:
        b += box(x, 200, 280, 130, "accent", label, sub)

    # 每张卡：能 / 不能
    b += text(60, 360, "支持证明", "label", "start")
    b += text(900, 360, "不能证明", "label", "start")

    pairs = [
        ("制品完整性", "发布者持续可信"),
        ("过程有记录", "行为普遍安全"),
        ("特定动作", "未记录动作存在"),
        ("特定样本", "其他场景均安全"),
        ("现实边界", "未发生风险不存在"),
    ]
    for i, (yes, no) in enumerate(pairs):
        y = 400 + i * 60
        b += cell(60, y, 800, 50, "green", [yes], line_h=20, text_cls="small")
        b += cell(900, y, 640, 50, "warm", [no], line_h=20, text_cls="small")

    # 底部：审计结论限定条件
    b += box(60, 760, 1480, 130, "muted", "审计结论必须限定", "版本 + 数据 + 任务 + 权限——任何一类证据超出这些边界即不可外推")

    svg("fig9-3_audit-boundaries.svg", "图9-3 审计证据边界", b)


def fig9_4():
    """图9-4　韧性 4 维度"""
    b = defs()
    b += text(60, 65, "图9-4　韧性 4 维度", "title", "start")
    b += text(800, 115, "事故后的韧性怎样被衡量——4 维雷达", "label")

    # 4 维雷达图
    cx, cy = 800, 460
    r = 280
    # 4 轴
    import math
    axes = ["检测速度", "隔离能力", "恢复时间", "学习沉淀"]
    for i, label in enumerate(axes):
        angle = math.radians(i * 90 - 90)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        b += f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" class="dash"/>'
        b += text(x, y - 10, label, "small", "middle")

    # 3 圈
    for rad in [r * 0.33, r * 0.66, r]:
        pts = []
        for i in range(4):
            angle = math.radians(i * 90 - 90)
            x = cx + rad * math.cos(angle)
            y = cy + rad * math.sin(angle)
            pts.append(f"{x},{y}")
        b += f'<polygon points="{" ".join(pts)}" fill="none" stroke="#8795a1" stroke-dasharray="4 4"/>'

    # 示例团队数据（0—10）：检测 7, 隔离 6, 恢复 4, 学习 8
    scores = [7, 6, 4, 8]
    pts = []
    for i, s in enumerate(scores):
        angle = math.radians(i * 90 - 90)
        rad = r * (s / 10)
        x = cx + rad * math.cos(angle)
        y = cy + rad * math.sin(angle)
        pts.append(f"{x},{y}")
    b += f'<polygon points="{" ".join(pts)}" fill="#dbeafe" stroke="#1f4e79" stroke-width="3"/>'

    # 中心
    b += f'<circle cx="{cx}" cy="{cy}" r="6" fill="#1f4e79"/>'

    # 与图9-3 关系
    b += box(60, 800, 1480, 80, "muted", "与图9-3 审计证据边界的关系", "韧性 4 维度是抽象评分；审计证据边界是结论限定——两者结合决定团队真正能「通过失败」的能力")

    svg("fig9-4-resilience.svg", "图9-4 韧性 4 维度", b)


def fig9_5():
    """图9-5　审计证据边界表"""
    b = defs()
    b += text(60, 65, "图9-5　审计证据边界表", "title", "start")
    b += text(800, 115, "审计能证明什么 / 不能证明什么——证据类型与结论边界", "label")

    # 表头
    headers = ["证据类型", "可证伪命题", "不可证伪命题"]
    col_x = [60, 480, 1020]
    col_w = [400, 520, 520]
    for x, w, h in zip(col_x, col_w, headers):
        b += box(x, 180, w, 50, "warm", h, "")

    # 5 行
    rows = [
        ("日志", "发生了什么（时间 · 身份 · 动作）", "为什么这样决策"),
        ("凭证", "授权链是否完整 · 谁批准", "批准背后的理由是否充分"),
        ("截图", "UI 显示的内容 · 时间点", "截图后的状态"),
        ("第三方报告", "系统在某条件下表现 X", "在其他条件下表现如何"),
        ("评测集", "在已知样本上表现 Y", "未见过的样本上表现"),
    ]
    for i, (evid, provable, notprovable) in enumerate(rows):
        y = 250 + i * 110
        cls = "accent"
        b += box(60, y, 400, 100, cls, evid, "")
        b += cell(480, y, 520, 100, "green", [p for p in [provable] if p], line_h=22, text_cls="small")
        b += cell(1020, y, 520, 100, "warm", [p for p in [notprovable] if p], line_h=22, text_cls="small")

    svg("fig9-5-audit-boundaries.svg", "图9-5 审计证据边界表", b)


# ============================================================
# 第十一章 12 张
# ============================================================

def fig11_2():
    """图11-2　数据空间 vs 联邦学习"""
    b = defs()
    b += text(60, 65, "图11-2　数据空间 vs 联邦学习", "title", "start")
    b += text(800, 115, "共享不必先交出 / 数据留在本地，模型汇集经验", "label")

    # 左半：数据空间
    b += box(60, 180, 720, 80, "accent", "数据空间", "共享不必先交出")
    b += box(60, 280, 720, 90, "muted", "基础设施", "目录 + 标识 + 接入")
    b += box(60, 380, 720, 90, "muted", "共享协议", "跨域授权 + 使用规则")
    b += box(60, 480, 720, 90, "muted", "数据集", "可被授权访问的版本")
    b += box(60, 580, 720, 90, "muted", "服务", "查询 · 计算 · 脱敏")

    # 右半：联邦学习
    b += box(820, 180, 720, 80, "warm", "联邦学习", "数据留在本地")
    b += box(820, 280, 720, 110, "muted", "本地训练", "原始数据不出域")
    b += box(820, 410, 720, 110, "muted", "参数上传", "仅模型 / 梯度")
    b += box(820, 540, 720, 110, "green", "全局聚合", "汇集经验")

    # 中间共同点（修正版）
    b += box(60, 720, 1480, 100, "muted", "共同点", "① 边界可表达 ② 授权可撤回 ③ 行动可追责")

    # 底部判断（修正版）
    b += box(60, 840, 1480, 40, "pink", "判断", "数据空间：数据不一定永远留在原处；联邦学习：原始病历等记录留在本地（解释性场景）")

    svg("fig11-2_data-space-vs-fl.svg", "图11-2 数据空间 vs 联邦学习", b)


def fig11_3():
    """图11-3　协同主权 4 层（个人/部门/企业/城市）"""
    b = defs()
    b += text(60, 65, "图11-3　协同主权层级关系", "title", "start")
    b += text(800, 115, "每层有可授权什么 / 责任不能外包的边界", "label")

    # 4 层嵌套（同心圆）—— 国家与城市合并为第四层
    cx, cy = 800, 480
    radii = [320, 250, 180, 100]
    labels = ["国家 / 城市", "企业", "组织单元", "个人"]
    for rad, label in zip(radii, labels):
        b += f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="none" stroke="#506273" stroke-width="2"/>'
        # 在圆的右边标 label
        b += text(cx + rad + 8, cy + 5, label, "small", "start")

    # 跨层互操作
    layers_pos = [(60, 180, "个人 ↔ 组织单元", "跨部门任务最小披露"),
                  (60, 380, "组织单元 ↔ 企业", "联邦检索 + 数据契约"),
                  (60, 580, "企业 ↔ 国家/城市", "采购 + 退出能力 + 公共责任"),
                  (60, 780, "跨境共同规则", "语言 + 知识多样性（不能成「少数人默认值」)")]
    for x, y, label, sub in layers_pos:
        b += box(x, y, 360, 100, "accent", label, sub)

    # 中间
    b += f'<circle cx="{cx}" cy="{cy}" r="40" fill="#1f4e79"/>'
    b += text(cx, cy + 5, "主权", "label", "middle")

    svg("fig11-3_collaborative-sovereignty.svg", "图11-3 协同主权层级关系", b)


def fig11_4():
    """图11-4　能力 × 权限边界"""
    b = defs()
    b += text(60, 65, "图11-4　能力 × 权限边界", "title", "start")
    b += text(800, 115, "能力变强不等于权限自动放宽", "label")

    # 上半：能力放大曲线
    b += text(60, 200, "能力放大（2024—2030）", "label", "start")
    b += '<line x1="80" y1="240" x2="1520" y2="240" class="dash"/>'
    b += '<path d="M150,420 C400,370 700,310 900,270 C1100,240 1300,210 1500,200" stroke="#3b82f6" stroke-width="5" fill="none"/>'
    b += text(1500, 195, "能力 ↑", "small", "start")

    # 下半：权限审查曲线（接近水平）
    b += text(60, 520, "权限审查（按比例）", "label", "start")
    b += '<line x1="80" y1="560" x2="1520" y2="560" class="dash"/>'
    b += '<path d="M150,720 C400,710 700,700 900,700 C1100,700 1300,700 1500,700" stroke="#ef4444" stroke-width="5" fill="none"/>'
    b += text(1500, 690, "权限 →", "small", "start")

    # 3 个交叉点
    intersections = [
        (450, 380, "内部工具 → 边界变严"),
        (900, 290, "公共服务 → 高风险审查"),
        (1300, 230, "公共系统门槛 → 多重审查"),
    ]
    for x, y, label in intersections:
        b += f'<circle cx="{x}" cy="{y}" r="10" fill="#10b981"/>'
        b += text(x, y - 30, label, "tiny", "middle")

    # 高影响决定需要（修正版：去掉"双人批准"硬约束）
    b += box(60, 770, 1480, 110, "pink", "高影响决定需要什么", "① 审计日志 ② 申诉路径 ③ 定期复审；能力每升一级，权限不能自动放宽——门槛形式依组织而定")

    svg("fig11-4_capability-permission.svg", "图11-4 能力 × 权限边界", b)


def fig11_5():
    """图11-5　职位 → 任务 迁移图"""
    b = defs()
    b += text(60, 65, "图11-5　工作从职位流向任务", "title", "start")
    b += text(800, 115, "从年度工资包到一次性任务券；组织记忆也要跟上", "label")

    # 左：传统职位
    b += box(60, 180, 660, 100, "muted", "传统职位", "年度 · 部门 · KPI")
    b += cell(60, 300, 660, 140, "muted", ["年度合同", "部门归属", "晋升路径", "KPI + 年终"], line_h=26)

    # 中间箭头
    b += '<path d="M720,230 L880,230" class="line" marker-end="url(#arrow)"/>'
    b += text(800, 220, "迁移", "tiny", "middle")

    # 右：任务
    b += box(880, 180, 660, 100, "accent", "任务", "一次性 · 跨部门 · 完成凭证")
    b += cell(880, 300, 660, 140, "muted", ["一次性合约", "跨部门边界", "完成证据", "任务券结算"], line_h=26)

    # 5 项配套
    b += text(60, 480, "5 项配套制度变化", "label", "start")
    items = [
        (60, "招聘", "从岗位描述到任务描述"),
        (340, "绩效", "从 KPI 到完成证据"),
        (620, "培训", "从长期岗位培训到任务能力"),
        (900, "离职", "从档案转移 + 任务交接"),
        (1180, "税务", "从工资税到任务券结算"),
    ]
    for x, label, sub in items:
        b += box(x, 510, 280, 130, "warm", label, sub)

    # 底部：组织记忆
    b += box(60, 690, 1480, 130, "muted", "组织记忆", "任务沉淀的知识 / 失败 / 修复必须能被机器使用、能被人解释——否则任务流变成黑箱")

    svg("fig11-5_job-to-task.svg", "图11-5 工作从职位流向任务", b)


def fig11_6():
    """图11-6　过程原生 vs 产品原生"""
    b = defs()
    b += text(60, 65, "图11-6　过程原生 vs 产品原生", "title", "start")
    b += text(800, 115, "两类不同的方法栈；可结合，不可混淆", "label")

    # 左半：过程原生
    b += box(60, 180, 720, 80, "warm", "过程原生", "process-native")
    stages_l = [
        (60, "① 输入", "真实任务 + 上下文"),
        (60, "② 决策", "智能体 + 人工批准"),
        (60, "③ 工具", "调用 + 副作用"),
        (60, "④ 结果", "可复盘的产物"),
        (60, "⑤ 沉淀", "进入知识 / 评测"),
    ]
    ys = [280, 380, 480, 580, 680]
    for y, (x, label, sub) in zip(ys, stages_l):
        b += box(x, y, 720, 90, "muted", label, sub)
    for y in [370, 470, 570, 670]:
        b += f'<path d="M420,{y} L420,{y+10}" class="line" marker-end="url(#arrow)"/>'

    # 右半：产品原生
    b += box(820, 180, 720, 80, "accent", "产品原生", "product-native")
    stages_r = [
        (820, "① 数据", "训练样本"),
        (820, "② 模型", "训练 + 评测"),
        (820, "③ 部署", "推理服务"),
        (820, "④ 维护", "版本 + 监控"),
    ]
    ys2 = [280, 420, 560, 700]
    for y, (x, label, sub) in zip(ys2, stages_r):
        b += box(x, y, 720, 130, "muted", label, sub)
    for y in [410, 550, 690]:
        b += f'<path d="M1180,{y} L1180,{y+10}" class="line" marker-end="url(#arrow)"/>'

    # 底部结合
    b += box(60, 800, 1480, 80, "muted", "结合点", "模型可以再被过程使用（过程内调用模型）；过程可以生成训练数据（沉淀进入产品）")

    svg("fig11-6_process-vs-product.svg", "图11-6 过程原生 vs 产品原生", b)


def fig11_7():
    """图11-7　人机分工 4 类（2×2 矩阵）"""
    b = defs()
    b += text(60, 65, "图11-7　人机分工 4 类", "title", "start")
    b += text(800, 115, "哪些事必须人 / 哪些事可以机器 / 哪些事要共做 / 哪些事要机器兜底", "label")

    # 2×2 矩阵
    # 横轴：判断难度（低 → 高）；纵轴：行动频率（低 → 高）
    b += text(60, 200, "行动频率 ↑", "small", "start")
    b += text(1500, 580, "判断难度 →", "small", "end")

    # 4 象限
    b += box(700, 200, 400, 220, "green", "检索 · 起草", "低判断 + 高频率：可以机器做（Copilot 类）")
    b += box(1120, 200, 400, 220, "accent", "执行 + 工具调用", "中判断 + 高频率：人机共做")
    b += box(700, 440, 400, 220, "warm", "失败回收 · 回滚", "低判断 + 中频率：机器兜底")
    b += box(1120, 440, 400, 220, "pink", "价值判断 · 责任签署", "高判断 + 低频率：必须人")

    # 中央箭头
    b += text(900, 410, "←", "label", "middle")

    # 底部说明
    b += box(60, 720, 1480, 130, "muted", "分工判断标准", "判断难度高 + 影响大 → 必须人；判断难度低 + 影响小 → 可以机器；中间地带 → 共做；机器兜底用于失败 / 异常 / 兜底答案")

    svg("fig11-7_human-machine.svg", "图11-7 人机分工 4 类", b)


def fig11_8():
    """图11-8　责任 × 学习 矩阵"""
    b = defs()
    b += text(60, 65, "图11-8　组织规模仍受责任与学习约束", "title", "start")
    b += text(800, 115, "为什么 OPC 的责任集中仍可持续", "label")

    # 2×2 矩阵
    b += text(60, 200, "学习集中度 ↑", "small", "start")
    b += text(1500, 580, "责任集中度 →", "small", "end")

    # 4 象限
    b += box(700, 200, 400, 220, "muted", "大企业", "责任分散 + 学习分散")
    b += box(1120, 200, 400, 220, "warm", "中型组织", "责任分散 + 学习集中")
    b += box(700, 440, 400, 220, "warm", "边缘自雇", "责任集中 + 学习分散")
    b += box(1120, 440, 400, 220, "green", "OPC", "责任集中 + 学习可外接")

    # 中心
    b += text(920, 430, "OPC 的特殊位置", "label", "middle")
    b += text(920, 460, "一人 + 极大能力网络", "small", "middle")

    # 底部
    b += box(60, 720, 1480, 130, "muted", "为什么 OPC 可持续", "责任集中让人对小任务负责任；学习可外接让一个人接入城市级生态——这与传统「小团队 / 自雇」不同")

    svg("fig11-8_responsibility-learning.svg", "图11-8 责任 × 学习 矩阵", b)


def fig11_9():
    """图11-9　角色迁移时间轴"""
    b = defs()
    b += text(60, 65, "图11-9　人的角色从亲手完成转向设计与接管", "title", "start")
    b += text(800, 115, "三阶段时间轴：亲手完成 → 工具辅助 → 设计与接管", "label")

    # 3 段时间轴（避免硬定年份；用"过去的 / 现在的 / 接下来的"）
    stages = [
        (60, "过去的阶段", "亲手完成", "人完成大部分动作", "muted"),
        (560, "当前的阶段", "工具辅助", "模型与 Copilot 加入", "accent"),
        (1060, "接下来的阶段", "设计与接管", "Agent + 设计 review + 异常接管", "warm"),
    ]
    for x, period, label, sub, cls in stages:
        b += box(x, 200, 460, 130, cls, period, "")
        b += text(x + 230, 290, label, "label", "middle")
        b += text(x + 230, 320, sub, "small", "middle")

    # 5 项新能力
    b += text(60, 400, "5 项新能力", "label", "start")
    abilities = [
        (60, "设计", "任务契约 · 接口"),
        (340, "验收", "完成证据 · 评测"),
        (620, "审计", "日志 · 凭证"),
        (900, "接管", "异常处理 · 回滚"),
        (1180, "替换", "工具切换 · 重新选型"),
    ]
    for x, label, sub in abilities:
        b += box(x, 430, 280, 130, "muted", label, sub)

    # 失败模式
    b += box(60, 620, 1480, 110, "pink", "每阶段失败模式", "① 亲手阶段：不会使用工具 ② 工具阶段：被工具反向控制 ③ 设计与接管阶段：能力膨胀 / 责任稀释")

    svg("fig11-9_role-transition.svg", "图11-9 角色迁移时间轴", b)


def fig11_10():
    """图11-10　组织记忆 3 道关"""
    b = defs()
    b += text(60, 65, "图11-10　组织记忆必须能被机器使用，也能被人解释", "title", "start")
    b += text(800, 115, "3 道关：抽取 → 结构化 → 双面表达", "label")

    # 3 道关
    b += box(60, 200, 460, 130, "accent", "① 抽取", "从经验中识别规则")
    b += box(560, 200, 460, 130, "warm", "② 结构化", "规则变成可机读")
    b += box(1060, 200, 480, 130, "green", "③ 双面表达", "机器可用 + 人可解释")

    # 箭头
    b += '<path d="M520,265 L560,265" class="line" marker-end="url(#arrow)"/>'
    b += '<path d="M1020,265 L1060,265" class="line" marker-end="url(#arrow)"/>'

    # 每关失败示例
    fails = [
        (60, "抽取失败", "经验留在人脑 · 离职即丢"),
        (560, "结构化失败", "结构化但无法查询"),
        (1060, "双面表达失败", "机器懂人不懂 · 或反之"),
    ]
    for x, label, sub in fails:
        b += box(x, 380, 460, 100, "pink", label, sub)

    # 与图5-4 对照
    b += box(60, 530, 1480, 110, "muted", "与图5-4 个人记忆对照", "个人记忆：事实 / 偏好 / 推断 × 时间 / 场景 / 解释三道边界；组织记忆：抽取 / 结构化 / 双面表达三道关——结构相似，主体不同")

    # 底部
    b += box(60, 690, 1480, 130, "green", "成功标志", "任务结束后，下一个 Agent 能从组织记忆里找到上一次的经验——并且人能复核")

    svg("fig11-10_org-memory.svg", "图11-10 组织记忆 3 道关", b)


def fig11_11():
    """图11-11　岗位边界卡片（5 智能体 × 6 字段）"""
    b = defs()
    b += text(60, 65, "图11-11　每个智能体都要有岗位边界", "title", "start")
    b += text(800, 115, "5 智能体 × 6 字段卡片", "label")

    # 表头
    headers = ["", "客服", "财务", "法务", "公共审批", "个人助理"]
    col_x = [60, 350, 590, 830, 1070, 1310]
    col_w = [280, 230, 230, 230, 230, 230]
    for x, w, h in zip(col_x, col_w, headers):
        b += box(x, 180, w, 50, "warm", h, "")

    # 6 行
    rows = [
        ("能做什么", ["查订单", "查账户", "查案例", "查申请", "读邮件"]),
        ("不能做什么", ["删账户", "改账户", "改条款", "批申请", "发邮件"]),
        ("谁授权", ["运营经理", "CFO", "法务总监", "行政主管", "用户本人"]),
        ("谁审计", ["运营 + AI", "财务审计", "法务审计", "公众 + 内部", "用户自己"]),
        ("谁回收", ["关停 Agent", "人工接管", "法务部", "撤销授权", "撤销凭证"]),
        ("失败后果", ["客户投诉", "财务损失", "法律责任", "公共争议", "个人损失"]),
    ]
    colors = ["green", "pink", "accent", "accent", "accent", "pink"]
    for i, (field, vals) in enumerate(rows):
        y = 250 + i * 80
        b += box(60, y, 280, 70, "muted", field, "")
        for j, (x, w) in enumerate(zip(col_x[1:], col_w[1:])):
            b += cell(x, y, w, 70, colors[i], [vals[j]], line_h=20, text_cls="small")

    # 底部
    b += box(60, 750, 1480, 90, "muted", "边界变更的 3 道流程", "① 谁批准边界变更 ② 变更是否对外公开 ③ 失败后能否回滚")

    svg("fig11-11_agent-boundary.svg", "图11-11 每个智能体都要有岗位边界", b)


def fig11_12():
    """图11-12　管理接口 4 类"""
    b = defs()
    b += text(60, 65, "图11-12　管理从盯人转向设计接口与处理例外", "title", "start")
    b += text(800, 115, "管理者的工作重新定义为 4 类接口设计", "label")

    # 4 象限
    b += box(60, 200, 700, 200, "accent", "① 任务契约", "定义完成条件 + 数据范围 + 工具权限")
    b += box(800, 200, 700, 200, "warm", "② 凭证与权限", "授权链 + 凭证生命周期 + 撤销机制")
    b += box(60, 430, 700, 200, "green", "③ 评测与异常", "评测集 + 异常告警 + 边界冲突")
    b += box(800, 430, 700, 200, "pink", "④ 申诉路径", "申诉入口 + 复核流程 + 退出")

    # 中央
    b += '<circle cx="800" cy="415" r="50" fill="#1f4e79"/>'
    b += text(800, 410, "管理者", "label", "middle")
    b += text(800, 432, "精力分配", "small", "middle")

    # 健康团队例外占比（去掉无来源阈值）
    b += box(60, 670, 1480, 130, "muted", "管理者精力如何分配（无固定阈值）", "例外占比随任务类型变化；图7-9 七天测试用于「账是否对得上」，不替代这里的判断")

    svg("fig11-12-management-interface.svg", "图11-12 管理接口 4 类", b)


def fig11_13():
    """图11-13　原生组织 10 项检验（雷达图）"""
    b = defs()
    b += text(60, 65, "图11-13　原生组织的十项检验", "title", "start")
    b += text(800, 115, "10 项检验 × 4 圈（运行闭环 + 责任约束）", "label")

    import math
    cx, cy = 800, 480
    r = 280
    axes = ["边界", "凭证", "评测", "任务契约", "异常路径", "学习循环", "申诉", "替换", "公共责任", "学习资产"]

    # 10 轴（去掉分数；只画雷达图骨架）
    for i, label in enumerate(axes):
        angle = math.radians(i * 36 - 90)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        b += f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" class="dash"/>'
        # label 位置稍微外推
        lx = cx + (r + 30) * math.cos(angle)
        ly = cy + (r + 30) * math.sin(angle)
        anchor = "middle"
        if math.cos(angle) > 0.3: anchor = "start"
        elif math.cos(angle) < -0.3: anchor = "end"
        b += text(lx, ly, label, "small", anchor)

    # 中心
    b += f'<circle cx="{cx}" cy="{cy}" r="6" fill="#1f4e79"/>'

    # 底部：十项检验的性质
    b += box(60, 800, 480, 80, "muted", "检验性质", "每项是「运行闭环 + 责任约束」子问题；不是评分尺度")
    b += box(560, 800, 460, 80, "warm", "前七问（前七项）", "对应运行闭环：身份/凭证/评测/任务/异常/学习/申诉")
    b += box(1040, 800, 460, 80, "green", "后三问（后三项）", "对应责任/人才/收益分配约束")

    svg("fig11-13_org-radar.svg", "图11-13 原生组织的十项检验", b)


# ============================================================
# 结语 6 张
# ============================================================

def fig_ep_1():
    """图结语-1　完整系统 5 要素"""
    b = defs()
    b += text(60, 65, "图结语-1　主权存在于完整系统怎样运行", "title", "start")
    b += text(800, 115, "完整系统 5 要素：缺一即失败", "label")

    # 中央：完整系统
    b += '<circle cx="800" cy="480" r="120" fill="#1f4e79"/>'
    b += text(800, 470, "完整系统", "label", "middle")
    b += text(800, 500, "主权存在", "small", "middle")

    # 5 要素（围绕）
    elements = [
        (800, 220, "身份", "muted"),
        (1280, 350, "凭证", "accent"),
        (1280, 650, "评测", "warm"),
        (800, 780, "异常路径", "pink"),
        (320, 650, "任务契约", "green"),
    ]
    # 任务契约在 320,650
    elements = [
        (800, 220, "身份", "muted"),
        (1280, 350, "凭证", "accent"),
        (1280, 650, "评测", "warm"),
        (800, 780, "异常路径", "pink"),
        (320, 650, "任务契约", "green"),
    ]
    for x, y, label, cls in elements:
        b += box(x - 80, y - 40, 160, 80, cls, label, "")

    # 连线
    for x, y, *_ in elements:
        b += f'<line x1="800" y1="480" x2="{x}" y2="{y}" class="dash"/>'

    svg("fig-ep-1_complete-system.svg", "图结语-1 完整系统 5 要素", b)


def fig_ep_2():
    """图结语-2　六能力 × 四责任 矩阵"""
    b = defs()
    b += text(60, 65, "图结语-2　六能力 × 四责任矩阵", "title", "start")
    b += text(800, 115, "六能力与四级责任必须一起检验", "label")

    # 表头
    abilities = ["理解", "评价", "选择", "取得", "改造", "使用"]
    responsibilities = ["个人", "组织", "企业", "国家/城市"]

    # 6 列 × 4 行
    col_w = 200
    row_h = 130
    x0 = 460
    y0 = 180

    # 列头
    for i, ab in enumerate(abilities):
        b += box(x0 + i * col_w, y0, col_w, 50, "warm", ab, "")

    # 行头 + 数据
    cell_data = [
        ("个人", ["必须", "必须", "必须", "必须", "必须", "必须"]),
        ("组织", ["部分", "必须", "必须", "必须", "部分", "部分"]),
        ("企业", ["外包", "部分", "必须", "必须", "部分", "必须"]),
        ("国家/城市", ["外包", "外包", "部分", "部分", "外包", "必须"]),
    ]
    color_map = {"必须": "green", "部分": "warm", "外包": "muted"}
    for ri, (resp, levels) in enumerate(cell_data):
        y = y0 + 50 + ri * row_h
        b += box(x0 - 150, y, 150, row_h, "accent", resp, "")
        for ci, lvl in enumerate(levels):
            b += box(x0 + ci * col_w, y, col_w, row_h, color_map[lvl], lvl, "")

    # 边界外：不允许的组合
    b += box(60, 760, 1480, 130, "pink", "不允许的组合",
             "① 企业可以'选择'模型，但'使用'的责任不能全部外包给个人  ② 个人可以'使用' AI，但'评价'的责任不能外包给企业  ③ 国家可以'评价'风险，但'改造'的责任不能外包给单一供应商")

    svg("fig-ep-2_six-by-four.svg", "图结语-2 六能力 × 四责任矩阵", b)


def fig_ep_3():
    """图结语-3　权利 → 运行 5 步转换"""
    b = defs()
    b += text(60, 65, "图结语-3　AgenticOps 把权利变成日常运行", "title", "start")
    b += text(800, 115, "5 步转换：权利定义 → 凭证生成 → 任务契约 → 运行时检查 → 异常回收", "label")

    # 5 步水平流程
    steps = [
        (60, "① 权利定义", "谁可以做什么"),
        (340, "② 凭证生成", "短期 · 任务绑定"),
        (620, "③ 任务契约", "完成条件 + 数据范围"),
        (900, "④ 运行时检查", "凭证 · 日志 · 状态"),
        (1180, "⑤ 异常回收", "停止 · 撤销 · 复盘"),
    ]
    for x, label, sub in steps:
        b += box(x, 220, 260, 130, "accent", label, sub)

    for x in [320, 600, 880, 1160]:
        b += f'<path d="M{x},380 L{x+20},380" class="line" marker-end="url(#arrow)"/>'

    # 失败示例 + 修复路径（每步）
    b += box(60, 400, 1480, 130, "pink", "每步失败示例",
             "① 权利未定义  ② 凭证被复制  ③ 任务契约宽松  ④ 运行时检查被绕过  ⑤ 异常无人响应")

    b += box(60, 560, 1480, 130, "green", "修复路径",
             "① 权利写入合同  ② 凭证有时效 + 范围  ③ 契约可验证  ④ 检查不可绕过  ⑤ 异常有 SLA")

    # 与图4-1 三循环的链接
    b += box(60, 720, 1480, 130, "muted", "与图4-1 三循环链接", "交付循环定义权利；运行循环执行检查；学习循环改进权利——5 步嵌入三个循环")

    svg("fig-ep-3_right-to-runtime.svg", "图结语-3 权利 → 运行 5 步转换", b)


def fig_ep_4():
    """图结语-4　能力分配 vs 治理边界"""
    b = defs()
    b += text(60, 65, "图结语-4　开源改变能力分配，但不取消治理", "title", "start")
    b += text(800, 115, "两条平行强调——为什么开源不能替代治理", "label")

    # 上半：能力扩散
    b += text(60, 200, "能力扩散（开源可以扩大）", "label", "start")
    b += box(60, 240, 1480, 120, "green", "扩散", "开放权重 + 蒸馏 + 量化 + 论文 + 人才流动")
    b += '<path d="M150,360 C400,340 700,320 900,310 C1100,300 1300,290 1500,280" stroke="#10b981" stroke-width="5" fill="none"/>'

    # 中间：交汇
    b += box(60, 400, 1480, 110, "muted", "交汇处", "能力扩散到更多主体，治理边界仍然必要——开源让更多人能改，但不取消谁负责改、谁能替换")

    # 下半：治理边界
    b += text(60, 540, "治理边界（开源不能替代）", "label", "start")
    b += box(60, 580, 1480, 120, "warm", "边界", "审计 + 凭证 + 申诉 + 替换 + 公共责任")
    b += '<path d="M150,760 C400,750 700,740 900,730 C1100,720 1300,710 1500,700" stroke="#ef4444" stroke-width="5" fill="none"/>'

    svg("fig-ep-4_capability-vs-governance.svg", "图结语-4 能力分配 vs 治理边界", b)


def fig_ep_5():
    """图结语-5　理论反例结构（3 类反证路径）"""
    b = defs()
    b += text(60, 65, "图结语-5　一套理论也应当允许被证伪", "title", "start")
    b += text(800, 115, "3 类反证路径 × 6 项预测（图11-1）的反证条件", "label")

    # 中央：6 项预测
    b += '<circle cx="800" cy="450" r="100" fill="#1f4e79"/>'
    b += text(800, 445, "6 项预测", "label", "middle")
    b += text(800, 475, "图11-1", "small", "middle")

    # 3 类反证
    categories = [
        (60, "① 可观测指标不达", "实际数据 vs 预测", "muted"),
        (560, "② 反例任务失败", "模型无法完成关键任务", "warm"),
        (1060, "③ 预测失效", "长期趋势反向", "pink"),
    ]
    for x, label, sub, cls in categories:
        b += box(x, 250, 480, 130, cls, label, sub)
        b += box(x, 400, 480, 130, "muted", "反证条件", "见各项预测的反例描述")

    # 连线
    for x in [300, 800, 1300]:
        b += f'<path d="M800,450 L{x},315" class="dash" marker-end="url(#arrow)"/>'

    # 反证触发后的修订流程
    b += box(60, 580, 1480, 130, "green", "反证触发后的修订流程",
             "① 记录反证（数据 · 时间 · 任务）　② 区分预测边界 vs 预测错误　③ 修订或撤回　④ 公告　⑤ 重新设定观察指标")

    svg("fig-ep-5_falsification.svg", "图结语-5 理论反例结构", b)


def fig_ep_6():
    """图结语-6　一次真实任务的最小清单"""
    b = defs()
    b += text(60, 65, "图结语-6　从一项真实任务开始", "title", "start")
    b += text(800, 115, "5 步最小行动清单", "label")

    # 5 步垂直流程
    steps = [
        (180, "① 选一项真实任务", "不是演示 · 不是测试"),
        (300, "② 定义边界", "数据范围 · 完成条件 · 退出条件"),
        (420, "③ 设凭证", "谁能调用 · 能调用什么"),
        (540, "④ 跑一次", "观察日志 · 收集证据"),
        (660, "⑤ 看证据", "结果是否可复盘 · 能否迁移"),
    ]
    for y, label, sub in steps:
        b += box(700, y, 800, 100, "accent", label, sub)
        if y < 660:
            b += f'<path d="M1100,{y+100} L1100,{y+120}" class="line" marker-end="url(#arrow)"/>'

    # 完成后保留的资产清单
    b += box(60, 800, 1480, 80, "green", "完成后应保留的资产",
             "凭证模板 + 任务契约模板 + 评测集 + 失败案例 + 修复路径——下一个 Agent 可继承")

    svg("fig-ep-6_minimal-task.svg", "图结语-6 一次真实任务的最小清单", b)


# ============================================================
# 主调用
# ============================================================

if __name__ == "__main__":
    print("=== 第八章 4 张 ===")
    fig8_12_1(); print("fig8-12_four-cities-start.svg OK")
    fig8_12_2(); print("fig8-12_yancheng.svg OK")
    fig8_12_3(); print("fig8-12_chongqing.svg OK")
    fig8_12_4(); print("fig8-12_longgang.svg OK")

    print("=== 第十章 5 张 ===")
    fig10_1(); print("fig10-1_four-opens-vs-equilibrium.svg OK")
    fig10_2(); print("fig10-2_supply-chain.svg OK")
    fig10_3(); print("fig10-3_hf-incident.svg OK")
    fig10_4(); print("fig10-4_supply-chain.svg OK")
    fig10_5(); print("fig10-5_diffusion-vs-control.svg OK")

    print("=== 第九章 4 张 ===")
    fig9_2(); print("fig9-2_dependency-types.svg OK")
    fig9_3(); print("fig9-3_recovery-steps.svg OK")
    fig9_4(); print("fig9-4-resilience.svg OK")
    fig9_5(); print("fig9-5-audit-boundaries.svg OK")

    print("=== 第十一章 12 张 ===")
    fig11_2(); print("fig11-2_data-space-vs-fl.svg OK")
    fig11_3(); print("fig11-3_collaborative-sovereignty.svg OK")
    fig11_4(); print("fig11-4_capability-permission.svg OK")
    fig11_5(); print("fig11-5_job-to-task.svg OK")
    fig11_6(); print("fig11-6_process-vs-product.svg OK")
    fig11_7(); print("fig11-7_human-machine.svg OK")
    fig11_8(); print("fig11-8_responsibility-learning.svg OK")
    fig11_9(); print("fig11-9_role-transition.svg OK")
    fig11_10(); print("fig11-10_org-memory.svg OK")
    fig11_11(); print("fig11-11_agent-boundary.svg OK")
    fig11_12(); print("fig11-12-management-interface.svg OK")
    fig11_13(); print("fig11-13_org-radar.svg OK")

    print("=== 结语 6 张 ===")
    fig_ep_1(); print("fig-ep-1_complete-system.svg OK")
    fig_ep_2(); print("fig-ep-2_six-by-four.svg OK")
    fig_ep_3(); print("fig-ep-3_right-to-runtime.svg OK")
    fig_ep_4(); print("fig-ep-4_capability-vs-governance.svg OK")
    fig_ep_5(); print("fig-ep-5_falsification.svg OK")
    fig_ep_6(); print("fig-ep-6_minimal-task.svg OK")

    print("\n=== 总计 31 张 SVG 已生成 ===")
