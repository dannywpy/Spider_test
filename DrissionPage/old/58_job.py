import csv
import time

import requests
url = 'https://hf.58.com/quanzhizhaopin/?key=%E7%94%B5%E8%AF%9D%E9%94%80%E5%94%AE&cmcskey=%E7%94%B5%E8%AF%9D%E9%94%80%E5%94%AE&final=1&jump=1&specialtype=gls&search_uuid=PQTismPF4dfeSwY4AnYGwZNZ4N7icjhj&classpolicy=uuid_PQTismPF4dfeSwY4AnYGwZNZ4N7icjhj&search_type=input'

from DrissionPage import ChromiumPage
f = open('58-合肥.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['name'])
csv_writer.writeheader()
page = ChromiumPage()
page.get(url)
for i in range(1,3):
    page.wait.load_start()
    page.scroll.to_location(0,4000)
    time.sleep(0.5)
    page.scroll.to_location(0, 6500)
    time.sleep(0.5)
    page.scroll.to_location(0, 3500)


    skus = page.eles('.fl')
    for sku in skus:
        link = sku.title
        dit = {
            'name': link,

        }
        csv_writer.writerow(dit)


    print(f'successfully   =============={i}页')
    time.sleep(2)
    page.ele('.next').click()

page.close()