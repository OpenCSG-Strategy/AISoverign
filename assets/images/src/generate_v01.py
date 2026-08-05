from pathlib import Path
from math import hypot

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

def fig12():
    b = defs()+text(60,65,"图1-2　模型之外的能力网络","title","start")
    b += text(800,118,"任务是中心；模型只是可替换节点", "label")
    nodes=[(180,220,"身份","谁可以发起"),(580,190,"检索","取什么上下文"),(1030,190,"模型","可替换推理"),(1250,400,"工具","如何行动"),(1050,650,"权限","能做什么"),(560,680,"记忆","保留什么"),(180,520,"评测","结果是否合格"),(340,370,"日志","如何复盘")]
    # 连接线先画，端点停在中心圆边缘；节点和中心文字随后覆盖线条。
    for x,y,_,_ in nodes:
        sx, sy = x + 125, y + 60
        dx, dy = 800 - sx, 450 - sy
        d = hypot(dx, dy)
        ex, ey = 800 - dx / d * 130, 450 - dy / d * 130
        b += f'<path d="M{sx},{sy} L{ex},{ey}" class="line"/>'
    b += '<circle cx="800" cy="450" r="130" fill="#1f4e79"/><text x="800" y="440" style="fill:white" class="label" text-anchor="middle">任务</text><text x="800" y="476" style="fill:white" class="small" text-anchor="middle">目标 · 状态 · 结果</text>'
    for x,y,l,s in nodes:
        b += box(x,y,250,120,"accent" if l=="模型" else "muted",l,s)
    b += '<path d="M1280,250 C1540,280 1540,620 1300,650" class="dash"/><text x="1470" y="610" class="small" text-anchor="middle">替换 / 迁移</text>'
    svg("fig1-2_capability-network.svg","图1-2 能力网络",b)

def fig21():
    b=defs()+text(60,65,"图2-1　一次请求，不等于一项任务","title","start")
    b+=text(800,115,"Request 只是入口；Task 还带着授权、工具、证据与补救路径","label")
    b+=box(80,330,210,110,"accent","Request","一句输入")
    b+=arrow(290,385,415,385,"创建")
    b+=box(420,300,250,170,"warm","Task","目标 · 状态 · 授权")
    b+=arrow(670,345,835,245,"执行")+arrow(670,425,835,525,"需批准")
    b+=box(850,180,250,120,"green","运行中","调用工具 / 产生证据")
    b+=box(850,465,250,120,"warm","等待批准","人或组织确认")
    b+=arrow(1100,240,1260,240,"完成")+arrow(1100,525,1260,525,"批准后继续")
    b+=box(1270,180,230,120,"green","完成","结果可交付")
    b+=box(1270,465,230,120,"muted","失败 / 取消","补救或退出")
    b+=arrow(975,300,975,465,"失败")
    b+=text(800,760,"可治理委托 = 任务边界清楚 + 状态可见 + 授权可撤 + 结果可复盘","label")
    svg("fig2-1_request-task-state.svg","图2-1 请求与任务状态",b)

def fig53():
    b=defs()+text(60,65,"图5-3　企业版 AgenticOps：管理智能体生命周期","title","start")
    b+=text(800,115,"每一阶段都有责任人、证据和停止条件","label")
    stages=[("立项","业务负责人"),("评测","评测负责人"),("影子运行","运行负责人"),("发布","变更负责人"),("观测","值班团队"),("事故响应","风险负责人"),("退役","资产负责人")]
    x0=100; y=390; w=185; gap=35
    for i,(l,s) in enumerate(stages):
        x=x0+i*(w+gap); b+=box(x,y,w,130,"accent" if i<4 else "warm",l,s)
        if i<len(stages)-1: b+=arrow(x+w,y+65,x+w+gap-8,y+65)
    b+='<path d="M1450,555 C1450,760 120,790 120,555" class="dash" marker-end="url(#arrow)"/>'
    b+=text(800,735,"闭环不是自动化流水线：任一阶段都可以暂停、回滚或退出", "label")
    for i,l in enumerate(["目标与边界","基线与反例","不影响生产","版本与批准","漂移与成本","隔离与补救","证据归档"]):
        x=x0+i*(w+gap)+w/2; b+=text(x,575,l,"tiny")
    svg("fig5-3_agenticops-lifecycle.svg","图5-3 AgenticOps 生命周期",b)

