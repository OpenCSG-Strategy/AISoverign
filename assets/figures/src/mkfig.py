import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "'Source Han Sans SC','Noto Sans CJK SC','PingFang SC','Microsoft YaHei','WenQuanYi Zen Hei',sans-serif"
INK, MID, LIGHT, FAINT = '#111', '#555', '#bbb', '#eee'


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="{FONT}">\n<rect width="{w}" height="{h}" fill="#fff"/>\n'
            '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>\n{body}\n</svg>\n')


def t(x, y, s, size=15, anchor='start', weight='normal', fill=INK):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}">{s}</text>'


def box(x, y, w, h, fill='#fff', stroke=INK, sw=1.5, rx=6, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def line(x1, y1, x2, y2, arrow=True, sw=1.5, dash='', stroke=INK):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    m = ' marker-end="url(#ar)"' if arrow else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'


def save(name, s):
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(s)


# 0-1 timeline
def fig0_1():
    W, H = 900, 400
    b = [t(40, 40, '二〇二六年七月：开放权重之争与一次 AI 入侵', 20, weight='bold')]
    x0, x1, y = 70, 840, 200
    b.append(line(x0, y, x1, y, arrow=True, sw=2))
    # day 16..31 mapping
    def X(d): return x0 + (d - 15) * (x1 - x0 - 30) / 16
    for d in (16, 20, 24, 28, 31):
        b.append(line(X(d), y - 5, X(d), y + 5, arrow=False))
        b.append(t(X(d), y + 24, f'{d}日', 13, 'middle', fill=MID))
    events_up = [
        (16, '月之暗面发布 Kimi K3', '综合排名第三'),
        (24, '黄仁勋首条 X 帖子', '转发开放权重联名信（25 家）'),
        (28, '联署超过 150 家', 'Anthropic 未签'),
    ]
    for i, (d, a, c) in enumerate(events_up):
        yy = 80 + (i % 2) * 40
        b.append(line(X(d), y - 6, X(d), yy + 30, arrow=False, stroke=MID, dash='3 3'))
        b.append(f'<circle cx="{X(d)}" cy="{y}" r="6" fill="{INK}"/>')
        b.append(t(X(d), yy, a, 15, 'middle', 'bold'))
        b.append(t(X(d), yy + 20, c, 13, 'middle', fill=MID))
    events_dn = [
        (25, '联署到 50 家', ''),
        (27, 'K3 权重公开', '英伟达等成立开放安全联盟'),
    ]
    for i, (d, a, c) in enumerate(events_dn):
        yy = 265 + i * 48
        b.append(line(X(d), y + 6, X(d), yy - 16, arrow=False, stroke=MID, dash='3 3'))
        b.append(f'<circle cx="{X(d)}" cy="{y}" r="5" fill="#fff" stroke="{INK}" stroke-width="2"/>')
        b.append(t(X(d), yy, a, 14, 'middle', 'bold'))
        if c:
            b.append(t(X(d), yy + 19, c, 13, 'middle', fill=MID))
    # HF band
    b.append(box(70, 345, 770, 40, fill=FAINT, stroke=MID, dash='5 4'))
    b.append(t(455, 370, '同月：AI 智能体在安全评测中越界，进入 Hugging Face 生产系统；取证最后靠本地运行的开放权重模型完成', 13, 'middle'))
    save('fig0-1_july2026.svg', svg(W, H, '\n'.join(b)))


# 5-1 action ladder
def fig5_1():
    W, H = 900, 470
    b = [t(40, 40, '离机器越近，把关越严', 20, weight='bold'),
         t(40, 66, '以蒂森克虏伯与西门子工业 Copilot 为例；各级把关方式为示意，并非厂商公布的分级', 13, fill=MID)]
    steps = ['读手册', '解释报错', '写控制代码', '写进工程项目', '下发到控制器', '修改生产参数']
    gates = ['随时可用', '随时可用', '人工检查', '测试环境验证', '安全网关逐项校验', '有权的人批准']
    n = len(steps)
    for i, (s, g) in enumerate(zip(steps, gates)):
        x = 60 + i * 135
        hgt = 90 + i * 45
        y = 430 - hgt
        shade = ['#fff', '#f4f4f4', '#e6e6e6', '#d4d4d4', '#bdbdbd', '#9e9e9e'][i]
        b.append(box(x, y, 118, hgt, fill=shade, rx=4))
        b.append(t(x + 59, y + 26, s, 15, 'middle', 'bold'))
        # gate width
        b.append(t(x + 59, y + 50, '把关：', 12, 'middle', fill=INK))
        b.append(t(x + 59, y + 68, g, 12, 'middle', fill=INK))
    b.append(line(60, 452, 870, 452, sw=2))
    b.append(t(60, 470 - 2, '后果越来越重、越来越难撤回 →', 13, fill=MID))
    save('fig5-1_action_ladder.svg', svg(W, H + 10, '\n'.join(b)))


# 5-2 federated vs hub
def fig5_2():
    W, H = 900, 460
    b = [t(40, 40, '把数据汇到一处，还是让问题去找数据', 20, weight='bold')]
    depts = ['销售', '财务', '法务', '采购']
    # left
    b.append(t(220, 85, '"企业大脑"', 17, 'middle', 'bold'))
    b.append(box(150, 230, 140, 60, fill=LIGHT))
    b.append(t(220, 266, '统一大入口', 15, 'middle', 'bold'))
    b.append(t(220, 340, '员工', 15, 'middle'))
    b.append(line(220, 322, 220, 294))
    for i, d in enumerate(depts):
        x = 50 + i * 90
        b.append(box(x, 115, 75, 45, fill='#fff'))
        b.append(t(x + 37, 143, d + '数据', 13, 'middle'))
        b.append(line(x + 37, 162, 220 + (x + 37 - 220) * 0.3, 228))
    b.append(t(220, 385, '所有数据流向一个入口', 13, 'middle', fill=MID))
    b.append(t(220, 405, '一处被攻破，处处可达', 13, 'middle', fill=MID))
    # divider
    b.append(line(450, 70, 450, 430, arrow=False, stroke=LIGHT, dash='6 5'))
    # right
    b.append(t(680, 85, '让问题去找数据', 17, 'middle', 'bold'))
    b.append(box(610, 230, 140, 60))
    b.append(t(680, 256, '任务路由', 15, 'middle', 'bold'))
    b.append(t(680, 276, '只转发问题', 12, 'middle', fill=MID))
    b.append(t(680, 340, '员工', 15, 'middle'))
    b.append(line(680, 322, 680, 294))
    for i, d in enumerate(depts):
        x = 490 + i * 90
        b.append(box(x, 115, 75, 60, fill=LIGHT))
        b.append(t(x + 37, 140, d, 14, 'middle', 'bold'))
        b.append(t(x + 37, 160, '本地处理', 12, 'middle'))
        cx = 680 + (x + 37 - 680) * 0.3
        b.append(line(cx - 6, 228, x + 31, 178, sw=1.2))
        b.append(line(x + 43, 178, cx + 6, 228, sw=1.2, dash='4 3'))
    b.append(t(680, 385, '实线：问题进去　虚线：只回结论和依据', 13, 'middle', fill=MID))
    b.append(t(680, 405, '原始数据留在负责它的部门', 13, 'middle', fill=MID))
    save('fig5-2_federated.svg', svg(W, H, '\n'.join(b)))


# 5-3 room card
def fig5_3():
    W, H = 900, 440
    b = [t(40, 40, '一张"行动房卡"，以及它在委托中怎样变窄', 20, weight='bold')]
    # card
    b.append(box(40, 70, 330, 300, rx=14, sw=2))
    b.append(f'<rect x="40" y="70" width="330" height="46" rx="14" fill="{INK}"/>')
    b.append(f'<rect x="40" y="100" width="330" height="16" fill="{INK}"/>')
    b.append(t(205, 100, '任务 #2026-1008-031', 15, 'middle', 'bold', fill='#fff'))
    rows = [('代表谁', '行政主管（示例）'), ('能进哪个系统', '公司日历'), ('能做什么', '只读：忙／闲'),
            ('有效期', '今天 18:00 前'), ('能否转交', '不能')]
    for i, (k, v) in enumerate(rows):
        y = 150 + i * 44
        b.append(t(62, y, k, 14, fill=MID))
        b.append(t(350, y, v, 15, 'end', 'bold'))
        if i < 4:
            b.append(line(62, y + 16, 350, y + 16, arrow=False, stroke=FAINT))
    b.append(t(205, 395, '任务结束、取消或风险升高，卡即作废', 13, 'middle', fill=MID))
    # delegation
    lv = [('员工本人', '日历、邮件、文件、审批……', 360), ('行政助手', '读日历　发内部邮件', 250),
          ('排期助手', '只看几个人的忙／闲', 150)]
    for i, (n, p, w) in enumerate(lv):
        y = 85 + i * 105
        x = 640 - w / 2
        b.append(box(x, y, w, 62, fill=['#fff', '#eee', LIGHT][i]))
        b.append(t(640, y + 26, n, 15, 'middle', 'bold'))
        b.append(t(640, y + 47, p, 12, 'middle'))
        if i < 2:
            b.append(line(640, y + 64, 640, y + 102))
            b.append(t(652, y + 88, '委托一层，权限少一圈', 12, fill=MID))
    save('fig5-3_room_card.svg', svg(W, H, '\n'.join(b)))


# 5-4 brakes
def fig5_4():
    W, H = 900, 300
    b = [t(40, 40, '刹车分五档', 20, weight='bold'),
         t(40, 66, '从轻到重；停止开关放在出问题的智能体够不着的地方，并有明确的人有权按下', 13, fill=MID)]
    lv = ['停掉一个工具', '收回高风险权限', '降为只提建议', '切到备用方案', '全部停止，交给人']
    for i, s in enumerate(lv):
        x = 40 + i * 168
        shade = ['#fff', '#eaeaea', '#cfcfcf', '#9a9a9a', '#111'][i]
        fg = '#fff' if i >= 3 else INK
        b.append(box(x, 110, 150, 90, fill=shade))
        b.append(t(x + 75, 145, f'第 {i + 1} 档', 13, 'middle', fill=fg))
        b.append(t(x + 75, 172, s, 15, 'middle', 'bold', fill=fg))
        if i < 4:
            b.append(line(x + 152, 155, x + 166, 155, sw=1.5))
    b.append(line(40, 235, 870, 235, sw=2))
    b.append(t(40, 262, '影响越来越大，恢复越来越慢 →', 13, fill=MID))
    save('fig5-4_brakes.svg', svg(W, H, '\n'.join(b)))


# 5-5 three ledgers
def fig5_5():
    W, H = 900, 330
    b = [t(40, 40, '三本账', 20, weight='bold'),
         t(40, 66, '只看 Token 单价，会漏掉行动风险，也会漏掉没人用上的产出', 13, fill=MID)]
    cols = [('资源账', '花了多少', ['Token、算力', '工具调用次数', '人工分钟'], '用来省钱', '#fff'),
            ('任务账', '做得怎样', ['成功率、耗时', '重试次数', '单任务总成本'], '用来比较方案', '#e8e8e8'),
            ('结果账', '换回了什么', ['问题解决了没有', '返工、投诉、错付', '丢掉的生意'], '老板真正关心', '#c8c8c8')]
    for i, (n, q, items, use, shade) in enumerate(cols):
        x = 40 + i * 285
        b.append(box(x, 90, 260, 210, fill=shade))
        b.append(t(x + 20, 125, n, 18, weight='bold'))
        b.append(t(x + 240, 125, q, 13, 'end', fill=MID))
        for j, it in enumerate(items):
            b.append(t(x + 20, 165 + j * 30, '· ' + it, 14))
        b.append(line(x + 20, 255, x + 240, 255, arrow=False, stroke=MID))
        b.append(t(x + 20, 282, use, 14, weight='bold'))
        if i < 2:
            b.append(line(x + 262, 195, x + 283, 195))
    save('fig5-5_three_ledgers.svg', svg(W, H, '\n'.join(b)))


for f in (fig0_1, fig5_1, fig5_2, fig5_3, fig5_4, fig5_5):
    f()
print(sorted(os.listdir(OUT)))
