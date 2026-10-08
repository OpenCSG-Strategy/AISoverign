from mkfig import *


def title(s, sub=None):
    b = [t(40, 40, s, 20, weight='bold')]
    if sub:
        b.append(t(40, 66, sub, 13, fill=MID))
    return b


def poly(pts, fill='#fff', stroke=INK, sw=1.5):
    p = ' '.join(f'{x},{y}' for x, y in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def path(d, sw=1.5, stroke=INK, arrow=True, dash='', fill='none'):
    m = ' marker-end="url(#ar)"' if arrow else ''
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{ds}{m}/>'


# 1-1 contract review pipeline
def fig1_1():
    W, H = 900, 400
    b = title('一次合同审查要经过的五个环节')
    steps = [('备料', ['合同、要求、', '对话、审查规则', 'RAG 找相关材料']),
             ('开机', ['模型读材料，', '逐个 Token', '生成审查意见']),
             ('厂房配合', ['芯片、内存、', '网络、电力、', '冷却']),
             ('排产', ['谁先处理、', '哪些合批、', '是否交给小模型']),
             ('验货', ['事实核对、', '规则检查、', '必要时律师复核'])]
    bw, gap, x0, y0, bh = 148, 25, 32, 90, 150
    for i, (n, lines) in enumerate(steps):
        x = x0 + i * (bw + gap)
        b.append(box(x, y0, bw, bh, fill='#fff'))
        b.append(t(x + bw / 2, y0 + 26, f'第 {i + 1} 步', 12, 'middle', fill=MID))
        b.append(t(x + bw / 2, y0 + 52, n, 17, 'middle', 'bold'))
        b.append(line(x + 18, y0 + 66, x + bw - 18, y0 + 66, arrow=False, stroke=LIGHT, sw=1))
        for j, s in enumerate(lines):
            b.append(t(x + bw / 2, y0 + 90 + j * 20, s, 13, 'middle'))
        if i < 4:
            b.append(line(x + bw + 2, y0 + bh / 2, x + bw + gap - 3, y0 + bh / 2))
    # hidden band
    xe = x0 + 5 * bw + 4 * gap
    b.append(box(x0 - 8, y0 - 10, xe - x0 + 16, bh + 20, fill='none', stroke=MID, dash='6 5', rx=10))
    # output
    lx = x0 + 4 * (bw + gap) + bw / 2
    b.append(line(lx, y0 + bh + 10, lx, 298))
    b.append(box(lx - 75, 300, 150, 46, fill=LIGHT))
    b.append(t(lx, 328, '审查意见', 15, 'middle', 'bold'))
    b.append(t(lx - 90, 328, '用户只看到这一段 →', 13, 'end', fill=MID))
    b.append(t(x0, 284, '虚线框里的五步，用户看不到；它们可能分属五个不同的公司', 13, fill=MID))
    b.append(t(x0, 372, '谁说了算：哪些材料进上下文，用哪个模型、在哪里运行，谁的请求排在前面，验货标准由谁定', 13, fill=MID))
    save('fig1-1_contract_review.svg', svg(W, H, '\n'.join(b)))


# 1-2 five layer cake
def fig1_2():
    W, H = 900, 470
    b = title('五层蛋糕：用户看到的是最上面一层')
    layers = ['应用', '模型', '云数据中心', '芯片和计算设备', '能源']
    shades = ['#fff', '#eeeeee', '#d6d6d6', '#bdbdbd', '#a0a0a0']
    cx, top, lh, gap = 360, 100, 62, 6
    for i, (n, sh) in enumerate(zip(layers, shades)):
        y = top + i * (lh + gap)
        w1 = 200 + i * 70
        w2 = 200 + i * 70 + 50
        pts = [(cx - w1 / 2, y), (cx + w1 / 2, y), (cx + w2 / 2, y + lh), (cx - w2 / 2, y + lh)]
        b.append(poly(pts, fill=sh, sw=2 if i == 0 else 1.5))
        b.append(t(cx, y + lh / 2 + 6, n, 17, 'middle', 'bold'))
    # top annotation
    b.append(t(cx, 88, '最上面一层', 13, 'middle', fill=MID))
    rx = cx + (200 + 50) / 2 + 20
    b.append(line(rx + 150, top + lh / 2, rx + 6, top + lh / 2))
    b.append(t(rx + 160, top + lh / 2 - 4, '普通用户', 15, weight='bold'))
    b.append(t(rx + 160, top + lh / 2 + 18, '每天接触的', 13, fill=MID))
    # bracket bottom three
    yb1 = top + 2 * (lh + gap)
    yb2 = top + 5 * (lh + gap) - gap
    bx = cx + (200 + 4 * 70 + 50) / 2 + 24
    b.append(path(f'M{bx},{yb1} h12 v{yb2 - yb1} h-12', arrow=False))
    b.append(t(bx + 28, (yb1 + yb2) / 2 - 4, '下面三层', 15, weight='bold'))
    b.append(t(bx + 28, (yb1 + yb2) / 2 + 18, '花钱最多、建设最慢', 13, fill=MID))
    b.append(t(cx, top + 5 * (lh + gap) + 18, '自下而上：能源 → 芯片和计算设备 → 云数据中心 → 模型 → 应用', 13, 'middle', fill=MID))
    save('fig1-2_five_layers.svg', svg(W, H, '\n'.join(b)))


# 2-1 ceiling and floor
def fig2_1():
    W, H = 900, 470
    b = title('天花板越来越高，地板越来越低', '示意图，不按比例')
    ax0, ax1, ay = 90, 820, 380
    b.append(line(ax0, ay, ax1, ay, sw=1.5))
    for x, lab in ((150, '二〇二二年'), (450, '二〇二四年'), (750, '二〇二六年')):
        b.append(line(x, ay - 4, x, ay + 4, arrow=False))
        b.append(t(x, ay + 22, lab, 13, 'middle', fill=MID))
    # ceiling
    b.append(path('M120,190 C300,175 520,140 790,100', sw=2.5))
    b.append(t(108, 196, '天花板', 17, 'end', 'bold'))
    b.append(t(330, 196, '前沿实验室不断推高能力', 13, fill=MID))
    b.append(f'<circle cx="750" cy="106" r="5" fill="{INK}"/>')
    b.append(t(740, 90, '前沿模型还在变大：Kimi K3 两万八千亿参数', 13, 'end'))
    # floor
    b.append(path('M120,252 C300,268 520,300 790,330', sw=2.5, dash='8 5'))
    b.append(t(108, 258, '地板', 17, 'end', 'bold'))
    b.append(t(565, 352, '工程师不断压低使用门槛', 13, fill=MID))
    b.append(f'<circle cx="150" cy="254" r="5" fill="{INK}"/>')
    b.append(f'<circle cx="450" cy="288" r="5" fill="{INK}"/>')
    b.append(t(165, 283, 'PaLM：五千四百亿参数', 13))
    b.append(t(450, 268, 'Phi-3-mini：三十八亿参数', 13, 'middle'))
    b.append(box(560, 200, 250, 72, fill=FAINT, stroke=MID))
    b.append(t(685, 228, '同样跨过 MMLU 60% 这道线', 13, 'middle'))
    b.append(t(685, 252, '两年里模型缩小约 142 倍', 15, 'middle', 'bold'))
    b.append(t(40, 440, '压低地板的办法：更干净的训练数据 · 蒸馏 · 剪掉不重要的连接 · 参数精度从十六位压到四位', 13, fill=MID))
    save('fig2-1_ceiling_floor.svg', svg(W, H, '\n'.join(b)))


# 2-2 openness
def fig2_2():
    W, H = 900, 450
    b = title('买产品、买机器、拿图纸')
    cols = [('买产品', '用云端接口（API）',
             ['拿到的是结果', '设备在别人手里', '改价、换版本、调规则', '由对方决定'], '#fff'),
            ('买机器', '拿到开放权重',
             ['可下载、运行、', '检查、改装', '未必知道怎么训练出来', '自己造不出第二台'], '#eeeeee'),
            ('拿图纸', '更完整的开源',
             ['权重之外，还公开', '训练代码、数据说明', '和中间版本', '连图纸和工艺一起给你'], '#d6d6d6')]
    for i, (n, sub, items, sh) in enumerate(cols):
        x = 40 + i * 280
        b.append(box(x, 85, 255, 260, fill=sh))
        # icons
        ix, iy = x + 205, 112
        if i == 0:
            b.append(box(ix - 16, iy - 14, 32, 28, rx=2))
            b.append(line(ix - 16, iy - 4, ix + 16, iy - 4, arrow=False))
        elif i == 1:
            b.append(box(ix - 20, iy - 14, 40, 28, rx=3))
            b.append(f'<circle cx="{ix}" cy="{iy}" r="7" fill="none" stroke="{INK}" stroke-width="1.5"/>')
        else:
            b.append(box(ix - 20, iy - 14, 40, 28, rx=1))
            for k in (-10, 0, 10):
                b.append(line(ix + k, iy - 14, ix + k, iy + 14, arrow=False, sw=0.8, stroke=MID))
            b.append(line(ix - 20, iy, ix + 20, iy, arrow=False, sw=0.8, stroke=MID))
        b.append(t(x + 22, 118, n, 20, weight='bold'))
        b.append(t(x + 22, 148, sub, 14, fill=MID))
        b.append(line(x + 22, 164, x + 233, 164, arrow=False, stroke=MID, sw=1))
        for j, s in enumerate(items):
            b.append(t(x + 22, 196 + j * 28, s, 15))
        if i < 2:
            b.append(line(x + 257, 215, x + 278, 215))
    b.append(line(40, 378, 855, 378, sw=2))
    b.append(t(40, 405, '往右，拿到的越多，能做的越多 →', 13, fill=MID))
    b.append(t(40, 428, '开放把权利交给使用者，也把打补丁、查恶意代码、守许可证、故障恢复的责任一起交了过去', 13, fill=MID))
    save('fig2-2_openness.svg', svg(W, H, '\n'.join(b)))


# 2-3 attachments
def fig2_3():
    W, H = 900, 450
    b = title('同一个模型，接上的东西越多，能做的事越多')
    att = ['聊天窗口', '知识库', '代码仓库和运行环境', '发布系统']
    attw = [96, 84, 172, 96]
    res = ['最多给出几句建议', '能回答内部问题', '能直接改程序', '改动可能直接到达真实用户']
    rh, y0 = 70, 90
    for r in range(4):
        y = y0 + r * (rh + 8)
        cy = y + rh / 2
        b.append(box(40, cy - 22, 70, 44, fill=LIGHT))
        b.append(t(75, cy + 5, '模型', 15, 'middle', 'bold'))
        x = 110
        for k in range(r + 1):
            b.append(line(x, cy, x + 18, cy, arrow=False))
            x += 18
            new = (k == r)
            b.append(box(x, cy - 20, attw[k], 40, fill='#fff', sw=2 if new else 1.2,
                         stroke=INK if new else MID))
            b.append(t(x + attw[k] / 2, cy + 5, att[k], 14, 'middle', 'bold' if new else 'normal',
                       fill=INK if new else MID))
            x += attw[k]
        b.append(line(x + 4, cy, 655, cy, dash='3 4', stroke=MID, sw=1.2))
        b.append(t(665, cy + 5, res[r], 15, weight='bold' if r == 3 else 'normal'))
    b.append(line(40, 410, 870, 410, sw=2))
    b.append(t(40, 436, '模型本身一点没变，它在现实中的权力从说话变成了动手；风险也顺着这些连接传播', 13, fill=MID))
    save('fig2-3_attachments.svg', svg(W, H, '\n'.join(b)))


# 3-1 agent parts
def fig3_1():
    W, H = 900, 470
    b = title('一个智能体由什么组成', '括号里是开车的比方')
    # context
    b.append(box(40, 110, 200, 190, fill=FAINT))
    b.append(t(140, 140, '上下文', 17, 'middle', 'bold'))
    for j, s in enumerate(['系统规则', '对话历史', '检索到的文档', '数据库查询结果']):
        b.append(t(140, 175 + j * 28, s, 14, 'middle'))
    b.append(line(242, 205, 318, 205))
    b.append(t(280, 196, '喂给', 12, 'middle', fill=MID))
    # model
    b.append(box(320, 160, 150, 90, fill=LIGHT, sw=2))
    b.append(t(395, 200, '模型', 17, 'middle', 'bold'))
    b.append(t(395, 225, '（司机）', 14, 'middle', fill=MID))
    # tool
    b.append(box(640, 160, 150, 90, sw=2))
    b.append(t(715, 200, '工具', 17, 'middle', 'bold'))
    b.append(t(715, 225, '（车）', 14, 'middle', fill=MID))
    # loop arrows
    b.append(path('M470,180 C530,150 580,150 638,180'))
    b.append(t(555, 145, '提出调用请求', 13, 'middle'))
    b.append(path('M640,232 C580,262 530,262 472,232'))
    b.append(t(555, 278, '看结果、再调整', 13, 'middle'))
    # account, permission
    b.append(box(590, 300, 120, 56))
    b.append(t(650, 324, '账号', 15, 'middle', 'bold'))
    b.append(t(650, 345, '（车钥匙）', 13, 'middle', fill=MID))
    b.append(box(725, 300, 140, 56))
    b.append(t(795, 324, '权限', 15, 'middle', 'bold'))
    b.append(t(795, 345, '（驾照准开的车型）', 13, 'middle', fill=MID))
    b.append(line(680, 298, 695, 253, arrow=False, stroke=MID))
    b.append(line(780, 298, 760, 253, arrow=False, stroke=MID))
    # loop label
    b.append(t(395, 305, '循环：读状态 → 选下一步 →', 13, 'middle', fill=MID))
    b.append(t(395, 325, '调用工具 → 看结果 → 再调整', 13, 'middle', fill=MID))
    # logs
    b.append(box(40, 385, 825, 50, fill='#fff', dash='6 4'))
    b.append(t(60, 416, '运行记录', 15, weight='bold'))
    b.append(t(135, 416, '（行车记录仪）', 13, fill=MID))
    b.append(t(845, 416, '在模型之外记下用了什么、跑的哪个版本、调了哪些工具', 13, 'end', fill=MID))
    save('fig3-1_agent_parts.svg', svg(W, H, '\n'.join(b)))


# 3-2 six capabilities
def fig3_2():
    W, H = 900, 420
    b = title('六种能力')
    caps = [('选择', '看清方案，按自己目标定'), ('替换', '另一套系统能接手'),
            ('迁移', '模型周围的东西带得走'), ('审计', '在模型之外留下证据'),
            ('组合', '不靠一个模型包打天下'), ('演进', '五年后仍然管得住')]
    for i, (n, g) in enumerate(caps):
        r, c = divmod(i, 3)
        x, y = 40 + c * 280, 80 + r * 130
        b.append(box(x, y, 255, 110))
        b.append(f'<rect x="{x}" y="{y}" width="64" height="110" rx="6" fill="{INK}"/>')
        b.append(f'<rect x="{x + 50}" y="{y}" width="14" height="110" fill="{INK}"/>')
        b.append(t(x + 32, y + 62, n, 20, 'middle', 'bold', fill='#fff'))
        b.append(t(x + 160, y + 61, g, 15, 'middle'))
    b.append(t(40, 375, '六种能力之间会打架。原则只有一条：', 13, fill=MID))
    b.append(t(40, 398, '系统看得越多、做得越多、动作越难撤回，管得就要越严', 15, weight='bold'))
    save('fig3-2_six_capabilities.svg', svg(W, H, '\n'.join(b)))


# 3-3 four questions
def fig3_3():
    W, H = 900, 400
    b = title('随身带着的四个问题', '对一个人、一家企业、一座城市都管用')
    qs = ['它能看到什么？', '它能做什么？', '谁能让它停下来？', '出了事谁负责？']
    for i, q in enumerate(qs):
        x = 40 + i * 207
        b.append(box(x, 95, 190, 110, sw=2))
        b.append(f'<circle cx="{x + 95}" cy="128" r="15" fill="{INK}"/>')
        b.append(t(x + 95, 134, str(i + 1), 16, 'middle', 'bold', fill='#fff'))
        b.append(t(x + 95, 180, q, 16, 'middle', 'bold'))
    b.append(t(40, 252, '“人在回路”：人点最后一下“确认”，三个条件同时满足才算数', 15, weight='bold'))
    conds = ['有足够的时间理解', '有足够的信息判断', '按下停止键不会因此受罚']
    for i, c in enumerate(conds):
        x = 40 + i * 276
        b.append(box(x, 275, 256, 56, fill=FAINT, stroke=MID))
        b.append(t(x + 128, 309, c, 15, 'middle'))
        if i < 2:
            b.append(t(x + 266, 310, '+', 18, 'middle', 'bold'))
    save('fig3-3_four_questions.svg', svg(W, H - 40, '\n'.join(b)))


FIGS = [fig1_1, fig1_2, fig2_1, fig2_2, fig2_3, fig3_1, fig3_2, fig3_3]
if __name__ == '__main__':
    for f in FIGS:
        f()
