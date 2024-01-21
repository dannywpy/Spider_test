import requests
import time

import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup
f = open('C:/Users/admin/spider_Test/pythonProject/2019.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '作者','年份','link','abstract'])
csv_writer.writeheader()

# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#     }
for i in range(1,274):
    link = f'https://www.nature.com/ncomms/research-articles?searchType=journalSearch&sort=PubDate&year=2019&page={i}'
    response = requests.get(url=link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.select(
            '#new-article-list > div > ul > li > div > article > div.c-card__layout.u-full-height > div.c-card__body.u-display-flex.u-flex-direction-column > h3 > a')
        author = soup.select(
            '#new-article-list > div > ul > li > div > article > div.c-card__layout.u-full-height > div.c-card__body.u-display-flex.u-flex-direction-column > ul')
        year = soup.select('#new-article-list > div > ul > li > div > article > div.c-card__section.c-meta > time')
        abstract_link = soup.select(
            '#new-article-list > div > ul > li > div > article > div.c-card__layout.u-full-height > div.c-card__body.u-display-flex.u-flex-direction-column > h3 > a')
        abstract = soup.select(
            '#new-article-list > div > ul > li > div > article > div.c-card__layout.u-full-height > div.c-card__body.u-display-flex.u-flex-direction-column > div')

        for name, author, year, abstract_link, abstract in zip(name, author, year, abstract_link, abstract):
            link = abstract_link.get('href')
            dit = {
                '标题': name.text,
                '作者': author.text,
                '年份': year.text,
                'link': link,
                'abstract': abstract.text
            }
            csv_writer.writerow(dit)

        print(f'第{i}页成功')
        i += 1
    else:
        print(f'第{i}页失败')
        continue

