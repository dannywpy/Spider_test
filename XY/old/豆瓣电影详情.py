import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from pandas.io import json
f = open('2023.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['names','导演','编剧','演员','类型','stata','language','tim','score','comment_number','texts','link'])
csv_writer.writeheader()
df = pd.read_excel('2023_link.xlsx')
column_name = 'link'
links = df[column_name]

ua = UserAgent()
headers =  {
'User-Agent': ua.random,
    'Referer':'https://movie.douban.com/explore',
    'Cookie':'ll="108296"; bid=AYGYUTaUnJg; douban-fav-remind=1; ap_v=0,6.0; __utma=30149280.976247145.1701872346.1713860751.1715946149.5; __utmb=30149280.0.10.1715946149; __utmc=30149280; __utmz=30149280.1715946149.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gads=ID=c60d0f2283332461:T=1713860753:RT=1715946481:S=ALNI_MbiGOftoREUVY4hMNWEzVt6McExNg; __gpi=UID=00000df6ec8a49eb:T=1713860753:RT=1715946481:S=ALNI_Mak5Im7vIu6iY74lLnEediSid13vA; __eoi=ID=37c20f4aac301cae:T=1713860753:RT=1715946481:S=AA-AfjYld1nYLEgDSqY4dkyNZRZS'
}
for link in links:
    response = requests.get(url=link,headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    names = soup.select('#content > h1 > span:nth-child(1)')
    director = soup.select('#info > span:nth-child(1) > span.attrs > a')
    screnn = soup.select('#info > span:nth-child(3) > span.attrs')
    actor = soup.select('#info > span:nth-child(5) > span.attrs')
    type = soup.select('#info > span:nth-child(8)')
    tim = soup.select('#info > span:nth-child(22)')
    score = soup.select('#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong')
    comment_number = soup.select('#comments-section > div.mod-hd > h2 > span')
    texts = soup.select('#link-report-intra > span')
    for na in names:
        print(na.get_text())
    # elements = soup.find_all(attrs={'property': 'v:initialReleaseDate'})
    print('1')
    for name,dir,scr,act,ty,ti,scor,com,text in zip(names,director,screnn,actor,type,tim,score,comment_number,texts):
        print('2')
        # text_value = element.get('content')
        dit = {'names': name.get_text(),
               '导演': dir.get_text(),
               '编剧': scr.get_text(),
               '演员': act.get_text(),
               '类型': ty.get_text(),
               'tim': ti.get_text(),
               'score': scor.get_text(),
               'comment_number':com.get_text(),
                'texts': text.get_text(),
               'link':link,
               # '上映时间':text_value
               }
        csv_writer.writerow(dit)
        print(dit)
        print(f'{link}   successfully')




