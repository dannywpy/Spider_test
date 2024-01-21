import csv
import json
import datetime
import time

import chardet
import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()
f = open('test1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['类别','证书编号','时间','机构名称','当前状态','姓名'])
csv_writer.writeheader()
df = pd.read_excel('ln.xlsx')
column_name = 'ln'
accountIds = df[column_name]
for accountId in accountIds:
    url = f'https://gs.amac.org.cn/amac-infodisc/api/pof/person/{accountId}'
    headers = {
        'User-Agent':ua.random,

    }
    time.sleep(1)
    response = requests.get(url=url,headers=headers).text
    json_data = json.loads(response)
    name = json_data['userName']
    HisturyList = json_data['personCertHistoryList']
    for i in range(len(HisturyList)):
        certCode = HisturyList[i]['certCode']
        creationDate = HisturyList[i]['creationDate']
        orgName = HisturyList[i]['orgName']
        certName = HisturyList[i]['certName']
        statusName = HisturyList[i]['statusName']


        # 将时间戳转换为datetime对象
        timestamp = creationDate / 1000  # 将毫秒转换为秒
        dt = datetime.datetime.fromtimestamp(timestamp)
        dit = {
            '类别':certName,
            '证书编号':certCode,
            '时间':dt,
        '机构名称':orgName,
        '当前状态':statusName,
        '姓名':name
        }
        csv_writer.writerow(dit)
        print(certName,certCode,dt,orgName,statusName,name)
    print(f'successfully     {url}')






