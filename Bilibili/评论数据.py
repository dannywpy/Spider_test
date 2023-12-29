"""
[课程内容]: Python采集B站评论数据

[授课老师]: 青灯教育-自游  [上课时间]: 20:05 可以点歌 可以问问题

[环境使用]:
    Python 3.10
    Pycharm

[模块使用]:
    import requests >>> pip install requests
    import csv
---------------------------------------------------------------------------------------------------
win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加婧琪老师微信python1018
---------------------------------------------------------------------------------------------------

写过爬虫 -> 1
没有写过 -> 0

url: 俗称网址
    唯一资源定位符

爬虫基本流程思路:
一. 数据来源分析
    1. 明确需求: 明确采集的网站以及数据内容
    2. 抓包分析: 浏览器自带工具 (开发者工具) 抓包
        - 打开开发者工具: F12 / 右键点击检查选择network (网络)
        - 点击最新评论 <栏目> / 获取刷新页面
        - 如何找到对应数据包地址:
            I. 如果返回数据包比较少, 我可以选择一个一个数据包点击去查看数据
            II. 通过关键字去搜索找到对应数据包 (极力推荐)
        数据包地址: https://api.bilibili.com/x/v2/reply/wbi/main

二. 代码实现步骤
    1. 发送请求 -> 模拟浏览器对于url发送请求
    2. 获取数据 -> 服务器返回的响应数据 <整个返回的内容>
    3. 解析数据 -> 提取需要的数据
    4. 保存数据 -> 保存表格文件中
对于本节课讲解的内容不懂就问

- 多页的数据采集: 本节课重点 (小难度)
    url请求参数变化规律
    - pagination_str:
        下一个参数, 来自于上一页的响应数据里面
    - w_rid: 需要JS逆向
        MD5(Ut + ct) --> md5加密方式
        Zt = [
            "mode=2",
            "oid=23836532",
            "pagination_str=%7B%22offset%22%3A%22%7B%5C%22type%5C%22%3A3%2C%5C%22direction%5C%22%3A1%2C%5C%22Data%5C%22%3A%7B%5C%22cursor%5C%22%3A6964%7D%7D%22%7D",
            "plat=1",
            "type=1",
            "web_location=1315875",
            "wts=1701089392" # 时间戳
        ]
        Ut: '&'.join(Zt)
        ct: "ea1db124af3c7062474693fa704f4ff8" <固定不变>
    - wts: 时间戳
        内置模块 time.time() 获取当前时间戳 自己生成出来

我没有基础 很多东西没学, 听得很懵..

- 了解咱们系统课程: 从零基础入门到项目实战, 学完之后可以达到企业开发水平

教授内容: 核心编程(基础) 爬虫开发 数据分析 网站开发 人工智能 自动化办公 JS逆向 vue框架...

加婧琪老师微信: pyton1018
    1. 免费领取课程学习路线图 <你要学什么内容>
    2. 根据你自己情况, 给你量身定制你学习方向


1. 兴趣爱好 (毕业 毕设)
    基础必备 + 后续根据个人需求 (爬虫 / 网站开发 / 人工智能)
2. 兼职外包: 核心编程+爬虫开发+数据分析+JS逆向 <入门简单深入难>
    推荐:
        理由1: 外包订单多
        理由2: 入门相对而言简单
    收益:
        单价: 200-5000左右
        收入: 1000-3000左右
    比如: 一周接1个外包, 一个外包均价 200元 --> 800元
    比如: 一周接2个外包, 一个外包均价 300元 --> 2400元

接单: 抽成2-3成  100元收入, 你到手 70-80元 <提供外包订单>
    淘宝 / 闲鱼
    接单群 QQ 微信
    接单平台

青灯教育外包接单群: <所有收益归你自己本身人所有>
    报名之后可以进群的 -> 直接提供甲方客户

想要跟着老师系统学 -> 6

我是零基础小白, 也能学会, 也能接单吗?
    - 按时听课: 坚持学习
    - 按时完成作业: 多敲多练
    - 认真学习态度: 不懂多问
老师可以保证你能够学会掌握

教学服务是全方面: 从入学 -> 学习中 -> 学习后
    - 直播 一周三节课 晚上8-10点直播授课
        理论+实践案例相结合教学方法
    - 录播 源码 笔记 文档 软件工具 作业 考核
    - 老师解答辅导 文字 语音远程操作调试
        任何不懂地方, 可以随时找我给你解答辅导
    - 班主任老师监督学习
    - 免费重修 <一遍不扎实, 学两遍 两遍不扎实, 学三遍>
    - 外包提供
        外包接单群 接单渠道 接单问题解答辅导 <python相关的呀>
    - 就业指导
        面试试题 面试技巧 面试简历 面试问题解答
    - 毕业证书
    - 培训合同
    - 发票
    ....

加婧琪老师微信: python1018
课程学费:
    兼职外包课程: 核心编程+爬虫开发+数据分析+JS逆向
        原价学费: 2260+2980+2180+1680 = 9100
        优惠学费: 6680
    高薪就业课程: 核心编程+爬虫开发+数据分析+网站开发+vue框架+人工智能+JS逆向
        原价学费: 2260+2980+2180+2980+1680+2680+1680 = 16440
        优惠学费: 8880

申请先学习后支付:
    1. 加婧琪老师: python1018
    2. 预定支付300元学费
    3. 直接办理入学进班学习
    4. 学一个月支付一个月学费

6680 - 300 = 6380 申请3/6/9/12/18个月支付学费
    6380 / 12 = 532元/月
    6380 / 18 = 354元/月

354元/月 相当于你一个月接1-2个简单外包
    200元外包 -> 2个
    300元外包 -> 1个

"""
# 导入数据请求模块 < 需要安装 pip install requests >
import requests
# 导入csv模块 <内置模块>
import csv
# 导入加密模块
import hashlib
# 导入时间模块
import time
from urllib.parse import quote
import re


