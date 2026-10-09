from mkfig import *


def title(s):
    return t(40, 40, s, 20, weight='bold')


def sub(s, y=66):
    return t(40, y, s, 13, fill=MID)


# 4-1 four layers
def fig4_1():
    W, H = 900, 440
    b = [title('个人在 AI 里积累的四层东西')]
    layers = [  # bottom -> top
        ('原始资料', '文字、照片、录音、邮件、账单、合同、通讯录', '#fff'),
        ('个人记忆', '资料之间的关系；你的解释、偏好、承诺和教训', '#eaeaea'),
        ('工作方法', '怎么开头、在哪几步求证、怎么交付、出错怎么补救', '#cfcfcf'),
        ('身份和关系', '别人怎么找到你、为什么信任你、谁愿意再找你', '#a8a8a8'),
    ]
    x0, wfull = 60, 600
    for i, (n, d, shade) in enumerate(layers):
        y = 330 - i * 72
        inset = i * 22
        x = x0 + inset
        w = wfull - 2 * inset
        b.append(box(x, y, w, 60, fill=shade, rx=4))
        b.append(t(x + 20, y + 36, n, 16, weight='bold'))
        b.append(t(x + 130, y + 36, d, 13))
    # right annotations
    b.append(line(720, 390, 720, 112, sw=2))
    b.append(t(735, 130, '越往上', 15, weight='bold'))
    b.append(t(735, 152, '越难重建', 15, weight='bold'))
    b.append(box(700, 330, 170, 60, fill=FAINT, stroke=MID, dash='5 4'))
    b.append(t(785, 355, '导出压缩包', 13, 'middle'))
    b.append(t(785, 375, '大致能带走这一层', 13, 'middle'))
    b.append(t(735, 230, '换到新系统，', 13, fill=MID))
    b.append(t(735, 250, '这几层不会', 13, fill=MID))
    b.append(t(735, 270, '自动恢复', 13, fill=MID))
    b.append(t(60, 420, '数据带走了，本事没跟着走', 14, fill=MID))
    body = b[0] + '\n<g transform="translate(0,-34)">' + '\n'.join(b[1:]) + '</g>'
    save('fig4-1_personal_layers.svg', svg(W, H - 34, body))


# 4-2 four levels
def fig4_2():
    W, H = 900, 520
    b = [title('从"读"到"代理"的四级授权')]
    lv = [('读', '看资料，不改任何东西'),
          ('建议', '提出下一步，由人决定'),
          ('代办', '在说清的范围内动手，', '关键节点回来确认'),
          ('代理', '人只给目标，它自己拆步骤、', '挑工具，遇到异常才停下')]
    shades = ['#fff', '#eaeaea', '#cfcfcf', '#a8a8a8']
    for i, item in enumerate(lv):
        x = 40 + i * 210
        hgt = 110 + i * 40
        y = 330 - hgt
        b.append(box(x, y, 195, hgt, fill=shades[i], rx=4))
        b.append(t(x + 97, y + 34, item[0], 18, 'middle', 'bold'))
        for j, s in enumerate(item[1:]):
            b.append(t(x + 97, y + 64 + j * 20, s, 13, 'middle'))
    b.append(line(40, 350, 860, 350, sw=2))
    b.append(t(40, 374, '授权一级一级往上走，人交出去的决定越来越多 →', 13, fill=MID))
    # lower: irreversibility rule
    b.append(t(40, 418, '动作越难撤回，授权就要离当下越近', 16, weight='bold'))
    ex = [('读公开网页', '可以长期授权'), ('改草稿', '按项目授权'),
          ('对外发表声明', '每次确认'), ('给陌生人付款', '一次新的、具体的同意')]
    for i, (a, c) in enumerate(ex):
        x = 40 + i * 210
        b.append(box(x, 435, 185, 62, fill='#fff', stroke=MID, sw=1.2))
        b.append(t(x + 92, 460, a, 14, 'middle', 'bold'))
        b.append(t(x + 92, 483, c, 13, 'middle'))
        if i < 3:
            b.append(line(x + 187, 466, x + 208, 466, sw=1.2))
    save('fig4-2_four_levels.svg', svg(W, H, '\n'.join(b)))


