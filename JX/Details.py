import time

import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup
f = open('C:/Users/D_Wang/PycharmProjects/Spider_dome/JX/details/混凝土机械详情.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['名称', '介绍','详情'])
csv_writer.writeheader()
df = pd.read_excel('混凝土机械.xlsx')
column_name = '超链接'
links= df[column_name]
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
i = 0
for link in links:
    response = requests.get(url=link, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        names = soup.select('body > div.container.dtop.cl > div.dtopin > h1')
        presents = soup.select('body > div.container.dtop.cl > div.dtopin > p')
        details = soup.select('body > div.container.dtop.cl > div.dtopin > div.dtopparam > dl')
        dit = {
                        '名称': names[0].text,
                        '介绍': presents[0].text,
                        '详情': details[0].text
                    }
        csv_writer.writerow(dit)
        print(f'成功{link},{i}页')
        i += 1
    else:
        print(f'现在是第{link}页，失败')
        continue


