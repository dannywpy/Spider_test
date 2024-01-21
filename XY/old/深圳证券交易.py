import time
from random import random
import json
import requests
import csv
f = open('2021_减少注册资本.csv', mode='a', encoding='utf_8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['下载链接','证券代码','公告标题'])
csv_writer.writeheader()

rand = random()

header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
data = {"seDate": ["2021-01-01", "2021-12-31"],
            "searchKey": ["减少注册资本"],
            "channelCode": ["listedNotice_disc"],
            "pageSize": 50,
            "pageNum": 6
            }


url = f'https://www.szse.cn/api/disc/announcement/annList?random={rand}'

response = requests.post(url=url,headers=header,json=data)
da = response.text
json = json.loads(da)
for i in range(0,2):
    link = json['data'][i]['id']
    code = json['data'][i]['secCode']
    name = json['data'][i]['title']
    dit = {

        '下载链接':link,
        '证券代码':code,
        '公告标题':name
    }
    csv_writer.writerow(dit)
    i += 1

print('完成(＾－＾)V')

















