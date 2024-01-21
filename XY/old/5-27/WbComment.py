
"""
    Author:黄杰
    Create_Time：2024-05-25
    编写程序：爬取微博XXX话题中用户昵称、头像、发布地址、发布时间、评论文本数据，并进行数据存储
"""
import json
import time  # 导入time模块
import csv   # 导入csv模块
import requests  # 导入requests库，用于发送HTTP请求

# 定义get_one_page方法，获取每一页评论目标数据
def get_one_page(params):
    """
    :param params: get请求需要的参数，数据类型为字典
    :return:  max_id: 请求所需的另一个参数
    """
    url = "https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=5033875395053100&is_show_bulletin=2&is_mix=0&count=10&uid=1699432410&fetch_level=0&locale=zh-CN"  # 给定评论网址

    resp = requests.get(url, headers=headers, params=params)  # 发送请求
    try:
        resp.encoding = 'utf-8'
        data_list = resp.json()["data"]
    except (UnicodeDecodeError, ValueError):
        text = resp.content.decode('utf-8', 'ignore')
        data_list = json.loads(text)["data"]
    # 获取响应的json数据
    # 依次循环获取页面中每一条用户数据信息，包括用户昵称、头像url、发布地址、发布时间、评论文本数据
    for data in data_list:
        data_dict = {
            "screen_name" : data["user"]["screen_name"],
            "profile_image_url" : data["user"]["profile_image_url"],
            "location" : data["user"]["location"],
            "created_time" : data["created_at"].replace("+0800",""),
            "text" : data["text_raw"]
        }
        # 依次打印数据爬取的数据
        print(
            f'昵称：{data_dict["screen_name"]}\n头像:{data_dict["profile_image_url"]}\n地址:{data_dict["location"]}\n发布时间:{data_dict["created_time"]}\n评论内容:{data_dict["text"]}')
        # 每一条数据进行*分隔
        print("=" * 90)
        # 依次调用saveData方法进行保存
        saveData(data_dict)
    # 获取数据中max_id值
    max_id = resp.json()["max_id"]
    # 判断max_id值是否为真，为真则返回对应的值，否则返回空数据
    if max_id:
        return max_id
    else:
        return

# 定义get_all_data方法，获取所有数据
def get_all_data(params):
    """
    :param params: get请求需求的参数，数据类型为字典
    :return:
    """
    max_id = get_one_page(params)  # 调用get_one_page方法，返回max_id值
    params["max_id"] = max_id  # 重新给params字典中max_id进行赋值
    params["count"] = 20  # 给params字典中count进行赋值
    while max_id:  # 当max_id参数为真时，调用get_one_page方法
        params["max_id"] = max_id
        time.sleep(.5)
        max_id = get_one_page(params)

# 定义saveData方法，进行数据保存
def saveData(data_dict):
    """
    :param data_dict: 要保存的数据，形式为dict类型
    :return:
    """
    writer.writerow(data_dict)

# 主函数
if __name__ == '__main__':
    uid = input("请输入作者id: ")  # 输入用户id
    id_str = input("请输入您要爬取的微博话题的英文id: ")  # 输入微博话题英文id
    fileName = input("请输入要保存的文件名: ")  #输入文件保存名
    # 定义请求头
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "x-requested-with":"XMLHttpRequest",
        "referer":"https://weibo.com/1699432410/OedfJlcxC".format(id_str),
        "cookie":'SINAGLOBAL=1238919649132.5305.1702477070392; UOR=,,login.sina.com.cn; ULV=1714052219878:4:1:1:3989475882846.667.1714052219877:1709639227981; XSRF-TOKEN=62g4NEXD45byB2KrD6LerV0G; SUB=_2A25LUAX5DeRhGeFH61US8yfNyTqIHXVoLAcxrDV8PUNbmtAGLUilkW9NeAxp1hSusjL82jTsBuPwiMrUtUg0mwVP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5_FnWjnCSuyyf7e4Ja-kUY5JpX5KzhUgL.FoM4ehM0e0.peoq2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMN1K5Ne0e4eKzc; ALF=02_1719403177; WBPSESS=yMTjzav5NEnm7oeChW6rmMSOzMRaaa2DOCb220peUko3Jrd17I7AGgrZJeeFyIkot1hO5whc5HURbyQmy-7BMPXiDk8ujwp0NuAQd8so23BMhvBdGOozjX8vEB-ysNcCqT4RdrKdcYve5ewLL5iQJw==',
        "x_xsrf_token":"9_o_eJJLCQWGjzB_bjAr9Pp7"
    }

    # 定义列表
    header = ["screen_name","profile_image_url","location","created_time","text"]
    #打开文件
    f = open(f"C:/Users/D_Wang/PycharmProjects/Spider_dome/XY/5-27/test/{fileName}.csv","w",encoding='utf-8-sig',newline="")
    # 创建写入对象，写入数据表头
    writer = csv.DictWriter(f,header)
    writer.writeheader()

    # 定义get请求的参数
    params = {
        "is_reload": 1,
        "id": id_str,
        "is_show_bulletin": 2,
        "is_mix": 0,
        "count": 10,
        "uid": int(uid)
    }
    #调用get_all_data方法，爬取数据
    get_all_data(params)
    # 关闭文件
    f.close()
    # 控制台打印数据爬取完毕
    print("数据爬取完毕。")

