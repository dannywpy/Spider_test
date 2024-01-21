import re
import time
from IP.IP_GET import ip_get
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

with open('ZJJ_SLGY1.csv', mode='w', encoding='utf_8_sig', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=['用户名', '星级','时间','长评论'])
    csv_writer.writeheader()

    headers = {
        "Cookie":'_lxsdk_cuid=18be225b61ba-05207df8083274-26031051-240000-18be225b61cc8; _lxsdk=18be225b61ba-05207df8083274-26031051-240000-18be225b61cc8; _hc.v=57a9fe96-f305-bacc-18fe-ef62c6e4af4e.1700306204; s_ViewType=10; WEBDFPID=803924z1y11555w0z5789223z4u7w40381yv773y78597958v6zvwz49-2015666268886-1700306268886MGWUSWAfd79fef3d01d5e9aadc18ccd4d0c95073668; ctu=8c7b21b14372bc0f51094231e05b222efef4e108874aac450a9f9224429bb419; fspop=test; cy=198; cye=zhangjiajie; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1703922128,1703922496,1703930375,1703996096; qruuid=aed72249-9fe7-48b1-9c0e-a53198652626; dplet=5eb1a6036cafa1da36f77600f7644d48; dper=2cf1c3ba4f0266b1d5e1276618ba30a2c3a204b605b650e75b79cd37e0993bf88f4573b0264e9cf26db789cb079c7219def75f6fa6cb3cc4717b946c1a7fc100; ll=7fd06e815b796be3df069dec7836c3df; ua=danny; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1703996949; _lxsdk_s=18cbe14fe27-e9f-cd0-3e7%7C%7C2056',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        'Host': 'www.dianping.com',
    }

    dit = {}

    for i in range(2,50):
        link = f'https://www.dianping.com/shop/k1Mqa9EsNB6wOei5/review_all/p{i}'
        print(link)
        proxies = ip_get()
        response = requests.get(url = link,headers=headers,proxies=proxies)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            names = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.dper-info > a')
            starts = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.review-rank > span')
            dates = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.misc-info.clearfix > span.time')
            class_comment = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.review-words')
            text = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li:nth-child(8) > div')
            data_long = []
            for name, start, date,long_comment,comment,text in zip(names, starts, dates,class_comment,text):
                print(text)
                dit = {
                    '用户名': name.text.strip(),
                    '星级': start,
                    '时间': date.text,
                    '长评论': long_comment.text.strip().replace('\n', '')

                }

                data_long.append(dit)

                csv_writer.writerow(dit)
                i += 1
        else:
            print(f'现在是第{i}页，失败' )
            raise Exception('请求失败！')














