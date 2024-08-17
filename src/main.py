import requests as req
from lxml import etree
from tkinter import Tk,filedialog
import json,time,random,os,re,platform

CODE_ST = 58344
CODE_ED = 58715
charset=[
    "D",
    "在",
    "主",
    "特",
    "家",
    "军",
    "然",
    "表",
    "场",
    "4",
    "要",
    "只",
    "v",
    "和",
    "?",
    "6",
    "别",
    "还",
    "g",
    "现",
    "儿",
    "岁",
    "?",
    "?",
    "此",
    "象",
    "月",
    "3",
    "出",
    "战",
    "工",
    "相",
    "o",
    "男",
    "直",
    "失",
    "世",
    "F",
    "都",
    "平",
    "文",
    "什",
    "V",
    "O",
    "将",
    "真",
    "T",
    "那",
    "当",
    "?",
    "会",
    "立",
    "些",
    "u",
    "是",
    "十",
    "张",
    "学",
    "气",
    "大",
    "爱",
    "两",
    "命",
    "全",
    "后",
    "东",
    "性",
    "通",
    "被",
    "1",
    "它",
    "乐",
    "接",
    "而",
    "感",
    "车",
    "山",
    "公",
    "了",
    "常",
    "以",
    "何",
    "可",
    "话",
    "先",
    "p",
    "i",
    "叫",
    "轻",
    "M",
    "士",
    "w",
    "着",
    "变",
    "尔",
    "快",
    "l",
    "个",
    "说",
    "少",
    "色",
    "里",
    "安",
    "花",
    "远",
    "7",
    "难",
    "师",
    "放",
    "t",
    "报",
    "认",
    "面",
    "道",
    "S",
    "?",
    "克",
    "地",
    "度",
    "I",
    "好",
    "机",
    "U",
    "民",
    "写",
    "把",
    "万",
    "同",
    "水",
    "新",
    "没",
    "书",
    "电",
    "吃",
    "像",
    "斯",
    "5",
    "为",
    "y",
    "白",
    "几",
    "日",
    "教",
    "看",
    "但",
    "第",
    "加",
    "候",
    "作",
    "上",
    "拉",
    "住",
    "有",
    "法",
    "r",
    "事",
    "应",
    "位",
    "利",
    "你",
    "声",
    "身",
    "国",
    "问",
    "马",
    "女",
    "他",
    "Y",
    "比",
    "父",
    "x",
    "A",
    "H",
    "N",
    "s",
    "X",
    "边",
    "美",
    "对",
    "所",
    "金",
    "活",
    "回",
    "意",
    "到",
    "z",
    "从",
    "j",
    "知",
    "又",
    "内",
    "因",
    "点",
    "Q",
    "三",
    "定",
    "8",
    "R",
    "b",
    "正",
    "或",
    "夫",
    "向",
    "德",
    "听",
    "更",
    "?",
    "得",
    "告",
    "并",
    "本",
    "q",
    "过",
    "记",
    "L",
    "让",
    "打",
    "f",
    "人",
    "就",
    "者",
    "去",
    "原",
    "满",
    "体",
    "做",
    "经",
    "K",
    "走",
    "如",
    "孩",
    "c",
    "G",
    "给",
    "使",
    "物",
    "?",
    "最",
    "笑",
    "部",
    "?",
    "员",
    "等",
    "受",
    "k",
    "行",
    "一",
    "条",
    "果",
    "动",
    "光",
    "门",
    "头",
    "见",
    "往",
    "自",
    "解",
    "成",
    "处",
    "天",
    "能",
    "于",
    "名",
    "其",
    "发",
    "总",
    "母",
    "的",
    "死",
    "手",
    "入",
    "路",
    "进",
    "心",
    "来",
    "h",
    "时",
    "力",
    "多",
    "开",
    "已",
    "许",
    "d",
    "至",
    "由",
    "很",
    "界",
    "n",
    "小",
    "与",
    "Z",
    "想",
    "代",
    "么",
    "分",
    "生",
    "口",
    "再",
    "妈",
    "望",
    "次",
    "西",
    "风",
    "种",
    "带",
    "J",
    "?",
    "实",
    "情",
    "才",
    "这",
    "?",
    "E",
    "我",
    "神",
    "格",
    "长",
    "觉",
    "间",
    "年",
    "眼",
    "无",
    "不",
    "亲",
    "关",
    "结",
    "0",
    "友",
    "信",
    "下",
    "却",
    "重",
    "己",
    "老",
    "2",
    "音",
    "字",
    "m",
    "呢",
    "明",
    "之",
    "前",
    "高",
    "P",
    "B",
    "目",
    "太",
    "e",
    "9",
    "起",
    "稜",
    "她",
    "也",
    "W",
    "用",
    "方",
    "子",
    "英",
    "每",
    "理",
    "便",
    "四",
    "数",
    "期",
    "中",
    "C",
    "外",
    "样",
    "a",
    "海",
    "们",
    "任"
]

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

