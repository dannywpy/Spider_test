import csv
import re
import threading
import time
from random import random

import chardet
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 '
              'Safari/537.36 Edg/124.0.0.')

headers = {'User-Agent': user_agent,
           'Cookie':'zh_choose=n; maxPageNum10044770=374; wzws_sessionid=gDI0MDg6ODIwYzpiNjBhOmY5NzA6Nzg4Mzo0ZTViOjgxOWI6YjIzOKBmT0dkgWExNmRkYYI2MGZlZDA=; __weac=15971110; __weaa=15971110.822125366.1716466082.1716471655.1716474502.3; __weab=15971110.1716474502.1716474502.1716474502.1; __wead=15971110.1716466082.1716471655.1716474502.3',
            'Host':'www.audit.gov.cn',
           'Referer':'https://www.audit.gov.cn/n4/n19/index.html'
           }
f = open('要闻1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['title','content','原始链接'])
csv_writer.writeheader()


df = pd.read_excel('ln.xlsx')
column_name = 'ln'
links = df[column_name]
for link in links:

    response = requests.get(url=link, headers=headers)
    content_type = response.headers.get('Content-Type')
    encoding = chardet.detect(response.content)['encoding']

    decoded_content = response.content.decode(encoding)

    soup = BeautifulSoup(decoded_content, 'html.parser')
    titles = soup.select('body > div.content > div.con-page-box > div > div.con-article-title-box')
    text = soup.select('#textSize')
    for t,title in zip(text,titles):
        content = t.get_text()
        tl = title.get_text()
        dit = {'title': content,
               'content': tl,
               '原始链接': link
               }
        csv_writer.writerow(dit)
        print(f'successful {link}')



