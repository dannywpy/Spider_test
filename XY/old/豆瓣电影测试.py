import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from pandas.io import json
f = open('2023.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['names','导演','编剧','演员','类型','stata','language','tim','score','comment_number','starts','texts','link'])
csv_writer.writeheader()
link='https://movie.douban.com/subject/36207371/'
ua = UserAgent()
headers =  {
'User-Agent': ua.random,
    'Referer':'https://movie.douban.com/explore',
    'Cookie':'ll="108296"; bid=AYGYUTaUnJg; douban-fav-remind=1; ap_v=0,6.0; __utma=30149280.976247145.1701872346.1713860751.1715946149.5; __utmb=30149280.0.10.1715946149; __utmc=30149280; __utmz=30149280.1715946149.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gads=ID=c60d0f2283332461:T=1713860753:RT=1715946481:S=ALNI_MbiGOftoREUVY4hMNWEzVt6McExNg; __gpi=UID=00000df6ec8a49eb:T=1713860753:RT=1715946481:S=ALNI_Mak5Im7vIu6iY74lLnEediSid13vA; __eoi=ID=37c20f4aac301cae:T=1713860753:RT=1715946481:S=AA-AfjYld1nYLEgDSqY4dkyNZRZS'
}
response = requests.get(url=link,headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
elements = soup.find_all(attrs={'property': 'v:initialReleaseDate'})

for element in elements:
    text_value = element.get('content')
    print(f"Text value for 'v:initialReleaseDate': {text_value}")










