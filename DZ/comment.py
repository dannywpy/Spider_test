import re
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

with open('ZJJ_SLGY1.csv', mode='w', encoding='utf_8_sig', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=['用户名', '星级','时间','长评论','短评论'])
    csv_writer.writeheader()


    headers = {
        "Cookie":"_lxsdk_cuid=18be225b61ba-05207df8083274-26031051-240000-18be225b61cc8; _lxsdk=18be225b61ba-05207df8083274-26031051-240000-18be225b61cc8; _hc.v=57a9fe96-f305-bacc-18fe-ef62c6e4af4e.1700306204; s_ViewType=10; WEBDFPID=803924z1y11555w0z5789223z4u7w40381yv773y78597958v6zvwz49-2015666268886-1700306268886MGWUSWAfd79fef3d01d5e9aadc18ccd4d0c95073668; ctu=8c7b21b14372bc0f51094231e05b222efef4e108874aac450a9f9224429bb419; fspop=test; cy=198; cye=zhangjiajie; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1703919411,1703922128,1703922496,1703930375; qruuid=7dd1e2b7-97bc-4025-9967-d1bcf00ae58c; dplet=5246b016fc91bce57c9d6090a3375ed9; dper=2cf1c3ba4f0266b1d5e1276618ba30a2babb67f27ec30669c386728eeb925f15f343555c6e0feb7b450ba094d4eeab7f495acd1be7e66827ff7b4ec31ac42e22; ll=7fd06e815b796be3df069dec7836c3df; ua=danny; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1703945440; _lxsdk_s=18cbb0f9651-0a7-779-ff1%7C%7C56",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        'Host': 'www.dianping.com',
    }

    dit = {}

    for i in range(57,799):
        link = f'https://www.dianping.com/shop/k1Mqa9EsNB6wOei5/review_all/p{i}'
        print(link)
        time.sleep(20)
        response = requests.get(url = link,headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            names = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.dper-info > a')
            starts = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.review-rank > span')
            dates = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.misc-info.clearfix > span.time')
            class_comment = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.review-words')
            class_hide = soup.select('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.review-words.Hide')

            data_long = []


            for name, start, date,long_comment,comment in zip(names, starts, dates,class_hide,class_comment):

                dit = {
                    '用户名': name.text.strip(),
                    '星级': start,
                    '时间': date.text,
                    '长评论': long_comment.text.strip().replace('\n', ''),
                    '短评论': comment.text.strip().replace('\n', '')
                }

                data_long.append(dit)

                csv_writer.writerow(dit)
                i += 1
        else:
            print(f'现在是第{i}页，失败' )
            raise Exception('请求失败！')














