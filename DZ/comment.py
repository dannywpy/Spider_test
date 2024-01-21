import time

import schedule

from IP import IP_GET
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
def DZ():
    f = open('肉本家·炭烤肉(杭州浙大总店) -good评.csv', mode='a', encoding='utf-8-sig', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=['用户名', '时间','评论'])
    # 写入表头
    csv_writer.writeheader()
    headers = {
        "Cookie":'_lxsdk_cuid=18be225b61ba-05207df8083274-26031051-240000-18be225b61cc8; _lxsdk=18be225b61ba-05207df8083274-26031051-240000-18be225b61cc8; _hc.v=57a9fe96-f305-bacc-18fe-ef62c6e4af4e.1700306204; s_ViewType=10; WEBDFPID=803924z1y11555w0z5789223z4u7w40381yv773y78597958v6zvwz49-2015666268886-1700306268886MGWUSWAfd79fef3d01d5e9aadc18ccd4d0c95073668; ctu=8c7b21b14372bc0f51094231e05b222efef4e108874aac450a9f9224429bb419; fspop=test; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1708521751,1708527817,1708527944,1708947862; cy=3; cye=hangzhou; qruuid=3055a6f8-888e-4974-a0e1-787c300a7140; dplet=4e3c83b0b159771aecba97a0860129ca; dper=0202822284ff034b55f9699960557179594c715c9bbadc434815fff3fcc56d89c6517d10851e96c8993c5a524b3eaf7ac05d4e37a1a73a8fc4e700000000501e0000ede4225243498b95eb528bd7a322097f3e83f97d3e8a50477dadaa60c491e18312f84fb0c795ebae97209b9a1d6f0b43; ll=7fd06e815b796be3df069dec7836c3df; ua=danny; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1708949305; _lxsdk_s=18de53aefe0-b67-ce6-1c1%7C%7C636',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    for i in range(1,8):
        shop = 'l8GtFO9oMLF3JcA2'
        com_type = 'good'
        link = f'https://www.dianping.com/shop/{shop}/review_all/p{i}?queryType=reviewGrade&queryVal={com_type}'
        print(link)
        # proxies = IP_GET.ip_get()
        time.sleep(2)
        response = requests.get(url = link,headers=headers)
        if response.status_code == 200:
            da = response.text

            data = da.replace(" Hide", "")
            soup = BeautifulSoup(data, 'html.parser')
            names = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.dper-info > a')
            dates = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.misc-info.clearfix > span.time')
            class_comment = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li> div > div.review-words')
            #循环遍历数据并追加到DataFrame
            # 创建一个空的 DataFrame
            df = pd.DataFrame()
            # 遍历 names、dates 和 class_comment 列表
            for name, date, long_comment in zip(names, dates, class_comment):
                # 创建一个字典，包含用户名、评论时间和评论内容
                dit = {'用户名': name.text, '时间': date.text, '评论': long_comment.text}
                csv_writer.writerow(dit)

            print(f'第{i}页successfully')

            i += 1
        else:
            print(f'现在是第{i}页，失败' )
            raise Exception('请求失败！')
if __name__ == '__main__':
    DZ()