def down_zj(it):
    global headers
    an = {}
    ele = etree.HTML(req.get('https://fanqienovel.com/page/'+str(it),headers=headers).text)
    a = ele.xpath('//div[@class="chapter"]/div/a')
    for i in range(len(a)):
        an[a[i].text] = a[i].xpath('@href')[0].split('/')[-1]
    if ele.xpath('//h1/text()')==[]:
        return ['err',0,0]
    return [ele.xpath('//h1/text()')[0],an,ele.xpath('//span[@class="info-label-yellow"]/text()')]

def interpreter(uni):
    global CODE_ST,charset
    bias = uni - CODE_ST
    if bias < 0 or bias >= len(charset) or charset[bias] =='?':
        return chr(uni)
    return charset[bias]

def down_text(it):
    global CODE_ST,CODE_ED,headers
    headers2 = headers
    headers2['cookie'] = 'novel_web_id=7357767624615331362'
    while True:
        res = req.get('https://fanqienovel.com/api/reader/full?itemId='+str(it),headers=headers2)
        n = json.loads(res.text)['data']
        if 'chapterData' in n:
            break
        time.sleep(0.5)
    n = n['chapterData']['content']
    s = ''
    for i in range(len(n)):
        uni = ord(n[i])
        if CODE_ST <= uni <= CODE_ED:
            s += interpreter(uni)
        else:
            s += n[i]
    try:
        return '\n'.join(etree.HTML(s).xpath('//p/text()'))
    except:
        s = s[6:]
        tmp = 1
        a = ''
        for i in s:
            if i=='<':
                tmp += 1
            elif i=='>':
                tmp -= 1
            elif tmp==0:
                a += i
            elif tmp==1 and i=='p':
                a = (a+'\n').replace('\n\n','\n')
        return a

def sanitize_filename(filename):
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    illegal_chars_rep = ['＜','＞','：','＂','／','＼','｜','？','＊']
    for i in range(len(illegal_chars)):
        filename = filename.replace(illegal_chars[i], illegal_chars_rep[i])
    return filename