def hash(data, date):
    print(quote(data))
    # %7B%22offset%22:%22%7B%5C%22type%5C%22:3,%5C%22direction%5C%22:1,%5C%22Data%5C%22:%7B%5C%22cursor%5C%22:7024%7D%7D%22%7D
    # %7B%22offset%22%3A%22%7B%5C%22type%5C%22%3A3%2C%5C%22direction%5C%22%3A1%2C%5C%22Data%5C%22%3A%7B%5C%22cursor%5C%22%3A7024%7D%7D%22%7D
    Zt = [
        "mode=2",
        "oid=23836532",
        f"pagination_str={quote(data)}",
        "plat=1",
        "type=1",
        "web_location=1315875",
        f"wts={date}"  # 时间戳
    ]
    ct = "ea1db124af3c7062474693fa704f4ff8"
    Ut = '&'.join(Zt)
    string = Ut + ct
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    w_rid = MD5.hexdigest()
    print(w_rid)
    return w_rid


def get_content(data):
    """发送请求: 模拟浏览器对于url发送请求
    - 模拟浏览器
    - url
    - 发送请求 (请求方法&请求参数)
    """
    # 时间戳
    date = (time.time() * 1000)
    pagination_str = '{"offset":"{\\"type\\":3,\\"direction\\":1,\\"Data\\":{\\"cursor\\":%s}}"}' % data
    print(pagination_str)
    w_rid = hash(pagination_str, date)
    # 模拟浏览器: 请求头 (字典)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    # 请求网址
    url = 'https://api.bilibili.com/x/v2/reply/wbi/main'

    print(url)
    # https://api.bilibili.com/x/v2/reply/wbi/main?oid=23836532&type=1&mode=2&pagination_str=%7B%22offset%22:%22%7B%5C%22type%5C%22:3,%5C%22direction%5C%22:1,%5C%22Data%5C%22:%7B%5C%22cursor%5C%22:7024%7D%7D%22%7D&plat=1&web_location=1315875&w_rid=d208fa03425c671711b111940a399bd8&wts=1701088928
    # https://api.bilibili.com/x/v2/reply/wbi/main?oid=23836532&type=1&mode=2&pagination_str=%7B%22offset%22%3A%22%7B%5C%22type%5C%22%3A3%2C%5C%22direction%5C%22%3A1%2C%5C%22Data%5C%22%3A%7B%5C%22cursor%5C%22%3A7024%7D%7D%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=d208fa03425c671711b111940a399bd8&wts=1701088928
    # 发送请求
    response = requests.get(url=url, params=data, headers=headers)
    print(response.json())
    """获取数据 -> 服务器返回的响应数据
    - response.json() 获取响应json数据
        <当你看到响应返回内容 {} 包裹起来的数据>
    - response.text 获取响应文本数据
        <html文件格式 其他内容>
    - response.content 获取响应二进制数据
        <保存 图片/音频/视频/特定格式文件 数据时候使用>
    """
    json_data = response.json()
    """解析数据 -> 提取需要的数据
        字典取值: 键值对取值
            根据冒号左边的内容[键], 提取冒号右边的内容[值]
        一层一层往下提取
    """
    # 提取数据所在列表
    replies = json_data['data']['replies']
    # 提取每条数据内容: for循环遍历
    for index in replies:
        message = index['content']['message'].replace('\n', ',')  # 评论
        like = index['like']  # 点赞
        name = index['member']['uname']  # 昵称
        sex = index['member']['sex']  # 性别
        location = index['reply_control']['location'].replace('IP属地：', '')  # 属地
        dit = {
            '昵称': name,
            '性别': sex,
            'IP': location,
            '评论': message,
            '点赞': like,
        }
        # 保存数据
        csv_writer.writerow(dit)
        print(dit)
    # 下一页请求参数
    next_offset = json_data['data']['cursor']['pagination_reply']['next_offset']
    next_page = re.findall('cursor\":(\d+)', next_offset)[0]
    print(next_page)
    return next_page


if __name__ == '__main__':
    """创建文件对象,保存数据内容"""
    f = open('data1.csv', mode='w', encoding='utf-8-sig', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=[
        '昵称',
        '性别',
        'IP',
        '评论',
        '点赞',
    ])
    csv_writer.writeheader()
    next_page = '7024'
    for page in range(1, 11):
        next_page = get_content(next_page)