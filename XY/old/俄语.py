import csv
import time
import threading
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook
import pandas as pd

ua = UserAgent()


threads = []
f = open('../详情1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['title','link'])
csv_writer.writeheader()
df = pd.read_excel('links.xlsx')
column_name = 'ln'
links = df[column_name]
for link in links:

    headers = {
        'User-Agent': ua.random
    }

    response = requests.get(url=link, headers=headers).text

    soup = BeautifulSoup(response, 'html.parser')

    paragraphs = soup.find_all(class_='Paragraph_paragraph__nYCys')
    # titles = soup.select('#content_box > div > main > section:nth-child(2) > div.NewsHeader_upper_text_block__oUUSZ > h1')
    # tims = soup.select('#content_box > div > main > section:nth-child(2) > div.NewsHeader_upper_text_block__oUUSZ > div > div > div > span')
    merged_text = '\n'.join([p.get_text(strip=True) for p in paragraphs])


    # 将合并后的文本内容写入Excel的第一个单元格
    dit = {'title': merged_text,
           'link':link}

    csv_writer.writerow(dit)
    print(link+'  successfully')





