def down_book(it, config_obj):
    name, zj, zt = down_zj(it)
    if name == 'err':
        return 'err'
    zt = zt[0]

    safe_name = sanitize_filename(name)
    book_dir = os.path.join(script_dir, safe_name)

    print('\n开始下载《%s》，状态‘%s’' % (name, zt))
    book_json_path = os.path.join(bookstore_dir, safe_name + '.json')

    if os.path.exists(book_json_path):
        with open(book_json_path, 'r', encoding='UTF-8') as json_file:
            ozj = json.load(json_file)
    else:
        ozj = {}

    cs = 0
    for i in zj:
        f = False
        if i in ozj:
            try:
                int(ozj[i])
                f = True
            except:
                zj[i] = ozj[i]
        else:
            f = True
        if f:
            print('下载', i)
            zj[i] = down_text(zj[i])
            time.sleep(random.uniform(config_obj['delay'][0],config_obj['delay'][1])/1000)
            cs += 1
            if cs>=5:
                cs = 0
                with open(book_json_path, 'w', encoding='UTF-8') as json_file:
                    json.dump(zj, json_file,ensure_ascii=False)

    with open(book_json_path, 'w', encoding='UTF-8') as json_file:
        json.dump(zj, json_file,ensure_ascii=False)

    fg = '\n' + ' ' * config_obj['kg']
    if config['save_mode']==1:
        text_file_path = os.path.join(config_obj['save_path'], safe_name + '.txt')
        with open(text_file_path, 'w', encoding='UTF-8') as text_file:
            for chapter_title in zj:
                text_file.write(chapter_title + fg)
                if config_obj['kg'] == 0:
                    text_file.write(zj[chapter_title] + '\n')
                else:
                    text_file.write(zj[chapter_title].replace('\n', fg) + '\n')
    elif config['save_mode']==2:
        text_dir_path = os.path.join(config_obj['save_path'], safe_name)
        if not os.path.exists(text_dir_path):
            os.makedirs(text_dir_path)
        for chapter_title in zj:
            text_file_path = os.path.join(text_dir_path, sanitize_filename(chapter_title) + '.txt')
            with open(text_file_path, 'w', encoding='UTF-8') as text_file:
                text_file.write(fg)
                if config_obj['kg'] == 0:
                    text_file.write(zj[chapter_title] + '\n')
                else:
                    text_file.write(zj[chapter_title].replace('\n', fg) + '\n')

    else:
        print('保存模式出错！')

    return zt

def is_number(s):
    return s.isdigit()

def parse_id(url):
    # 使用正则表达式从URL中提取书籍ID
    match = re.search(r'/page/(\d+)', url)
    if match:
        return int(match.group(1))
    else:
        return None

def select_save_directory():
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    return filedialog.askdirectory(title='请选择保存小说的文件夹')

script_dir = ''

# 设置data文件夹的路径
data_dir = os.path.join(script_dir, 'data')

# 检查data文件夹是否存在，如果不存在则创建
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# 设置bookstore文件夹的路径
bookstore_dir = os.path.join(data_dir,'bookstore')

# 检查bookstore文件夹是否存在，如果不存在则创建
if not os.path.exists(bookstore_dir):
    os.makedirs(bookstore_dir)

# 更新record.json和config.json的文件路径
record_path = os.path.join(data_dir, 'record.json')
config_path = os.path.join(data_dir, 'config.json')

# 打印程序信息
os.popen('title fanqienovel-downloader v1.0.7')
print('本程序完全免费。\nGithub: https://github.com/ying-ck/fanqienovel-downloader\n作者：Yck & qxqycb')

# 检查并创建配置文件config.json
reset = {'kg': 0, 'delay': [50, 150], 'save_path': '', 'save_mode': 1}

# 首先尝试加载已有的config.json
if not os.path.exists(config_path):
    # 如果不存在，检查当前目录下是否有config.json
    if os.path.exists('config.json'):
        shutil.copy('config.json', config_path)  # 使用shutil.copy代替os.replace
    else:
        # 如果当前目录下也没有，创建新的config.json
        with open(config_path, 'w', encoding='UTF-8') as f:
            json.dump(reset, f)

# 加载config.json的内容
with open(config_path, 'r', encoding='UTF-8') as f:
    config = json.load(f)

# 确保config包含所有必要的键
for key in reset:
    if key not in config:
        config[key] = reset[key]

# 保存更新后的配置
with open(config_path, 'w', encoding='UTF-8') as f:
    json.dump(config, f)

# 检查并创建记录文件record.json
record_path = os.path.join(data_dir, 'record.json')
if not os.path.exists(record_path):
    if os.path.exists('record.json'):
        os.replace('record.json',record_path)
    else:
        with open(record_path, 'w', encoding='UTF-8') as f:
            json.dump([], f)

