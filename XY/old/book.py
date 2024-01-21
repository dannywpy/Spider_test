import csv
import time

import requests
from bs4 import BeautifulSoup
f = open('book嗯.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['姓名', '简介','link'])
csv_writer.writeheader()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',

}
for i in range(73,210):
    time.sleep(1)
    response = requests.get(url=f'https://www.bookschina.com/kinder/54000000_0_0_11_0_1_{i}_0_0_/',headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_name = soup.select('#container > div > div.listLeft > div.bookList > ul > li > div.infor > h2 > a')
    abstracts = soup.select('#container > div > div.listLeft > div.bookList > ul > li > div.infor > p')
    links = [img['data-original'] for img in soup.select('#container > div > div.listLeft > div.bookList > ul > li > div.cover > a > img')]
    for name,abstract,link in zip(book_name,abstracts,links):
        dit = {
            '姓名': name.text,
            '简介': abstract.text,
            'link': link
        }
        csv_writer.writerow(dit)
    print(f'已完成{i}')













