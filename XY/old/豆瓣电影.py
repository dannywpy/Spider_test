import csv
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from pandas.io import json
f = open('2023_link.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['link'])
csv_writer.writeheader()
ua = UserAgent()
headers =  {
'User-Agent': ua.random,
    'Host':'m.douban.com',
    'Referer':'https://movie.douban.com/explore',
    'Origin':'https://movie.douban.com',
    'Cookie':'ll="108296"; bid=AYGYUTaUnJg; douban-fav-remind=1; ap_v=0,6.0; __utma=30149280.976247145.1701872346.1713860751.1715946149.5; __utmb=30149280.0.10.1715946149; __utmc=30149280; __utmz=30149280.1715946149.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gads=ID=c60d0f2283332461:T=1713860753:RT=1715946481:S=ALNI_MbiGOftoREUVY4hMNWEzVt6McExNg; __gpi=UID=00000df6ec8a49eb:T=1713860753:RT=1715946481:S=ALNI_Mak5Im7vIu6iY74lLnEediSid13vA; __eoi=ID=37c20f4aac301cae:T=1713860753:RT=1715946481:S=AA-AfjYld1nYLEgDSqY4dkyNZRZS'
}
tim = '2023'
for i in range(1,26):
    num = i * 20
    response = requests.get(url=f'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count={num}&selected_categories=%7B%7D&uncollect=false&tags={time}',headers=headers)

    data = json.loads(response.text)

    # 获取 items 列表
    items = data.get("items", [])

    # 遍历 items 列表，打印每个项目的 id
    for item in items:
        link_id = item.get("id")
        link = 'https://movie.douban.com/subject/' + link_id
        dit = {
            'link':link
        }
        csv_writer.writerow(dit)
        print(link)
        time.sleep(2)
















