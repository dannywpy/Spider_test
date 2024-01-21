import time

import schedule

import IP_GET
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
def DZ():
    f = open('ZBcha评.csv', mode='w', encoding='utf-8-sig', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=['用户名', '时间','评论'])
    # 写入表头
    csv_writer.writeheader()
    headers = {
        "Cookie":'_lxsdk_cuid=18be225b61ba-05207df8083274-26031051-240000-18be225b61cc8; _lxsdk=18be225b61ba-05207df8083274-26031051-240000-18be225b61cc8; _hc.v=57a9fe96-f305-bacc-18fe-ef62c6e4af4e.1700306204; s_ViewType=10; WEBDFPID=803924z1y11555w0z5789223z4u7w40381yv773y78597958v6zvwz49-2015666268886-1700306268886MGWUSWAfd79fef3d01d5e9aadc18ccd4d0c95073668; ctu=8c7b21b14372bc0f51094231e05b222efef4e108874aac450a9f9224429bb419; fspop=test; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1708154947,1708331271,1708428266; cy=145; cye=zibo; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; qruuid=2ad3426a-b8f9-4122-92fa-87cafdcacbc4; dplet=1aa68e3815aedb86690a27f2f48abd13; dper=0202e4208dc6075cdb1790cc76e4d77a3d4bde27837805953fcbfddd7834c443a85d19974e334b13c125ccd1c61182d7be77140f2f9a146aabc700000000501e00006eda8d1449d99919078364bfb0726cb7c0d3941ef7606704f1972ce902fca298c88f55e55991451292cf104e2b01d536; ll=7fd06e815b796be3df069dec7836c3df; ua=danny; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1708434264; _lxsdk_s=18dc66fda27-1d9-93f-a81%7C%7C1346',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    shop = 'H9emH3dGy4eOb1x3'
    for i in range(1,11):
        link = f'https://www.dianping.com/shop/{shop}/review_all/p{i}?queryType=reviewGrade&queryVal=bad'
        print(link)
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
                print(dit)
            print(f'第{i}页successfully')

            i += 1
        else:
            print(f'现在是第{i}页，失败' )
            raise Exception('请求失败！')
if __name__ == '__main__':
    DZ()