def fig71():
    b=defs()+text(60,65,"图8-1　开放控制面：驾驶舱与发动机分离","title","start")
    b+=text(800,115,"主权不等于拥有所有发动机，而是保留切换、审计和退出的驾驶权","label")
    b+=box(170,230,500,430,"accent","控制面 / 驾驶舱","")
    for i,(l,s) in enumerate([("身份","谁可以做什么"),("策略","什么条件下允许"),("评测","结果是否合格"),("证据","发生了什么"),("切换权","如何迁移 / 退出")]):
        b+=box(220,285+i*68,400,52,"muted",l,s)
    b+=box(930,210,480,470,"warm","发动机层 / 执行能力","")
    for i,(l,s) in enumerate([("模型 A","通用推理"),("模型 B","专门任务"),("私有算力","受控环境"),("外部工具","检索 / 交易 / 设备")]):
        b+=box(990,280+i*82,360,62,"muted",l,s)
    b+=arrow(670,350,930,350,"调用")+arrow(930,520,670,520,"证据返回")
    b+=text(800,775,"控制面自身也必须可导出、可验证、可迁移，否则驾驶舱仍被锁定", "label")
    svg("fig8-1_open-control-plane.svg","图8-1 开放控制面",b)

def fig61():
    b=defs()+text(60,65,"图7-1　国家能力藏在危机到来以后：能力飞轮","title","start")
    b+=text(800,115,"一次采购只能得到设备；持续任务才能沉淀共同能力","label")
    cx,cy=800,445
    items=[("基础设施与人才",800,220),("真实公共 / 产业任务",1120,345),("数据、模型与工具",1010,630),("标准与运营经验",590,630),("下一轮吸收能力",480,345)]
    for i,(l,x,y) in enumerate(items): b+=box(x-150,y-55,300,110,"accent" if i in (0,2) else "muted",l,"可验证沉淀")
    for (x1,y1),(x2,y2) in zip([(800,275),(1120,400),(1010,575),(590,575),(480,400)],[(1120,400),(1010,575),(590,575),(480,400),(800,275)]): b+=arrow(x1,y1,x2,y2)
    b+=box(660,385,280,120,"green","能力飞轮","任务 → 沉淀 → 反哺")
    b+=box(1200,730,260,80,"warm","一次采购","飞轮外的反例")
    b+=text(800,805,"判断标准：危机发生后，系统是否还能调度、复盘、迁移与继续运行？", "label")
    svg("fig7-1_national-capability-wheel.svg","图7-1 国家能力飞轮",b)

def fig31():
    b=defs()+text(60,65,"图3-1　本地、受控云与公共云","title","start")
    b+=text(800,115,"先看任务敏感度，再决定部署位置；没有一种模式对所有任务都最优","label")
    cols=[("本地","高敏感 / 可离线","密钥自己保管","明文不出本地","保留期自己决定","导出后可退出","accent"),("受控云","中高敏感 / 需协作","合同与密钥边界","按配置可见","保留期可谈判","迁移需验证","warm"),("公共云","低敏感 / 追求便利","平台托管","按服务条款可见","平台规则决定","退出成本更高","muted")]
    for i,(l,sub,*rows) in enumerate(cols):
        x=100+i*500; b+=box(x,210,400,115,rows[-1],l,sub)
        for j,r in enumerate(rows[:-1]): b+=box(x,350+j*75,400,58,"muted",r,"")
    b+=text(800,760,"隐私判断不是“安全 / 不安全”，而是明文、密钥、保留期与退出方式的组合", "label")
    svg("fig3-1_privacy-modes.svg","图3-1 三种隐私模式",b)