# 4-3 weekend tests
def fig4_3():
    W, H = 900, 470
    b = [title('一个周末的四项测试'),
         sub('挑最重要的那项工作，各做一次')]
    tests = [('失忆测试', ['关掉长期记忆和历史对话，', '只给一页自己写的任务说明'],
              ['还能不能接着干？']),
             ('换人测试', ['换另一款模型、弱一点的本地', '工具，或照文字流程自己做'],
              ['核心事实、步骤和交付物', '能不能恢复？']),
             ('断权测试', ['收回邮箱、日历、网盘或支付', '中的一项权限'],
              ['老实报告"做不了"，', '还是从别的连接绕过去？']),
             ('追账测试', ['随便挑一次已完成的', '重要任务'],
              ['谁发起、用了什么、调了', '什么工具、谁确认的？'])]
    for i, (n, how, look) in enumerate(tests):
        x = 40 + (i % 2) * 420
        y = 90 + (i // 2) * 155
        b.append(box(x, y, 400, 140, rx=6))
        b.append(f'<rect x="{x}" y="{y}" width="110" height="140" rx="6" fill="{FAINT}" stroke="{INK}" stroke-width="1.5"/>')
        b.append(t(x + 55, y + 76, n, 16, 'middle', 'bold'))
        b.append(t(x + 125, y + 28, '做法', 12, fill=MID))
        for j, s in enumerate(how):
            b.append(t(x + 125, y + 48 + j * 19, s, 13))
        b.append(t(x + 125, y + 98, '看', 12, fill=MID))
        for j, s in enumerate(look):
            b.append(t(x + 145, y + 98 + j * 19, s, 13, weight='bold'))
    b.append(box(40, 405, 820, 46, fill=FAINT, stroke=MID, dash='5 4'))
    b.append(t(450, 434, '每次记下恢复花了多长时间：五分钟能恢复的工具故障，和三个月才能重建的客户知识库，不是同一种依赖', 13, 'middle'))
    save('fig4-3_weekend_tests.svg', svg(W, H, '\n'.join(b)))


# 6-1 three national paths
def fig6_1():
    W, H = 900, 510
    b = [title('三条国家路径')]
    cols = [('中国', ['超大市场', '工程优化', '开放模型', '算力组织'], ['先进芯片', '跨厂商互联', '框架生态', '规则执行']),
            ('中东', ['能源', '公共资本', '国际联盟', '技术准入'], ['出口许可', '芯片和软件栈', '合作方的治理要求']),
            ('东南亚', ['本地语言适配', '开放模型', '跨国互通', '数据中心走廊'], ['外部基础模型', '云和芯片', '人才和持续维护'])]
    for i, (n, have, ctrl) in enumerate(cols):
        x = 60 + i * 270
        w = 240
        b.append(f'<rect x="{x}" y="70" width="{w}" height="44" rx="6" fill="{INK}"/>')
        b.append(t(x + w / 2, 99, n, 17, 'middle', 'bold', fill='#fff'))
        b.append(box(x, 124, w, 150, fill='#fff'))
        b.append(t(x + 16, 148, '主要靠什么', 13, fill=MID))
        for j, s in enumerate(have):
            b.append(t(x + 16, 174 + j * 24, '· ' + s, 14))
        b.append(box(x, 284, w, 128, fill=FAINT))
        b.append(t(x + 16, 308, '关键控制点还在哪里', 13, fill=MID))
        for j, s in enumerate(ctrl):
            b.append(t(x + 16, 334 + j * 22, '· ' + s, 14))
        b.append(line(x + w / 2, 414, 450 + (x + w / 2 - 450) * 0.25, 446))
    b.append(box(260, 448, 380, 44, fill=LIGHT))
    b.append(t(450, 476, '项目结束以后，能力留在了哪里？', 16, 'middle', 'bold'))
    save('fig6-1_national_paths.svg', svg(W, H, '\n'.join(b)))


# 6-2 five stages
def fig6_2():
    W, H = 900, 300
    b = [title('宣布、签约、获批、在建、上线'),
         sub('读 AI 投资新闻时，五个阶段要分开看')]
    st = ['宣布', '签约', '获批', '在建', '上线']
    gaps = [['未必签了', '合同'], ['未必拿到', '许可'], ['未必设备', '到货'], ['电力、网络、', '软件、客户', '未必就位']]
    shades = ['#fff', '#eaeaea', '#d4d4d4', '#b8b8b8', '#111']
    for i, s in enumerate(st):
        x = 40 + i * 170
        b.append(box(x, 120, 120, 64, fill=shades[i]))
        b.append(t(x + 60, 159, s, 18, 'middle', 'bold', fill='#fff' if i == 4 else INK))
        if i < 4:
            b.append(line(x + 122, 152, x + 168, 152))
            for j, g in enumerate(gaps[i]):
                b.append(t(x + 145, 206 + j * 17, g, 12, 'middle', fill=MID))
    b.append(t(40, 280, '很多误读，来自把这五个阶段当成一回事', 14, weight='bold'))
    save('fig6-2_five_stages.svg', svg(W, H, '\n'.join(b)))


# 6-3 city returns
def fig6_3():
    W, H = 900, 430
    b = [title('一座城市的三种回流')]
    b.append(box(330, 70, 240, 54, fill=LIGHT))
    b.append(t(450, 103, '城市的 AI 公共投入', 16, 'middle', 'bold'))
    nodes = [
        (40, '资源回流', ['本地科研人员、企业和开发者', '更容易用上算力和模型，', '而不只是多一批闲置机柜']),
        (325, '资产回流', ['项目结束后，留下本地能', '维护的代码、模型、测试集、', '数据产品和懂行的人']),
        (610, '价值回流', ['产业收入、公共服务的改善、', '人才的成长，继续投进', '基础设施、教育科研和新企业']),
    ]
    bw, y = 250, 190
    for i, (x, n, ds) in enumerate(nodes):
        b.append(box(x, y, bw, 130))
        b.append(t(x + bw / 2, y + 32, n, 16, 'middle', 'bold'))
        for j, s_ in enumerate(ds):
            b.append(t(x + bw / 2, y + 66 + j * 21, s_, 13, 'middle'))
        b.append(line(450 + (i - 1) * 60, 126, x + bw / 2, y - 3))
    # reinvest loop from value back to input
    b.append(f'<path d="M 860 255 L 880 255 L 880 97 L 574 97" fill="none" stroke="{INK}" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#ar)"/>')
    b.append(t(872, 150, '再投入', 13, 'end', fill=MID))
    b.append(t(40, 370, '算力规模写得出一个大数字，却说明不了谁能用上、排多久的队、花了多少钱，', 13, fill=MID))
    b.append(t(40, 392, '更说明不了用完以后留下了什么', 13, fill=MID))
    save('fig6-3_city_return.svg', svg(W, H, '\n'.join(b)))


# 6-4 robodebt
def fig6_4():
    W, H = 900, 640
    b = [title('一个平均数怎样变成一笔债'),
         sub('澳大利亚"机器人追债"（Robodebt），二〇一五年起；左图为示意，不代表具体个案')]
    # schematic chart
    gx, gy, gw, gh = 60, 110, 360, 190
    b.append(line(gx, gy + gh, gx + gw, gy + gh, arrow=False, sw=1.5))
    b.append(line(gx, gy + gh, gx, gy, arrow=False, sw=1.5))
    vals = [0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0]
    n = len(vals)
    bwid = gw / n
    avg = sum(vals) / n
    for i, v in enumerate(vals):
        x = gx + i * bwid + 4
        hgt = v * 16
        if hgt:
            b.append(box(x, gy + gh - hgt, bwid - 8, hgt, fill=LIGHT, sw=1, rx=0))
    ya = gy + gh - avg * 16
    b.append(line(gx, ya, gx + gw, ya, arrow=False, sw=2, dash='6 4'))
    b.append(t(gx + gw + 8, ya + 5, '平均数', 13, weight='bold'))
    b.append(t(gx + gw / 2, gy + gh + 22, '每两周（一年）', 13, 'middle', fill=MID))
    b.append(t(gx + 4, gy - 10, '实际收入：季节工、临时工忽高忽低', 13, fill=MID))
    b.append(t(gx + gw - 60, ya - 12, '凭空造出的"收入"', 13, 'middle', weight='bold'))
    b.append(t(gx + 60, ya - 12, '凭空造出的"收入"', 13, 'middle', weight='bold'))
    # flow on right
    steps = ['税务部门记录的年度收入', '平均摊到每两周', '和申领人申报的收入对比', '推断"多领了补助"',
             '自动认定欠款，自动寄出催缴', '当事人自己证明没有欠钱']
    fx, fw = 520, 340
    for i, s in enumerate(steps):
        y = 82 + i * 62
        shade = '#111' if i == 5 else ('#d4d4d4' if i >= 3 else '#fff')
        b.append(box(fx, y, fw, 44, fill=shade))
        b.append(t(fx + fw / 2, y + 28, s, 15, 'middle', 'bold' if i >= 3 else 'normal',
                   fill='#fff' if i == 5 else INK))
        if i < 5:
            b.append(line(fx + fw / 2, y + 46, fx + fw / 2, y + 60))
    b.append(t(fx - 14, 82 + 4 * 62 + 10, '统计推断', 13, 'end', fill=MID))
    b.append(t(fx - 14, 82 + 4 * 62 + 30, '被当成事实执行 →', 13, 'end', fill=MID))
    # missing brakes
    b.append(box(40, 470, 820, 70, fill=FAINT, stroke=MID, dash='5 4'))
    b.append(t(60, 497, '本该刹车却没起作用的地方', 14, weight='bold'))
    b.append(t(60, 523, '人工核查退出了流程　·　异议没能及时让系统停下　·　法律上的质疑没有形成有效的刹车', 13))
    # outcome
    b.append(t(40, 580, '结果', 14, weight='bold'))
    b.append(t(90, 580, '运行约五年，向数十万人发出债务通知；约四十七万笔后来被政府承认为非法提出；', 13))
    b.append(t(90, 604, '二〇二一年的和解退还、核销并赔偿约十八亿澳元', 13))
    save('fig6-4_robodebt.svg', svg(W, H, '\n'.join(b)))


# 7-1 three moments
def fig7_1():
    W, H = 900, 450
    b = [title('进入、使用、离开三个时刻')]
    cols = [('进入', ['知道自己接受了什么', '有没有别的选择'],
             ['免费试用把门槛降到零，', '退出代价写在很后面']),
            ('使用', ['看得见系统在做什么', '能限制它的权力', '规则改变时能提出异议'],
             ['权限一次次扩大，', '只靠更新条款来通知']),
            ('离开', ['能带走自己的东西', '能恢复基本工作能力', '不因离开受不合理惩罚'],
             ['导出来的是一堆', '别处读不懂的文件'])]
    for i, (n, need, trap) in enumerate(cols):
        x = 40 + i * 285
        w = 255
        b.append(f'<rect x="{x}" y="70" width="{w}" height="48" rx="6" fill="{INK}"/>')
        b.append(t(x + w / 2, 101, n, 18, 'middle', 'bold', fill='#fff'))
        if i < 2:
            b.append(line(x + w + 3, 94, x + 282, 94, sw=2))
        b.append(box(x, 130, w, 150))
        b.append(t(x + 18, 156, '要做到', 13, fill=MID))
        for j, s in enumerate(need):
            b.append(t(x + 18, 186 + j * 28, '· ' + s, 15))
        b.append(box(x, 292, w, 100, fill=FAINT, stroke=MID, dash='5 4'))
        b.append(t(x + 18, 318, '常见的坑', 13, fill=MID))
        for j, s in enumerate(trap):
            b.append(t(x + 18, 344 + j * 22, s, 14))
    b.append(t(40, 430, '离开也可能以另一种方式到来：系统自己坏了', 13, fill=MID))
    save('fig7-1_three_moments.svg', svg(W, H, '\n'.join(b)))


# 7-2 open layers
def fig7_2():
    W, H = 900, 640
    b = [title('开放的几个层次')]
    # rights row
    b.append(t(40, 80, '"开放"是一组权利，可以一项项拆开检查', 15, weight='bold'))
    rights = ['看', '在自己的机器上跑', '改', '再分发', '参与决定项目方向']
    ws = [90, 190, 90, 110, 200]
    x = 40
    for i, (r, w) in enumerate(zip(rights, ws)):
        b.append(box(x, 98, w, 46, fill='#fff'))
        b.append(t(x + w / 2, 127, r, 15, 'middle', 'bold'))
        x += w + 17
    # three forms (ch2)
    b.append(t(40, 192, '三种拿到模型的方式（见第二章）', 15, weight='bold'))
    forms = [('用云端接口', '像买产品', ['拿到的是结果', '设备在别人手里', '改价、换版本由厂商定'], '#fff'),
             ('拿到开放权重', '像买下一台机器', ['可以下载、运行、改装', '可以固定版本', '训练过程往往说不全'], '#e2e2e2'),
             ('更完整的开源', '连图纸和工艺一起给', ['训练代码、数据说明、', '中间版本也公开', '可以自己维护'], '#bdbdbd')]
    for i, (n, m, items, shade) in enumerate(forms):
        x = 40 + i * 280
        b.append(box(x, 208, 255, 160, fill=shade))
        b.append(t(x + 18, 238, n, 16, weight='bold'))
        b.append(t(x + 237, 238, m, 12, 'end', fill=MID))
        for j, s in enumerate(items):
            b.append(t(x + 18, 272 + j * 26, '· ' + s, 14))
        if i < 2:
            b.append(line(x + 257, 288, x + 278, 288))
    b.append(t(40, 396, '越往右，你能自己做的越多，要自己担的责任也越多', 13, fill=MID))
    # gap between right and ability
    b.append(box(40, 412, 820, 48, fill=FAINT, stroke=MID, dash='5 4'))
    b.append(t(450, 442, '拿到了复制的权利，离真正有复制的能力还很远（复现训练仍要大量算力和专业人员）', 13, 'middle'))
    # leave test
    b.append(t(40, 498, '检验开放算不算数：回到"离开"', 15, weight='bold'))
    qs = [['原维护者不干了，', '社区能接手发布和修复吗？'], ['换一个云平台，', '模型和工作流能继续跑吗？'],
          ['不同意主流路线的人，', '能在法律和技术上', '另起炉灶吗？']]
    for i, q in enumerate(qs):
        x = 40 + i * 280
        b.append(box(x, 514, 255, 90))
        y0 = 553 - (len(q) - 2) * 11
        for j, s in enumerate(q):
            b.append(t(x + 127, y0 + j * 22, s, 14, 'middle'))
    save('fig7-2_open_layers.svg', svg(W, H, '\n'.join(b)))


FIGS = (fig4_1, fig4_2, fig4_3, fig6_1, fig6_2, fig6_3, fig6_4, fig7_1, fig7_2)
if __name__ == '__main__':
    for f in FIGS:
        f()
