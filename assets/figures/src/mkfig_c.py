from mkfig import *
from mkfig_a import title, poly, path


def ml(x, y, lines, size=13, anchor='start', weight='normal', fill=INK, lh=None):
    lh = lh or size + 6
    return [t(x, y + i * lh, s, size, anchor, weight, fill) for i, s in enumerate(lines)]


def dark(x, y, w, h, s, size=15, rx=6):
    return [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{INK}"/>',
            t(x + w / 2, y + h / 2 + size * 0.35, s, size, 'middle', 'bold', fill='#fff')]


def num(cx, cy, n, r=11, size=12):
    return [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{INK}"/>',
            t(cx, cy + size * 0.36, str(n), size, 'middle', 'bold', fill='#fff')]


def bracket_down(x1, x2, y, h=10, stroke=MID):
    return path(f'M{x1},{y} v{h} H{x2} v{-h}', arrow=False, stroke=stroke, sw=1.2)


def edge(p, q, hw, hh):
    """Point on the border of a box centred at p (half sizes hw, hh) towards q."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    k = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
    return p[0] + dx * k, p[1] + dy * k


# 8-1 six things that can be opened
def fig8_1():
    W, H = 900, 450
    b = title('从源代码到六样可以开放的东西')
    b.append(box(40, 90, 170, 292, fill=FAINT))
    b.append(t(125, 120, '开源软件', 17, 'middle', 'bold'))
    b.append(box(65, 210, 120, 50, fill='#fff', sw=2))
    b.append(t(125, 241, '源代码', 16, 'middle', 'bold'))
    b += ml(125, 300, ['拿到源代码，', '基本就拿到了', '全部'], 13, 'middle', fill=MID)
    b.append(line(214, 236, 252, 236, sw=2))
    b.append(t(500, 80, '开源 AI：一个能干活的系统由几样东西组成', 13, 'middle', fill=MID))
    rows = [('代码', '可读、可改，自己能维护'),
            ('模型和权重', '可替换、可本地运行、可独立验证'),
            ('数据', '知识能沉淀，训练能复现，责任能追溯'),
            ('协议和接口', '降低平台锁定，方便组合和退出'),
            ('评测', '不必只信排行榜和厂商的说法'),
            ('运行方法', '让主权在系统运行时也成立')]
    for i, (n, v) in enumerate(rows):
        y = 92 + i * 50
        hl = (i == 1)
        b.append(box(260, y, 140, 42, fill=LIGHT if hl else '#fff', sw=2 if hl else 1.5))
        b.append(t(330, y + 27, n, 15, 'middle', 'bold'))
        b.append(t(415, y + 27, v, 14))
    b.append(bracket_down(0, 0, 0, 0) if False else '')
    b.append(path('M720,96 h10 V230 h-10', arrow=False, stroke=MID))
    b += ml(742, 150, ['《开源 AI 定义》', '要求公开代码、', '参数和数据信息'], 13, fill=MID)
    b.append(path('M720,246 h10 V380 h-10', arrow=False, stroke=MID))
    b += ml(742, 310, ['这三样', '常被忽视'], 13, fill=MID)
    b.append(t(40, 425, '今天大多数被叫作“开源模型”的东西，只开放了灰色那一行，准确的说法是开放权重模型', 13, fill=MID))
    save('fig8-1_open_ai_objects.svg', svg(W, H, '\n'.join(x for x in b if x)))


# 9-1 license spectrum
def fig9_1():
    W, H = 900, 540
    b = title('许可证光谱：从宽松许可到源代码可用')
    groups = [(40, 200, '宽松许可证', ['MIT', 'BSD', 'Apache 2.0'], '保留声明即可', '#fff'),
              (250, 180, '弱著佐权', ['LGPL', 'MPL 2.0'], '限于程序库或被改的文件', '#ececec'),
              (440, 180, '强著佐权', ['GPLv3', 'AGPLv3'], '衍生作品同样开放', '#d2d2d2'),
              (670, 190, '源代码可用', ['BSL', 'SSPL', 'RSAL'], '限制特定商业用途', '#fff')]
    centers = []
    for x, w, n, items, note, shade in groups:
        dash = '6 4' if n == '源代码可用' else ''
        b.append(box(x, 110, w, 150, fill=shade, dash=dash))
        b.append(t(x + w / 2, 138, n, 16, 'middle', 'bold'))
        for j, s in enumerate(items):
            b.append(t(x + w / 2, 168 + j * 22, s, 14, 'middle'))
        b.append(t(x + w / 2, 248, note, 12, 'middle', fill=MID))
        centers.append(x + w / 2)
    b.append(path('M40,100 v-8 H620 v8', arrow=False, stroke=MID, sw=1.2))
    b.append(t(330, 86, 'OSI 认可的开源许可证', 13, 'middle', 'bold'))
    b.append(t(765, 92, '不属于开源', 13, 'middle', 'bold'))
    b.append(line(645, 100, 645, 270, arrow=False, stroke=MID, dash='4 4'))
    b.append(line(40, 284, 618, 284, sw=1.5))
    b.append(t(40, 304, '对衍生作品“同样开放”的要求越来越强 →', 13, fill=MID))
    # license changes
    b.append(t(40, 344, '几次改许可证', 14, weight='bold'))
    rows = [(372, centers[1], centers[3], 'Terraform', '二〇二三年　MPL 2.0 → BSL'),
            (412, centers[0], centers[3], 'Redis', '二〇二四年　BSD → RSALv2／SSPL'),
            (452, centers[3], centers[2], 'Redis 8', '二〇二五年　加上 AGPLv3')]
    for y, x1, x2, n, lab in rows:
        b.append(f'<circle cx="{x1}" cy="{y}" r="4" fill="{INK}"/>')
        b.append(line(x1, y, x2 + (-6 if x2 > x1 else 6), y, sw=1.5))
        b.append(t((x1 + x2) / 2, y - 7, lab, 12, 'middle'))
        b.append(t(x1 - 12 if x2 > x1 else x1 + 12, y + 5, n, 13, 'end' if x2 > x1 else 'start', 'bold'))
    b.append(box(40, 482, 400, 40, fill=FAINT, stroke=MID))
    b.append(t(240, 507, '内容和数据：CC0 · CC BY · CC BY-SA', 13, 'middle'))
    b.append(box(460, 482, 400, 40, fill=FAINT, stroke=MID))
    b.append(t(660, 507, '大模型：厂商自定义的开放权重许可，差别很大', 13, 'middle'))
    save('fig9-1_license_spectrum.svg', svg(W, H, '\n'.join(b)))


# 10-1 sovereign data loop
def fig10_1():
    import math
    W, H = 900, 520
    b = title('主权数据闭环')
    cx, cy, rx, ry = 450, 285, 330, 168
    nodes = ['采集', '授权', '清洗', '标注', '版本登记', '使用', '评测', '反馈', '治理']
    pts = []
    for i in range(len(nodes)):
        a = math.radians(-90 + i * 40)
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    hw, hh = 58, 21
    for i, (n, p) in enumerate(zip(nodes, pts)):
        q = pts[(i + 1) % len(pts)]
        s = edge(p, q, hw + 3, hh + 3)
        e = edge(q, p, hw + 6, hh + 6)
        b.append(line(s[0], s[1], e[0], e[1], sw=1.5))
    for i, (n, p) in enumerate(zip(nodes, pts)):
        last = (i == len(nodes) - 1)
        b.append(box(p[0] - hw, p[1] - hh, hw * 2, hh * 2, fill=LIGHT if last else '#fff', sw=2 if last else 1.5))
        b.append(t(p[0], p[1] + 6, n, 15, 'middle', 'bold'))
    tp = pts[-1]
    b.append(t(tp[0], tp[1] - 30, '决定更新、限制还是删除', 12, 'middle', fill=MID))
    b.append(t(cx, cy - 66, '每一次使用都说得清', 16, 'middle', 'bold'))
    b += ml(cx, cy - 34, ['谁在用', '为了什么任务', '凭什么权限', '留下了什么记录', '用完以后能不能撤回'], 14, 'middle', lh=24)
    b.append(t(40, 505, '出了事，查得出一份数据进了哪些训练集、索引和评测集，被哪些智能体在哪些任务里用过', 13, fill=MID))
    save('fig10-1_data_loop.svg', svg(W, H, '\n'.join(b)))


# 10-2 data flywheel
def fig10_2():
    W, H = 900, 470
    b = title('数据飞轮：失败记录变成评测题')
    def node(x, y, w, h, name, subl, fill='#fff', sw=1.5):
        r = [box(x, y, w, h, fill=fill, sw=sw), t(x + w / 2, y + 26, name, 15, 'middle', 'bold')]
        r.append(t(x + w / 2, y + 47, subl, 12, 'middle', fill=MID))
        return r
    b += node(60, 90, 160, 62, '真实任务', '系统每天处理的活')
    b += node(290, 90, 200, 62, '留下一条轨迹', '请求、资料、工具、结果')
    b += node(560, 90, 280, 62, '员工采用、修改或推翻', '被推翻和修改的最值钱', fill=FAINT)
    b += node(60, 230, 300, 62, '改进', '知识库 · 工具 · 权限 · 路由 · 模型', fill=LIGHT, sw=2)
    b += node(430, 230, 190, 62, '评测集', '出错案例，下次先测一遍')
    b += node(660, 230, 180, 62, '反馈', '员工的修改，带着判断')
    b.append(line(222, 121, 287, 121))
    b.append(line(492, 121, 557, 121))
    b.append(line(620, 154, 560, 227))
    b.append(line(750, 154, 750, 227))
    b.append(line(428, 261, 363, 261))
    b.append(path('M750,294 V318 H300 V297'))
    b.append(line(140, 228, 140, 155))
    b.append(t(150, 196, '再回到真实任务', 12, fill=MID))
    b.append(t(372, 360 - 50, '每次改动都有记录，改坏了能退回去', 12, fill=MID))
    b.append(box(40, 345, 400, 54, fill='#fff'))
    b += ml(240, 367, ['评测集、知识库、反馈记录在自己手里：', '换了模型照样能用'], 13, 'middle')
    b.append(box(460, 345, 400, 54, fill='#fff', stroke=MID, dash='6 4'))
    b += ml(660, 367, ['只存在供应商平台上，或者默默回流：', '飞轮转得再快，积累也在别人那边'], 13, 'middle', fill=MID)
    b.append(t(40, 440, '两个前提：员工愿意纠正，并把改过的地方留在系统里；采集要克制，先脱敏，写清保留期限', 13, weight='bold'))
    save('fig10-2_data_flywheel.svg', svg(W, H, '\n'.join(b)))


# 11-1 routing and standby
def fig11_1():
    W, H = 900, 520
    b = title('按任务派活，备用模型平时就上岗')
    b.append(box(40, 165, 90, 50, fill=FAINT))
    b.append(t(85, 196, '请求', 15, 'middle', 'bold'))
    b.append(line(132, 190, 178, 190))
    b.append(box(180, 140, 160, 100, sw=2))
    b.append(t(260, 178, '多模型路由', 16, 'middle', 'bold'))
    b += ml(260, 202, ['先判断难度', '和敏感程度'], 12, 'middle', fill=MID, lh=17)
    outs = [(95, '简单', '便宜的小模型'), (168, '敏感', '留在本地的模型'), (241, '难', '闭源前沿模型')]
    for y, lab, n in outs:
        b.append(line(342, 190, 548, y + 22))
        ly = 190 + (y + 22 - 190) * (470 - 342) / (548 - 342)
        b.append(t(470, ly - 8 if y <= 168 else ly + 20, lab, 13, 'middle', 'bold'))
        b.append(box(550, y, 190, 44))
        b.append(t(645, y + 28, n, 14, 'middle'))
    b.append(t(760, 150, '某个模型出故障：', 12, fill=MID))
    b.append(t(760, 168, '自动降级', 12, fill=MID))
    b.append(t(760, 194, '慢一点、粗糙一点，', 12, fill=MID))
    b.append(t(760, 212, '安全规则不松', 12, fill=MID))
    b.append(line(40, 305, 860, 305, arrow=False, stroke=LIGHT, dash='6 5'))
    b.append(t(40, 335, '一项关键业务', 14, weight='bold'))
    b.append(box(40, 352, 120, 70, fill=FAINT))
    b.append(t(100, 393, '真实流量', 14, 'middle', 'bold'))
    b.append(line(162, 375, 256, 357, sw=5))
    b.append(line(162, 400, 256, 420, sw=1.5))
    b.append(box(260, 335, 210, 44, sw=2))
    b.append(t(365, 363, '主模型　大部分流量', 14, 'middle', 'bold'))
    b.append(box(260, 400, 210, 44))
    b.append(t(365, 428, '备用模型　一小部分', 14, 'middle'))
    b.append(box(560, 340, 300, 100, fill=FAINT))
    b.append(t(710, 372, '和具体模型无关的评测集', 15, 'middle', 'bold'))
    b += ml(710, 398, ['企业自己的资产', '主模型每次升级，主备一起测'], 12, 'middle', fill=MID, lh=18)
    b.append(line(558, 375, 474, 357, dash='4 3', sw=1.2))
    b.append(line(558, 405, 474, 422, dash='4 3', sw=1.2))
    b.append(t(40, 490, '每个季度挑一个工作日，把一项业务的全部流量切到备用模型跑半天，记下质量、成本和投诉的变化', 13, fill=MID))
    save('fig11-1_model_routing.svg', svg(W, H, '\n'.join(b)))


# 12-1 common layer and difference layer
def fig12_1():
    W, H = 900, 470
    b = title('公共层交给社区，差异层留给自己')
    b.append(box(40, 85, 820, 120, fill=FAINT))
    b.append(t(60, 115, '公共层', 17, weight='bold'))
    b.append(t(130, 115, '社区共同维护，中立基金会托管，共享接口和标准', 13, fill=MID))
    for i, s in enumerate(['训练和推理框架', '模型和数据的格式', '智能体接入工具的协议', '基础的评测工具']):
        x = 60 + i * 198
        b.append(box(x, 135, 182, 50))
        b.append(t(x + 91, 166, s, 14, 'middle'))
    b.append(box(40, 305, 820, 120))
    b.append(t(60, 335, '差异层', 17, weight='bold'))
    b.append(t(130, 335, '各家自己的东西，各自竞争，各自保护', 13, fill=MID))
    for i, s in enumerate(['业务规则', '客户资料', '领域数据', '内部评测集', '流程']):
        x = 60 + i * 158
        b.append(box(x, 355, 146, 50, fill=LIGHT))
        b.append(t(x + 73, 386, s, 14, 'middle', 'bold'))
    # take
    b.append(line(300, 207, 300, 228))
    b.append(box(220, 230, 160, 48, sw=2))
    b.append(t(300, 252, '内部镜像仓库', 14, 'middle', 'bold'))
    b.append(t(300, 270, '固定版本和哈希值', 12, 'middle', fill=MID))
    b.append(line(300, 280, 300, 302))
    b.append(t(205, 260, '取能力', 14, 'end', 'bold'))
    b.append(t(395, 252, '平台出事、被收购', 12, fill=MID))
    b.append(t(395, 270, '或改规则时的退路', 12, fill=MID))
    # give back
    b.append(line(700, 302, 700, 208))
    b.append(t(715, 240, '回馈', 14, weight='bold'))
    b.append(t(715, 260, '提交修复 · 公开工具', 12, fill=MID))
    b.append(t(715, 278, '资助维护 · 参与治理', 12, fill=MID))
    b.append(t(40, 455, 'PyTorch 和 MCP 交给基金会，就是把公共层交给社区；回馈可以看成给退路交的保险费', 13, fill=MID))
    save('fig12-1_common_layer.svg', svg(W, H, '\n'.join(b)))


# 13-1 four-layer fractal
def fig13_1():
    W, H = 900, 510
    b = title('四层主权，同一个图案')
    layers = [('国家', '靠什么保持韧性', '#fff'), ('城市', '怎样把机房变成能力', '#f0f0f0'),
              ('企业', '哪些资产不能随供应商走掉', '#dedede'), ('个人', '换了工具、丢了账号还能接着工作', '#c8c8c8')]
    for i, (n, q, shade) in enumerate(layers):
        x, y = 40 + i * 30, 80 + i * 62
        w, h = 500 - i * 60, 370 - i * 82
        b.append(box(x, y, w, h, fill=shade, sw=2 if i == 0 else 1.5))
        b.append(t(x + 16, y + 30, n, 17, weight='bold'))
        b.append(t(x + 62, y + 30, q, 13))
    b.append(line(545, 260, 588, 260, arrow=True))
    b.append(box(590, 80, 270, 190, fill=FAINT))
    b.append(t(610, 110, '每一层都要回答', 15, weight='bold'))
    for i, q in enumerate(['它能看到什么', '它能做什么', '谁能让它停下', '出了事谁负责']):
        b += num(622, 140 + i * 32 - 5, i + 1, r=10)
        b.append(t(642, 140 + i * 32, q, 14))
    b.append(box(590, 290, 270, 160))
    b.append(t(610, 320, '每一层都要经受', 15, weight='bold'))
    for i, s in enumerate(['选择', '替换', '迁移', '审计', '组合', '演进']):
        r, c = divmod(i, 3)
        x, y = 610 + c * 80, 342 + r * 48
        b.append(box(x, y, 70, 36, fill='#fff'))
        b.append(t(x + 35, y + 24, s, 14, 'middle', 'bold'))
    b.append(t(40, 476, '镜头拉近或拉远，看到的图案相似', 13, weight='bold'))
    b.append(t(40, 498, '国家、城市、企业、个人手里的资源差得很远，要回答的问题几乎一样', 13, fill=MID))
    save('fig13-1_four_layers.svg', svg(W, H, '\n'.join(b)))


# 13-2 six faces of national AI capability
def fig13_2():
    W, H = 900, 460
    b = title('国家 AI 能力的六个面')
    b.append(t(40, 66, '每一面都写下：依赖谁，断了以后多久能补上', 13, fill=MID))
    faces = [('能源', ['决定能拿到', '多少算力和', 'Token 成本']),
             ('算力', ['决定能生产', '多少智能']),
             ('高质量数据', ['本国的语言、', '经济和公共服务', '能否被模型理解']),
             ('模型', ['提供通用和', '专业能力']),
             ('智能体', ['能否进工厂、', '医院和政务', '大厅去办事']),
             ('开放生态与人才', ['前五样能否', '持续改进'])]
    for i, (n, d) in enumerate(faces):
        x = 40 + i * 138
        b.append(box(x, 85, 126, 140))
        b.append(t(x + 63, 113, n, 15 if len(n) < 6 else 13, 'middle', 'bold'))
        b += ml(x + 63, 145, d, 12, 'middle', lh=18)
        for j, q in enumerate(['依赖谁？', '断了多久补上？']):
            b.append(box(x, 233 + j * 30, 126, 24, fill='#fff', stroke=MID, sw=1, dash='3 3', rx=3))
            b.append(t(x + 63, 250 + j * 30, q, 12, 'middle', fill=MID))
    b.append(t(40, 325, '韧性：没有一处断了就全停', 16, weight='bold'))
    res = [('芯片受到限制', ['有替代的芯片，', '也有移植模型的', '工程能力']),
           ('云服务改条款或停服', ['关键系统', '迁得走']),
           ('前沿模型来自外国', ['本地仍能评测、', '部署、治理数据、', '做业务集成']),
           ('公共系统出了错', ['有审计、有申诉，', '也有人能接管'])]
    for i, (c, r) in enumerate(res):
        x = 40 + i * 207
        b.append(box(x, 340, 192, 100))
        b.append(t(x + 96, 364, c, 14, 'middle', 'bold'))
        b.append(line(x + 16, 374, x + 176, 374, arrow=False, stroke=LIGHT, sw=1))
        b += ml(x + 96, 394, r, 12, 'middle', lh=17)
    save('fig13-2_six_faces.svg', svg(W, H, '\n'.join(b)))


# 14-1 city data space by domains
def fig14_1():
    W, H = 900, 520
    b = title('分域的城市数据空间')
    b.append(t(40, 66, '数据留在原来的部门，城市统一管身份、目录、授权和审计', 13, fill=MID))
    doms = ['政务', '交通', '文旅', '招商', '医疗', '教育', '工业']
    for i, d in enumerate(doms):
        x = 40 + i * 117
        b.append(box(x, 95, 108, 72, fill=FAINT if i == 1 else '#fff', sw=2 if i == 1 else 1.5))
        b.append(t(x + 54, 125, d, 16, 'middle', 'bold'))
        b.append(t(x + 54, 151, '数据留在本域', 12, 'middle', fill=MID))
    b.append(box(40, 235, 812, 58, fill=LIGHT))
    b.append(t(446, 270, '城市统一提供：身份 · 目录 · 授权 · 审计 · 数据标准', 16, 'middle', 'bold'))
    xd = 40 + 117 + 54
    b.append(line(xd - 8, 233, xd - 8, 171))
    b.append(line(xd + 8, 171, xd + 8, 231, dash='4 3'))
    b.append(t(xd + 20, 200, '授权后按需取用，只交回所需结果', 12, fill=MID))
    b.append(box(300, 345, 200, 56, sw=2))
    b.append(t(400, 379, '智能体办一件事', 15, 'middle', 'bold'))
    b.append(line(400, 343, 400, 296))
    b.append(t(410, 324, '申请', 12, fill=MID))
    b.append(box(560, 345, 292, 56, fill=FAINT, stroke=MID))
    b.append(t(706, 368, '留下记录', 13, 'middle', 'bold'))
    b.append(t(706, 389, '用了多少、用来做什么、谁批准的', 12, 'middle'))
    b.append(line(502, 373, 557, 373, sw=1.2))
    b.append(t(40, 440, '数据空间也要能退出', 14, weight='bold'))
    b.append(box(40, 452, 400, 50, fill='#fff', stroke=MID, dash='6 4'))
    b.append(t(240, 482, '运营方换了：目录、授权记录、日志、标准完整交接', 13, 'middle'))
    b.append(box(452, 452, 400, 50, fill='#fff', stroke=MID, dash='6 4'))
    b.append(t(652, 482, '部门不再参加：数据撤出，相关服务随之调整', 13, 'middle'))
    save('fig14-1_city_data_space.svg', svg(W, H, '\n'.join(b)))


# 15-1 seven control points
def fig15_1():
    W, H = 900, 380
    b = title('企业主权架构的七个控制点')
    b.append(t(40, 66, '智能体代表企业说话、办事，责任就落在企业身上', 13, fill=MID))
    pts = [(1, '身份', ['代表员工、', '部门，还是', '公司对外']),
           (2, '数据', ['每次访问', '有边界、', '有目的']),
           (4, '工具', ['参数要校验，', '权限压到', '最小']),
           (5, '预算', ['每项任务', '有成本上限']),
           (6, '轨迹', ['证据留在', '智能体改不了', '的地方']),
           (3, '模型', ['能评测、', '能路由、', '能替换']),
           (7, '退出', ['数据、配置、', '工作流', '都能带走'])]
    xs = [40, 154, 268, 382, 520, 658, 772]
    for (n, name, d), x in zip(pts, xs):
        b.append(box(x, 95, 106, 150, fill=FAINT if name in ('轨迹',) else '#fff'))
        b += num(x + 22, 118, n)
        b.append(t(x + 62, 123, name, 16, 'middle', 'bold'))
        b.append(line(x + 12, 138, x + 94, 138, arrow=False, stroke=LIGHT, sw=1))
        b += ml(x + 53, 162, d, 12, 'middle', lh=19)
    groups = [(40, 488, '决定智能体做什么'), (520, 626, '审计'), (658, 878, '选择、替换和迁移')]
    for x1, x2, lab in groups:
        b.append(bracket_down(x1, x2, 255))
        b.append(t((x1 + x2) / 2, 290, lab, 14, 'middle', 'bold'))
    b.append(t(450, 320, '对应第三章的六种能力', 12, 'middle', fill=MID))
    b.append(t(40, 360, '不必一次建齐：从风险最高的那个流程开始，一个控制点一个控制点地补', 13, fill=MID))
    save('fig15-1_seven_control_points.svg', svg(W, H, '\n'.join(b)))


# 16-1 digital continuity and brakes
def fig16_1():
    W, H = 900, 450
    b = title('带得走的四类资产，装在手边的几处刹车')
    b.append(t(40, 80, '数字连续性：要随身带走的', 15, weight='bold'))
    assets = [('原始资料', '通用格式另存一份，放在服务商够不着的地方'),
              ('知识和记忆', '写成自己看得懂的笔记，不只存在助手里'),
              ('做事的方法', '提示词、工作流程、技能和工具设置'),
              ('“我怎样工作”', '一页任务说明，换人换助手看完就能上手')]
    for i, (n, d) in enumerate(assets):
        y = 95 + i * 62
        b.append(box(40, y, 400, 52, fill=FAINT if i == 0 else '#fff'))
        b += num(62, y + 26, i + 1)
        b.append(t(84, y + 22, n, 15, weight='bold'))
        b.append(t(84, y + 42, d, 12, fill=MID))
    b.append(t(40, 365, '法律上的数据可携带权，主要管第 1 类', 12, fill=MID))
    b.append(box(40, 378, 400, 50, fill='#fff', stroke=MID, dash='6 4'))
    b.append(t(240, 400, '身份和关系最难打包', 14, 'middle', 'bold'))
    b.append(t(240, 419, '前三类保管好，关系断了还有重建的材料', 12, 'middle', fill=MID))
    b.append(line(465, 80, 465, 430, arrow=False, stroke=LIGHT, dash='6 5'))
    b.append(t(490, 80, '一人公司的刹车', 15, weight='bold'))
    brakes = [('试验环境和生产数据分开', '智能体随便折腾，碰不到真实客户和账目'),
              ('备份放在智能体够不着的地方', '删得掉线上的，删不掉离线副本'),
              ('付款、签约、删除、对外发布本人确认', '靠权限设置保证，不靠提示词里的一句话'),
              ('停止的办法在手边', '最好能一键收回全部授权'),
              ('每个关键账户有替代方案', '邮箱、收款、网盘、主力模型')]
    for i, (n, d) in enumerate(brakes):
        y = 95 + i * 66
        b.append(f'<rect x="490" y="{y}" width="8" height="52" fill="{INK}"/>')
        b.append(t(512, y + 20, n, 14, weight='bold'))
        b.append(t(512, y + 42, d, 12, fill=MID))
    save('fig16-1_continuity_brakes.svg', svg(W, H, '\n'.join(b)))


# 17-1 reference architecture
def fig17_1():
    W, H = 900, 480
    b = title('四层参考架构：从学会、运行、拥有到编排')
    layers = [('编排', '控制面', 'Control Plane', 'AgenticHub', ['多个智能体的身份、权限、', '工具和协作由谁统一管']),
              ('拥有', '资产中枢', 'Asset Hub', 'CSGHub', ['模型、数据、提示词、评测', '沉淀在哪里，能不能带走']),
              ('运行', '运行时', 'Runtime', 'CSGClaw', ['智能体在受控环境里动手，', '动手的范围在哪里']),
              ('学会', '能力入口', 'Capability Entry', 'CSGLite', ['低门槛地试用、比较、', '获得 AI 能力'])]
    shades = ['#c8c8c8', '#dcdcdc', '#ececec', '#fff']
    for i, (step, n, en, prod, q) in enumerate(layers):
        y = 90 + i * 76
        b.append(box(160, y, 600, 64, fill=shades[i], sw=2 if i == 1 else 1.5))
        b += dark(172, y + 16, 48, 32, step, 14, rx=4)
        b.append(t(234, y + 29, n, 16, weight='bold'))
        b.append(t(234, y + 49, en, 12, fill=MID))
        b.append(box(370, y + 12, 140, 40, fill='#fff', sw=2))
        b.append(t(440, y + 38, prod, 15, 'middle', 'bold'))
        b += ml(525, y + 28, q, 12, lh=18)
    b.append(t(440, 90 + 76 + 62, '', 1))
    # community
    b.append(box(40, 166, 100, 64, fill=FAINT, stroke=MID))
    b.append(t(90, 192, '公共社区', 14, 'middle', 'bold'))
    b.append(t(90, 212, '模型、数据集', 11, 'middle', fill=MID))
    b.append(line(142, 198, 157, 198))
    b.append(t(90, 248, '多源同步', 12, 'middle', fill=MID))
    b.append(t(90, 264, '进私有仓库', 12, 'middle', fill=MID))
    # AgenticOps
    b.append(box(778, 90, 82, 292, fill=FAINT, sw=2))
    b.append(t(819, 130, 'Agentic', 13, 'middle', 'bold'))
    b.append(t(819, 148, 'Ops', 13, 'middle', 'bold'))
    b += ml(819, 190, ['贯穿', '四层', '', '发布', '运行', '改进'], 13, 'middle', lh=22)
    b.append(t(40, 420, '模型提供智能，运行装置（Harness）提供行动能力，AgenticOps 提供可控运行', 14, weight='bold'))
    b.append(t(40, 448, '检验是不是真的分了层：挑一层换掉，看另外几层要不要跟着重写', 13, fill=MID))
    save('fig17-1_reference_architecture.svg', svg(W, H, '\n'.join(b)))


# 18-1 asset repository
def fig18_1():
    W, H = 900, 470
    b = title('资产仓库要答上的四个问题')
    srcs = ['公共社区', '供应商交付', '自己微调']
    for i, s in enumerate(srcs):
        y = 110 + i * 80
        b.append(box(40, y, 130, 50, fill=FAINT, stroke=MID))
        b.append(t(105, y + 31, s, 14, 'middle'))
        b.append(line(172, y + 25, 226, 220 + (i - 1) * 40))
    b.append(t(105, 360, '多源同步时', 12, 'middle', fill=MID))
    b.append(t(105, 377, '断点续传、校验完整性', 12, 'middle', fill=MID))
    b.append(box(230, 90, 270, 290, sw=2))
    b.append(t(365, 120, '资产仓库', 17, 'middle', 'bold'))
    items = ['模型', '数据集', '代码', '应用空间', '提示词', 'MCP 服务']
    for i, s in enumerate(items):
        r, c = divmod(i, 2)
        x, y = 250 + c * 120, 138 + r * 52
        b.append(box(x, y, 110, 42, fill=LIGHT if i < 2 else '#fff'))
        b.append(t(x + 55, y + 27, s, 14, 'middle', 'bold' if i < 2 else 'normal'))
    b.append(line(250, 302, 480, 302, arrow=False, stroke=LIGHT, sw=1))
    b.append(t(365, 326, '模型卡 · 模型树 · 下载记录', 12, 'middle', fill=MID))
    b.append(t(365, 348, '细到单个资产的权限', 12, 'middle', fill=MID))
    b.append(t(365, 368, '模型网关：多个上游，故障切换', 12, 'middle', fill=MID))
    b.append(box(540, 90, 320, 136, fill=FAINT))
    for i, q in enumerate(['有哪些 AI 资产？', '每一样从哪里来？', '谁能用？', '哪个版本正在生产环境里跑？']):
        b += num(562, 118 + i * 28 - 5, i + 1, r=10)
        b.append(t(582, 118 + i * 28, q, 14))
    b.append(t(540, 254, '答得上来，四种能力就有了着落', 13, weight='bold'))
    caps = [('有版本', '能回滚', '演进'), ('有元数据', '', '审计'),
            ('有标准接口', '', '组合'), ('不绑一家供应商', '', '迁移')]
    for i, (a, m, c) in enumerate(caps):
        y = 270 + i * 28
        b.append(t(540, y + 14, a, 13))
        b.append(t(668, y + 14, m, 13, fill=MID))
        b.append(line(718, y + 9, 760, y + 9, sw=1.2))
        b.append(t(770, y + 14, c, 14, weight='bold'))
    b.append(box(40, 400, 820, 50, fill='#fff', stroke=MID, dash='6 4'))
    b.append(t(450, 422, '仓库证明不了模型本身安全、输出正确，这些仍要靠独立测试', 13, 'middle'))
    b.append(t(450, 441, '私有仓库装好以后没人维护，过两年会变成新的孤岛', 12, 'middle', fill=MID))
    save('fig18-1_asset_repository.svg', svg(W, H, '\n'.join(b)))


# 19-1 CSGLite and CSGClaw
def fig19_1():
    W, H = 900, 500
    b = title('本地与云端并存，一个人带一支智能体团队')
    # left panel
    b.append(t(40, 86, 'CSGLite：本地推理', 15, weight='bold'))
    b.append(box(120, 104, 240, 44))
    b.append(t(240, 131, '按 OpenAI 格式写好的应用', 14, 'middle'))
    b.append(line(240, 150, 240, 178))
    b.append(box(120, 180, 240, 44, fill=LIGHT, sw=2))
    b.append(t(240, 207, '本机的兼容接口', 14, 'middle', 'bold'))
    b.append(line(200, 226, 135, 268))
    b.append(line(280, 226, 345, 268))
    b.append(t(240, 256, '改指向，代码不用重写', 12, 'middle', fill=MID))
    for x, n, d in ((40, '本地小模型', ['资料涉及隐私', '要求响应快', '没网的地方', '固定、重复量大']),
                    (250, '云端模型', ['复杂推理', '长篇写作', '少见的专业问题'])):
        b.append(box(x, 270, 190, 140, fill=FAINT if x == 40 else '#fff'))
        b.append(t(x + 95, 296, n, 15, 'middle', 'bold'))
        b += ml(x + 95, 324, d, 13, 'middle', lh=21)
    b.append(t(40, 440, '它回答“它能看到什么”：', 12, fill=MID))
    b.append(t(40, 458, '放在本地处理的资料不出门', 12, fill=MID))
    b.append(line(465, 80, 465, 480, arrow=False, stroke=LIGHT, dash='6 5'))
    # right panel
    b.append(t(490, 86, 'CSGClaw：个人 AI 团队的运行时', 15, weight='bold'))
    b.append(box(590, 104, 170, 44, fill=LIGHT, sw=2))
    b.append(t(675, 131, '你：由你做决定', 14, 'middle', 'bold'))
    b.append(line(675, 150, 675, 176))
    b.append(box(560, 178, 230, 56))
    b.append(t(675, 201, '主管智能体', 15, 'middle', 'bold'))
    b.append(t(675, 222, '拆分任务 · 挑执行者 · 跟进 · 汇总', 12, 'middle', fill=MID))
    names = ['前端', '后端', '测试', '文档']
    for i, n in enumerate(names):
        x = 490 + i * 93
        b.append(line(675, 236, x + 42, 268, sw=1.2))
        b.append(box(x, 270, 84, 70, fill='none', stroke=MID, dash='4 3', rx=4))
        b.append(box(x + 10, 290, 64, 36))
        b.append(t(x + 42, 313, n, 13, 'middle'))
        b.append(t(x + 42, 284, '沙箱', 10, 'middle', fill=MID))
    b.append(t(490, 362, '每个执行者默认在隔离的 Docker 沙箱里干活', 12, fill=MID))
    b.append(t(490, 382, '入口：浏览器工作台 · 飞书 · 微信 · Matrix', 12, fill=MID))
    b.append(box(490, 400, 370, 64, fill='#fff', stroke=MID, dash='6 4'))
    b.append(t(675, 424, '截至二〇二六年十月，说明文件还没写到', 12, 'middle', fill=MID))
    b.append(t(675, 446, '细粒度授权 · 人工确认 · 断点恢复 · 整体导出', 13, 'middle', 'bold'))
    save('fig19-1_local_and_team.svg', svg(W, H, '\n'.join(b)))


# 20-1 task and connections
def fig20_1():
    W, H = 900, 500
    b = title('智能体按任务来管，连接按登记来管')
    b.append(box(40, 90, 270, 280))
    b += dark(40, 90, 270, 40, '一项任务', 15)
    rows = [('谁发起，代表谁', []), ('房卡', ['能进哪个系统、做哪些操作、', '有效期到哪天、能不能转交']),
            ('任务单', ['做到什么程度算完、谁验收、', '能用哪些工具、金额和次数上限']),
            ('停下找人', ['碰到什么情况要回来问人'])]
    y = 158
    for k, v in rows:
        b.append(t(56, y, k, 14, weight='bold'))
        b += ml(56, y + 20, v, 12, fill=MID, lh=18)
        y += 34 + 18 * len(v)
    b.append(line(312, 230, 368, 230))
    b.append(t(340, 220, '领卡', 12, 'middle', fill=MID))
    b.append(box(370, 180, 170, 100, fill=LIGHT, sw=2))
    b.append(t(455, 214, '智能体', 16, 'middle', 'bold'))
    b.append(t(455, 238, '工作流里放确认点', 12, 'middle'))
    b.append(t(455, 258, '在沙箱里执行', 12, 'middle'))
    # MCP
    b.append(box(610, 100, 110, 56, sw=2))
    b.append(t(665, 133, 'MCP 网关', 14, 'middle', 'bold'))
    b.append(line(520, 178, 608, 140))
    b.append(t(560, 148, 'MCP', 12, 'middle', 'bold'))
    for i, s in enumerate(['工具', '数据源']):
        b.append(box(770, 90 + i * 44, 90, 36))
        b.append(t(815, 113 + i * 44, s, 13, 'middle'))
        b.append(line(722, 128, 768, 108 + i * 44, sw=1.2))
    # A2A
    b.append(box(640, 250, 150, 46))
    b.append(t(715, 278, '其他智能体', 14, 'middle'))
    b.append(line(542, 260, 637, 270))
    b.append(line(637, 282, 542, 272))
    b.append(t(590, 300, 'A2A', 12, 'middle', 'bold'))
    b.append(t(590, 316, '分工、交接', 11, 'middle', fill=MID))
    b.append(box(370, 330, 490, 40, fill=FAINT, stroke=MID, dash='5 4'))
    b.append(t(615, 355, '登记每一根线：来源、版本、谁批准、哪些智能体能调、用谁的身份', 12, 'middle'))
    b.append(t(40, 410, '智能体的一生', 14, weight='bold'))
    life = ['登记上线', '运行和监控', '定期复审', '退役']
    for i, s in enumerate(life):
        x = 40 + i * 150
        b.append(box(x, 424, 128, 40, fill=LIGHT if i == 3 else '#fff'))
        b.append(t(x + 64, 449, s, 14, 'middle', 'bold' if i == 3 else 'normal'))
        if i < 3:
            b.append(line(x + 130, 444, x + 148, 444))
    b += ml(640, 438, ['撤销身份，关掉接口，', '解除下游依赖，把经验带回来'], 12, fill=MID, lh=18)
    save('fig20-1_task_and_connections.svg', svg(W, H, '\n'.join(b)))


# 21-1 value chain and three conditions
def fig21_1():
    W, H = 900, 470
    b = title('Token 工厂的价值链和三个条件')
    chain = ['能源', '算力', '模型', 'Token', '智能体', '任务', '验证过的结果']
    shades = ['#fff', '#fff', '#fff', '#fff', '#ececec', '#dcdcdc', '#bdbdbd']
    for i, s in enumerate(chain):
        x = 40 + i * 119
        b.append(box(x, 90, 102, 56, fill=shades[i], sw=2 if i == 6 else 1.5))
        b.append(t(x + 51, 124, s, 15 if i < 6 else 13, 'middle', 'bold'))
        if i < 6:
            b.append(line(x + 104, 118, x + 117, 118, sw=1.2))
    b.append(path('M40,178 H856', arrow=True, sw=1.5))
    b.append(t(40, 170, '← 越容易计量，也越容易被当成目标本身', 12, fill=MID))
    b.append(t(856, 170, '越接近业务价值 →', 12, 'end', fill=MID))
    b.append(bracket_down(40, 499, 190))
    b.append(t(270, 222, '城市报多少 P、企业报多少亿 Token，都停在这半段', 12, 'middle'))
    b.append(bracket_down(516, 856, 190))
    b.append(t(686, 222, '客户最终要买：完成了、验过了的任务', 12, 'middle'))
    b.append(t(40, 268, '主权 Token 工厂的三个条件', 16, weight='bold'))
    conds = [('多源', ['算力和模型不止一个来源，', '替代路径演练过'], '对应：选择、替换'),
             ('可计量', ['Token、工具调用、人工复核、', '成功率和业务结果进同一本账'], '对应：审计，出了事谁负责'),
             ('可治理', ['数据边界、版本、权限、', '轨迹和退出都能审计'], '检验：几年后本地留下了什么')]
    for i, (n, d, m) in enumerate(conds):
        x = 40 + i * 282
        b.append(box(x, 285, 255, 125))
        b.append(t(x + 18, 314, n, 17, weight='bold'))
        b += ml(x + 18, 342, d, 13, lh=20)
        b.append(t(x + 18, 396, m, 12, fill=MID))
        if i < 2:
            b.append(t(x + 268, 352, '＋', 18, 'middle', 'bold'))
    b.append(t(40, 448, '三条同时满足才算主权基础设施；只满足一两条，它可能是一个效率很高的新集中依赖点', 13, fill=MID))
    save('fig21-1_token_factory.svg', svg(W, H, '\n'.join(b)))


# 22-1 enterprise hub blueprint
def fig22_1():
    W, H = 900, 440
    b = title('企业主权 AI 中枢：四样东西，三个验收动作')
    b.append(t(40, 82, '第一阶段只挑三项真实任务，例如', 13, fill=MID))
    for i, s in enumerate(['内部知识问答', '研发辅助', '客户服务', '合同审查']):
        x = 40 + i * 132
        b.append(box(x, 94, 120, 42, fill=FAINT, stroke=MID))
        b.append(t(x + 60, 120, s, 13, 'middle'))
    b.append(line(300, 140, 300, 168))
    b.append(t(40, 190, '企业自己建立', 13, fill=MID))
    things = [('资产目录', 'CSGHub'), ('模型网关', '路由和计量'), ('一套权限', '每个智能体最小权限'), ('评测和运行记录', '用真实失败攒题')]
    for i, (n, s) in enumerate(things):
        x = 40 + i * 132
        b.append(box(x, 202, 120, 70, fill=LIGHT, sw=2))
        b.append(t(x + 60, 232, n, 14 if len(n) < 6 else 13, 'middle', 'bold'))
        b.append(t(x + 60, 254, s, 11, 'middle', fill=MID))
    b.append(line(300, 276, 300, 304))
    b.append(box(40, 306, 516, 44, fill='#fff', stroke=MID, dash='6 4'))
    b.append(t(298, 333, '底层继续用多家云、多家模型', 14, 'middle'))
    b.append(t(600, 82, '第一阶段怎样算做成', 14, weight='bold'))
    checks = [('换模型', ['把一项任务换成另一家的模型，', '评测题重考一遍']),
              ('导出资产', ['提示词、知识库、评测集、记录', '在另一套环境里能读懂、能用']),
              ('停下智能体', ['按下停止键，确认真的停了，', '业务切到人工或备用流程'])]
    for i, (n, d) in enumerate(checks):
        y = 94 + i * 86
        b.append(box(600, y, 260, 76))
        b += num(622, y + 24, i + 1)
        b.append(t(642, y + 29, n, 15, weight='bold'))
        b += ml(616, y + 50, d, 12, lh=17)
    b.append(t(40, 400, '每个 OpenCSG 组件都可以换成别家的同类产品；换了以后蓝图仍然成立，不成立的地方就是锁定风险', 13, fill=MID))
    save('fig22-1_enterprise_hub.svg', svg(W, H, '\n'.join(b)))


# 22-2 data factory pipeline
def fig22_2():
    W, H = 900, 500
    b = title('高质量数据工厂：从原始数据到可审计资产')
    row1 = ['盘点数据', '确认许可和合规', '去重', '清洗、转换', '处理敏感信息']
    row2 = ['标注', '抽检质量', '写数据集说明书', '版本管理', '用于训练或评测']
    gap_tool = {'去重', '处理敏感信息'}
    tags = {'清洗、转换': 'DataFlow', '标注': 'DataFlow', '版本管理': 'CSGHub'}
    w, g = 146, 20
    def draw(i, s, y):
        x = 40 + i * (w + g)
        dash = '5 4' if s in gap_tool else ''
        b.append(box(x, y, w, 50, fill='#fff', dash=dash, stroke=MID if dash else INK))
        b.append(t(x + w / 2, y + 31, s, 14, 'middle', 'bold' if s == '用于训练或评测' else 'normal'))
        if s in tags:
            b.append(t(x + w / 2, y + 68, tags[s], 12, 'middle', 'bold', fill=MID))
        return x
    for i, s in enumerate(row1):
        x = draw(i, s, 100)
        if i < 4:
            b.append(line(x + w + 2, 125, x + w + g - 2, 125, sw=1.2))
    # row2 right->left
    for i, s in enumerate(row2):
        draw(4 - i, s, 220)
        x = 40 + (4 - i) * (w + g)
        if i < 4:
            b.append(line(x - 2, 245, x - g + 2, 245, sw=1.2))
    xr = 40 + 4 * (w + g) + w / 2
    b.append(line(xr, 152, xr, 218, sw=1.2))
    b.append(path(f'M40,245 H24 V125 H37', dash='5 4', sw=1.2))
    b.append(t(30, 92, '使用结果反馈回来', 12, fill=MID))
    b.append(t(40, 318, 'DataFlow、CSGHub：OpenCSG 公开文档写到的部分　　虚线框：公开文档没写到，需另配工具', 12, fill=MID))
    b.append(t(40, 360, '看这些指标，不看处理了多少 TB', 15, weight='bold'))
    ms = ['可用样本比例', '重复率、错误率', '覆盖率', '标注一致性', '许可完整率', '评测提升', '真实任务改善', '可用周期']
    for i, s in enumerate(ms):
        r, c = divmod(i, 4)
        x, y = 40 + c * 207, 376 + r * 52
        hl = (s == '许可完整率')
        b.append(box(x, y, 192, 42, fill=LIGHT if hl else FAINT, sw=2 if hl else 1, stroke=INK if hl else MID))
        b.append(t(x + 96, y + 27, s, 14, 'middle', 'bold' if hl else 'normal'))
    b.append(t(40, 490, '许可完整率最容易被忽略，出了问题代价最大', 12, fill=MID))
    save('fig22-2_data_factory.svg', svg(W, H, '\n'.join(b)))


# 23-1 ten board questions
def fig23_1():
    W, H = 900, 500
    b = title('董事会每半年回答的十个问题')
    groups = [('依赖', [(1, ['主模型或云不可用，', '关键任务能否继续']),
                        (2, ['切换供应商时资产', '能否导出、跑起来'])]),
              ('资产', [(3, ['数据、知识、评测和', '反馈在哪里，谁拥有']),
                        (4, ['有没有统一的', '资产清单']),
                        (5, ['有没有独立于供应商', '的黄金评测集'])]),
              ('责任', [(6, ['哪些智能体能代表公司', '行动，权限和预算多大']),
                        (7, ['哪些动作要人确认，', '谁真正有权停止']),
                        (8, ['事故有没有变成', '回归测试和制度改进'])]),
              ('方向', [(9, ['投入产出按 Token、', '任务还是业务结果算']),
                        (10, ['一年后积累的是自己', '的能力，还是依赖'])])]
    for i, (g, qs) in enumerate(groups):
        x = 40 + i * 207
        b += dark(x, 80, 192, 38, g, 16)
        b.append(box(x, 118, 192, 232, fill=FAINT if i == 3 else '#fff'))
        for j, (n, lines) in enumerate(qs):
            y = 146 + j * 70
            b += num(x + 20, y - 5, n, r=11, size=11)
            b += ml(x + 38, y, lines, 13, lh=19)
    b.append(bracket_down(40, 646, 360))
    b.append(t(343, 392, '前八个可以用事实回答', 13, 'middle', 'bold'))
    b.append(bracket_down(661, 853, 360))
    b.append(t(757, 392, '后两个需要判断', 13, 'middle', 'bold'))
    b.append(t(40, 428, '每个问题配一页，证据要可以复查', 14, weight='bold'))
    for i, s in enumerate(['现状', '证据', '缺口']):
        x = 300 + i * 90
        b.append(box(x, 412, 80, 26, fill='#fff', stroke=MID, rx=3))
        b.append(t(x + 40, 430, s, 13, 'middle'))
    b.append(t(40, 466, '例如：资产清单的版本号、评测集最近一次运行结果、停止演练记录、导出测试的日志', 13, fill=MID))
    b.append(t(40, 488, '答不上来也是有用的信息：写明下一个半年由谁补齐', 13, fill=MID))
    save('fig23-1_board_questions.svg', svg(W, H + 10, '\n'.join(b)))


# 24-1 180-day roadmap gantt
def fig24_1():
    W, H = 900, 530
    b = title('一百八十天路线图')
    x0, x1 = 330, 860
    def X(d): return x0 + (x1 - x0) * d / 180
    for d in range(0, 181, 30):
        b.append(line(X(d), 92, X(d), 436, arrow=False, stroke=FAINT if d not in (0,) else LIGHT, sw=1))
        b.append(t(X(d), 84, f'{d}', 12, 'middle', fill=MID))
    b.append(t(x0 - 10, 84, '天', 12, 'end', fill=MID))
    phases = [('盘点', 'AI 依赖地图、十项任务、六种能力评分'),
              ('试点', '黄金评测集、最小权限、三本账基线'),
              ('生产', '模型路由、审计轨迹、停止和接管演练'),
              ('数据飞轮', '数据卡、失败集、反馈回流'),
              ('规模化', '智能体模板、统一资产目录、治理门槛'),
              ('主权演练', '模型切换、平台导出、应急演练报告')]
    shades = ['#fff', '#eeeeee', '#dddddd', '#cccccc', '#bbbbbb', '#111']
    for i, (n, d) in enumerate(phases):
        y = 100 + i * 56
        b.append(t(40, y + 18, n, 15, weight='bold'))
        b.append(t(40, y + 38, d, 12, fill=MID))
        b.append(box(X(30 * i) + 2, y + 6, X(30) - X(0) - 4, 34, fill=shades[i], rx=4))
        b.append(t(X(30 * i + 15), y + 28, f'{30 * i + 1}—{30 * i + 30}', 12, 'middle', fill='#fff' if i == 5 else INK))
    b.append(box(X(0) - 4, 100, X(90) - X(0) + 8, 168, fill='none', stroke=MID, dash='5 4', rx=8))
    b += ml(X(90) + 14, 160, ['前九十天与第二十七章', '的作战手册重叠'], 12, fill=MID, lh=18)
    b.append(line(x0, 456, x1, 456, arrow=False, sw=2))
    cps = [(30, '依赖地图'), (60, '闭环跑通'), (90, '故障演练'), (180, '真实切换')]
    for d, s in cps:
        x = X(d)
        b.append(poly([(x, 446), (x + 9, 456), (x, 466), (x - 9, 456)], fill=INK))
        b.append(t(x, 486, f'第 {d} 天', 12, 'middle', 'bold'))
        b.append(t(x, 504, s, 12, 'middle', fill=MID))
    b.append(t(40, 461, '四个检查点', 14, weight='bold'))
    save('fig24-1_180_day_roadmap.svg', svg(W, H, '\n'.join(b)))


# 25-1 maturity levels
def fig25_1():
    W, H = 900, 490
    b = title('成熟度六级：每升一级都要拿出证据')
    lv = [('L0', '影子 AI'), ('L1', '工具 AI'), ('L2', '流程 AI'), ('L3', '智能体 AI'), ('L4', '主权 AI'), ('L5', '自适应组织')]
    ev = [['使用清单', '基本政策'],
          ['任务单', '独立智能体账号', '第一版评测集'],
          ['停止和接管演练', '三本账数据', '发布门'],
          ['真实替换记录', '完整导出记录', '备用模型跑真流量'],
          ['失败变成评测题', '修改进入知识库', '治理规则改过']]
    caps = ['选择', '审计的起点', '', '替换、迁移', '组合、演进']
    shades = ['#fff', '#f0f0f0', '#e0e0e0', '#cfcfcf', '#bcbcbc', '#a6a6a6']
    base, w = 420, 128
    for i, (code, n) in enumerate(lv):
        x = 40 + i * 138
        h = 60 + i * 42
        y = base - h
        b.append(box(x, y, w, h, fill=shades[i], rx=4, dash='6 4' if i == 5 else ''))
        b.append(t(x + w / 2, y + 22, code, 13, 'middle', fill=MID if i < 5 else INK))
        b.append(t(x + w / 2, y + 44, n, 15, 'middle', 'bold'))
        if i < 5:
            top = y - 14 - 19 * len(ev[i]) - (18 if caps[i] else 0)
            b.append(t(x + 6, top, f'升 L{i + 1} 要有：', 12, weight='bold'))
            b += ml(x + 6, top + 19, ev[i], 12, lh=19)
            if caps[i]:
                b.append(t(x + 6, top + 19 * (len(ev[i]) + 1), '对应：' + caps[i], 12, fill=MID))
    b.append(t(40 + 5 * 138 + w / 2, base - 60 - 5 * 42 - 14, '一个方向', 12, 'middle', fill=MID))
    b.append(line(40, base + 2, 860, base + 2, arrow=False, sw=2))
    b.append(t(40, 448, '衡量的是控制程度，不是模型有多先进；只写得出“供应商说”的地方，一律按低一级算', 13, fill=MID))
    b.append(t(40, 472, '级别可以往下掉：模型更新、平台迁移、关键工程师离职以后，按任务分别重评', 13, fill=MID))
    save('fig25-1_maturity_levels.svg', svg(W, H, '\n'.join(b)))


# 26-1 twenty principles
def fig26_1():
    W, H = 900, 520
    b = title('给 CEO 的二十条原则')
    dont = ['把 AI 战略写成模型采购清单', '把私有化部署等同于主权', '把开放权重叫作完整开源',
            '让组织记忆只存在聊天历史里', '给智能体超出任务需要的权限', '上线没人真正有权停止的系统',
            '只看 Token 成本', '只做漂亮的演示', '把数据全部集中到一处', '把许可证治理留到发布前一天']
    do = ['保留一条真实可用的模型替代路径', '做一次完整导出，并在别处跑起来', '把高质量数据当作长期资本',
          '把人工修改当作高价值的反馈', '让备用模型平时承担少量真实流量', '让开源社区成为人才和标准的入口',
          '产品建在开放接口和可迁移资产上', '把智能体当作数字劳动力来管', '把每次事故变成评测和制度改进',
          '能力可以购买，责任不能外包']
    for c, (head, items, start) in enumerate((('十条不要做的事', dont, 1), ('十条一定要做的事', do, 11))):
        x = 40 + c * 420
        b += dark(x, 80, 400, 36, head, 15)
        b.append(box(x, 116, 400, 316, fill='#fff' if c == 0 else FAINT))
        for i, s in enumerate(items):
            y = 140 + i * 30
            n = start + i
            b += num(x + 22, y, n, r=11, size=11)
            b.append(t(x + 42, y + 5, ('不要' if c == 0 else '') + s, 14, weight='bold' if n == 20 else 'normal'))
    b.append(t(40, 462, '落地', 14, weight='bold'))
    steps = ['挑三到五条', '绑定一个已有管理动作', '指定检查人', '半年后拿证据检查']
    xs = [90, 246, 446, 600]
    ws = [130, 180, 130, 170]
    for i, (x, w, s) in enumerate(zip(xs, ws, steps)):
        b.append(box(x, 444, w, 34, fill='#fff', stroke=MID))
        b.append(t(x + w / 2, 466, s, 13, 'middle'))
        if i < 3:
            b.append(line(x + w + 2, 461, xs[i + 1] - 3, 461, sw=1.2))
    b.append(t(40, 506, '例如采购审批、预算申请、上线评审或季度汇报', 12, fill=MID))
    save('fig26-1_twenty_principles.svg', svg(W, H, '\n'.join(b)))


# 27-1 six steps, ninety days
def fig27_1():
    W, H = 900, 460
    b = title('作战手册：六个步骤，九十天')
    steps = [('选任务', ['先选任务，', '再选模型']), ('画任务图', ['八类节点，', '每个节点标清']),
             ('最小控制面', ['八组对应关系', '随时查得到']), ('评测代替演示', ['六类测试，', '每次改动重跑']),
             ('三本账', ['每项任务成本', '每个验证结果成本']), ('设计退出', ['第一天就画', '降级路径'])]
    for i, (n, d) in enumerate(steps):
        x = 40 + i * 138
        b.append(box(x, 85, 126, 108, fill=LIGHT if i == 5 else '#fff'))
        b += num(x + 20, 105, i + 1)
        b.append(t(x + 63, 136, n, 15 if len(n) < 6 else 14, 'middle', 'bold'))
        b += ml(x + 63, 160, d, 12, 'middle', lh=17)
        if i < 5:
            b.append(line(x + 127, 139, x + 137, 139, sw=1.2))
    b.append(path('M796,195 V214 H103 V198', dash='5 4', sw=1.2))
    b.append(t(450, 236, '形成闭环：能交付、能衡量、能叫停、能替换', 14, 'middle', 'bold'))
    x0, x1 = 40, 860
    def X(wk): return x0 + (x1 - x0) * wk / 13
    b.append(t(40, 278, '九十天', 14, weight='bold'))
    phases = [(0, 2, '发现', ['任务清单', '风险分级', '成本基线']),
              (2, 6, '试点', ['三个最小可用版本', '黄金评测集、最小权限']),
              (6, 10, '生产', ['控制面、监控', '三本账、备用路径']),
              (10, 13, '推广', ['任务模板、资产沉淀', '治理规则'])]
    shades = ['#fff', '#e6e6e6', '#cccccc', '#aaaaaa']
    for i, (a, z, n, d) in enumerate(phases):
        b.append(box(X(a) + 2, 292, X(z) - X(a) - 4, 40, fill=shades[i], rx=4))
        b.append(t((X(a) + X(z)) / 2, 318, n, 15, 'middle', 'bold'))
        b.append(t((X(a) + X(z)) / 2, 352, f'第 {a + 1}—{z} 周', 12, 'middle', fill=MID))
        b += ml((X(a) + X(z)) / 2, 376, d, 12, 'middle', lh=18)
    b.append(t(40, 444, '九十天以后，公司层面的工作接着走第二十四章的一百八十天路线图', 13, fill=MID))
    save('fig27-1_playbook.svg', svg(W, H, '\n'.join(b)))


# 27-2 task graph
def fig27_2():
    W, H = 900, 450
    b = title('一张任务图：八类节点')
    nodes = [('触发', '什么事件开始'), ('理解', '弄清要做什么'), ('检索', '找到要用的资料'),
             ('判断', '在选项里做决定'), ('行动', '调工具改外部状态'), ('确认', '关键处请人把关'),
             ('验证', '是否真的达成')]
    w, g = 104, 15
    for i, (n, d) in enumerate(nodes):
        x = 40 + i * (w + g)
        hl = n in ('行动', '确认')
        b.append(box(x, 95, w, 50, fill=LIGHT if n == '确认' else '#fff', sw=2 if hl else 1.5))
        b.append(t(x + w / 2, 126, n, 16, 'middle', 'bold'))
        b.append(t(x + w / 2, 165, d, 12, 'middle', fill=MID))
        if i < 6:
            b.append(line(x + w + 1, 120, x + w + g - 1, 120, sw=1.2))
    b.append(box(340, 225, 220, 54, fill=FAINT, dash='5 4'))
    b.append(t(450, 249, '异常处理', 16, 'middle', 'bold'))
    b.append(t(450, 269, '出错时退回哪里', 12, 'middle', fill=MID))
    xa = 40 + 4 * (w + g) + w / 2
    xv = 40 + 6 * (w + g) + w / 2
    xr = 40 + 2 * (w + g) + w / 2
    b.append(path(f'M{xa},176 L520,222', dash='4 3', sw=1.2))
    b.append(path(f'M{xv},176 L560,236', dash='4 3', sw=1.2))
    b.append(path(f'M340,252 H{xr} V180', dash='4 3', sw=1.2))
    b.append(t(xr + 10, 214, '退回某一步', 12, fill=MID))
    b.append(box(40, 312, 820, 104))
    b.append(t(60, 340, '每个节点都标明', 14, weight='bold'))
    tags = ['数据从哪里来', '模型看到了什么', '调用了什么工具', '用的是谁的身份',
            '权限多久失效', '失败后回到哪一步', '最终由谁负责']
    for i, s in enumerate(tags):
        r, c = divmod(i, 4)
        x, y = 60 + c * 198, 354 + r * 32
        b.append(box(x, y, 184, 26, fill=FAINT, stroke=MID, sw=1, rx=3))
        b.append(t(x + 92, y + 18, s, 13, 'middle'))
    b.append(t(40, 440, '画的过程中常会发现：藏着一个需要人判断的环节，或者某一步要用权限过大的老接口', 13, fill=MID))
    save('fig27-2_task_graph.svg', svg(W, H + 10, '\n'.join(b)))


# 28-1 five transitions
def fig28_1():
    W, H = 900, 470
    b = title('五次跃迁：从工具化到主权化')
    st = [('工具化', ['员工各自用聊天机器人', '经验锁在对话框里']),
          ('流程化', ['接进客服、销售、研发', '重复任务稳定下来']),
          ('智能体化', ['围绕目标规划步骤', '对外部世界产生结果']),
          ('平台化', ['统一管模型、数据、', '身份、权限、评测、成本']),
          ('主权化', ['具备六种能力，', '供应商变了业务照常'])]
    base = 400
    for i, (n, d) in enumerate(st):
        x = 40 + i * 166
        h = 96 + i * 46
        y = base - h
        b.append(box(x, y, 156, h, fill=['#fff', '#eeeeee', '#dddddd', '#c8c8c8', '#b0b0b0'][i], rx=4, sw=2 if i == 4 else 1.5))
        b.append(t(x + 78, y + 28, n, 16, 'middle', 'bold'))
        b += ml(x + 78, y + 52, d, 12, 'middle', lh=18)
        b.append(t(x + 78, y - 10, '第' + "一二三四五"[i] + '次', 12, 'middle', fill=MID))
    b.append(line(40, base + 2, 860, base + 2, arrow=False, sw=2))
    b.append(t(40, 430, '不必一步不落地走完，同一家公司的不同部门可能在不同阶段', 13, fill=MID))
    b.append(t(40, 454, '要看的是：有没有一种可以持续的机制，把外部的智能吸收进来，变成自己的能力', 13, weight='bold'))
    save('fig28-1_five_transitions.svg', svg(W, H, '\n'.join(b)))


# 28-2 digital worker file
def fig28_2():
    W, H = 900, 430
    b = title('一份数字员工档案，和它的一生')
    b.append(box(40, 85, 440, 300))
    b += dark(40, 85, 440, 40, '数字员工档案', 15)
    rows = [('身份', '自己的身份，不借员工账号和管理密钥'),
            ('权限', '看什么、做什么、多久失效、能否转交'),
            ('预算', '钱、工具调用、算力，用完就停'),
            ('何时问人', '哪些情况必须回来找人'),
            ('何时失效', '到期自动作废'),
            ('当前版本', '正在跑的是哪个版本'),
            ('最近评测', '最近一次评测的结果')]
    for i, (k, v) in enumerate(rows):
        y = 152 + i * 33
        main = i < 3
        b.append(t(60, y, k, 14 if main else 13, weight='bold' if main else 'normal', fill=INK if main else MID))
        b.append(t(140, y, v, 13 if main else 12, fill=INK if main else MID))
        if i == 2:
            b.append(line(60, y + 13, 460, y + 13, arrow=False, stroke=LIGHT, sw=1))
    b.append(path('M470,138 h0', arrow=False))
    b.append(t(470, 145 + 33, '', 1))
    b.append(t(540, 100, '和员工一样走完整流程', 14, weight='bold'))
    life = [('上线要登记', '负责人、服务的任务、身份、权限、预算'), ('权限定期复核', '能看什么、能做什么、多久失效'),
            ('表现持续评估', '看结果，也看资源、出错和人工介入'), ('正式退役', '撤销身份，收回凭证，留下经验')]
    for i, (n, d) in enumerate(life):
        y = 116 + i * 66
        b.append(box(540, y, 320, 50, fill=LIGHT if i == 3 else '#fff'))
        b.append(t(556, y + 22, n, 14, weight='bold'))
        b.append(t(556, y + 41, d, 12, fill=MID))
        if i < 3:
            b.append(line(700, y + 52, 700, y + 64, sw=1.2))
    b.append(box(40, 395, 820, 30, fill='none', stroke=MID, dash='5 4', rx=4))
    b.append(t(450, 415, '最大的风险：没人负责、长期握着权限、从没重新评测过的“影子智能体”', 13, 'middle'))
    save('fig28-2_digital_worker.svg', svg(W, H + 10, '\n'.join(b)))


FIGS = [fig8_1, fig9_1, fig10_1, fig10_2, fig11_1, fig12_1, fig13_1, fig13_2, fig14_1, fig15_1,
        fig16_1, fig17_1, fig18_1, fig19_1, fig20_1, fig21_1, fig22_1, fig22_2, fig23_1, fig24_1,
        fig25_1, fig26_1, fig27_1, fig27_2, fig28_1, fig28_2]
if __name__ == '__main__':
    for f in FIGS:
        f()
    print(len(FIGS), 'figures')