# 主循环
while True:
    print('\n输入书的id直接下载\n输入下面的数字进入其他功能:')
    print('''
1. 更新小说
2. 设置
3. 退出
''')

    inp = input()
    if inp in ['1', '2', '3']:
        if inp == '1':
            # 更新操作
            with open(record_path, 'r', encoding='UTF-8') as f:
                records = json.load(f)
            for book_id in records:
                status = down_book(book_id, config)
                if status == 'err' or status == '已完结':
                    records.remove(book_id)
            with open(record_path, 'w', encoding='UTF-8') as f:
                json.dump(records, f)
            print('更新完成')

        elif inp == '2':
            # 设置操作
            print('请选择项目：1.正文段首空格数 2.章节下载间隔延迟 3.小说保存路径 4.小说保存方式 5. 批量下载')
            inp2 = input()
            if inp2 == '1':
                config['kg'] = int(input('请输入正文段首空格数（当前为%d）：' % config['kg']))
                print('设置完成')
            elif inp2 == '2':
                print('由于延迟过小造成的后果请自行负责。\n请输入下载间隔随机延迟的')
                config['delay'][0] = int(input('下限（当前为%d）（毫秒）：' % config['delay'][0]))
                config['delay'][1] = int(input('上限（当前为%d）（毫秒）：' % config['delay'][1]))
                print('设置完成')
            elif inp2 == '3':
                print('tip:设置为当前目录点取消')
                time.sleep(1)
                config['save_path'] = select_save_directory()
                print('设置完成')
            elif inp2 == '4':
                print('请选择：1.保存为单个txt 2.分章保存')
                inp3 = input()
                if inp3 == '1':
                    config['save_mode'] = 1
                elif inp3 == '2':
                    config['save_mode'] = 2
                else:
                    print('请正确输入!')
                print('设置完成')
                continue
            elif inp2 == '5':
                urls_path = 'urls.txt'  # 定义文件名
                if not os.path.exists(urls_path):
                    print(f"未找到'{urls_path}'，将为您创建一个新的文件。")
                    with open(urls_path, 'w', encoding='UTF-8') as file:
                        file.write("# 请输入小说链接，用逗号隔开\n")
                print(f"'{urls_path}' 已存在。请在文件中输入小说链接，并用逗号(注意：用英文逗号!英文!!!)隔开。")

                # 使用默认文本编辑器打开urls.txt文件供用户编辑
                root = Tk()
                root.withdraw()  # 隐藏主窗口
                root.update()  # 更新Tkinter的事件循环，确保窗口被隐藏

                if platform.system() == "Windows":
                    # Windows系统使用os.startfile
                    os.startfile(urls_path)
                elif platform.system() == "Darwin":
                    # macOS系统使用open命令
                    os.system(f"open -a TextEdit {urls_path}")
                else:
                    # 其他系统使用默认文本编辑器
                    os.system(f"xdg-open {urls_path}")

                print("输入完成后请保存并关闭文件，然后按Enter键继续...")
                input()

                # 读取urls.txt文件中的链接
                with open(urls_path, 'r', encoding='UTF-8') as file:
                    content = file.read()
                    urls = re.split(r',\s*', content.strip())

                # 开始批量下载
                for url in urls:
                    book_id = parse_id(url)  # 尝试从链接中解析出书籍ID
                    if book_id is not None:
                        print(f'开始下载链接: {url}')
                        status = down_book(book_id, config)
                        if status == 'err':
                            print(f'链接: {url} 下载失败。')
                        else:
                            print(f'链接: {url} 下载完成。')
                    else:
                        print(f'无效链接或格式错误: {url}')

            else:
                print('请正确输入!')
                continue
            with open(config_path, 'w', encoding='UTF-8') as f:
                json.dump(config, f)

        elif inp == '3':
            break

    elif is_number(inp):  # 检查是否为纯数字ID
        book_id = int(inp)
        status = down_book(book_id, config)
        if status == 'err':
            print('找不到此书或无效的ID。')
        else:
            print('下载完成。')
    elif parse_id(inp) is not None:  # 检查是否为链接
        book_id = parse_id(inp)
        status = down_book(book_id, config)
        if status == 'err':
            print('找不到此书或链接无效。')
        else:
            print('下载完成。')
    else:
        print('无效的输入，请输入正确的书籍ID、链接或选择功能选项。')