def fig_memory():
    b=defs()+text(60,65,"补图A　个人记忆的三重边界","title","start")
    b+=text(800,115,"记忆不是静态数据库：事实、偏好和推断都要经过时间、场景与解释边界","label")
    b+='<circle cx="800" cy="470" r="240" fill="#e8eef5" stroke="#34495e" stroke-width="4"/><circle cx="800" cy="470" r="165" fill="#fef3c7" stroke="#34495e" stroke-width="4"/><circle cx="800" cy="470" r="90" fill="#dcfce7" stroke="#34495e" stroke-width="4"/>'
    b+=text(800,465,"事实","label")+text(800,500,"本人提供 / 可核对","tiny")
    b+=text(800,350,"偏好","label")+text(800,380,"行为中形成 / 可修正","tiny")
    b+=text(800,230,"推断","label")+text(800,260,"模型生成 / 不等于事实","tiny")
    b+=box(220,330,260,90,"accent","时间边界","多久有效？")+box(1120,330,260,90,"warm","场景边界","在哪里适用？")+box(220,610,260,90,"muted","解释边界","为何这样判断？")
    b+=arrow(480,375,620,430)+arrow(1120,375,980,430)+arrow(480,655,650,530)
    b+=box(1110,610,270,90,"green","本人操作","查看 · 纠正 · 删除")+arrow(980,530,1110,655)
    b+=text(800,805,"过时偏好 → 推荐 → 行为强化；纠正必须能改变后续使用，而不是只改一条显示文字", "label")
    svg("fig3-A_memory-boundaries.svg","补图A 个人记忆边界",b)

def fig_agent_loop():
    b=defs()+text(60,65,"补图B　个人代理控制回路","title","start")
    b+=text(800,115,"低风险草稿可以快，高影响行动必须慢；每一步都保留接管入口","label")
    pts=[("任务契约","目标 / 范围 / 结束条件"),("最小权限","只给本次所需"),("建议或草稿","可比较 / 可追问"),("确认门","人批准或拒绝"),("行动收据","记录发生了什么"),("撤销 / 接管","暂停、回滚、人工继续")]
    for i,(l,s) in enumerate(pts):
        x=135+(i%3)*500; y=250+(i//3)*250; b+=box(x,y,330,125,"accent" if i<3 else "warm",l,s)
    b+=arrow(465,312,625,312)+arrow(965,312,1125,312)+arrow(1290,375,1290,500)+arrow(1125,562,965,562)+arrow(625,562,465,562)
    b+=text(800,760,"循环的终点不是“自动完成”，而是“可复核、可撤回、可接管”", "label")
    svg("fig3-B_personal-agent-loop.svg","补图B 个人代理控制回路",b)

def fig_evidence():
    b=defs()+text(60,65,"补图C　高影响决定的证据链","title","start")
    b+=text(800,115,"能解释结果，不等于能证明结果；受影响的人要有看见、纠正和申诉的路径","label")
    pts=[("来源","原始材料"),("版本","模型 / 规则版本"),("推断","形成了什么判断"),("专业复核","谁检查过"),("通知","影响如何告知"),("申诉 / 纠正","如何改结果"),("删除 / 保留","证据留多久")]
    for i,(l,s) in enumerate(pts):
        x=90+i*215; b+=box(x,330,180,130,"accent" if i<4 else "warm",l,s)
        if i<len(pts)-1: b+=arrow(x+180,395,x+205,395)
    b+=text(800,650,"关键缺口不是“有没有一个分数”，而是能否沿链条回到原始证据并改变结果", "label")
    b+=text(800,730,"不保存无必要的完整思维轨迹；保存足以复盘行动、版本、来源和责任的证据", "small")
    svg("fig4-C_high-impact-evidence.svg","补图C 高影响决定证据链",b)

for f in (fig12, fig21, fig53, fig71, fig61, fig31, fig_memory, fig_agent_loop, fig_evidence): f()
