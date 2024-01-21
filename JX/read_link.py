import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import re
import csv

f = open('新能源.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['名称', '图片链接','超链接'])
# 写入表头
csv_writer.writeheader()

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# 读取Excel文件
df = pd.read_excel('link.xlsx')

# 指定要读取的列名
column_name = 'link'

# 读取指定列的数据
links= df[column_name]

# 打印列数据

def jpg(i):
    try:
        response = requests.get(url=url,headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            jpgs = soup.select('body > div.container.cl > div.right.pagelist_right > div.product_list.cl > div > a > img')
            names = soup.select('body > div.container.cl > div.right.pagelist_right > div.product_list.cl > div > h2 > a')
            links = soup.select('body > div.container.cl > div.right.pagelist_right > div.product_list.cl > div > a')
            data_long = []
            for jpg,name,link in zip(jpgs,names,links):

                link = link.get('href')
                jpg = jpg.get('src')
                dit = {
                    '名称': name.text,
                    '图片链接': jpg,
                    '超链接': link

                }
                csv_writer.writerow(dit)
            print(f'成功{i}页')
            i += 1
        else:
            print(f'现在是第{i}页，失败')
            raise Exception('请求失败！')
            continue_running()
    except requests.exceptions.RequestException as e:
        # 处理请求异常
        print(f'Request failed: {str(e)}')
        # 继续执行其他代码
        continue_running()
for link in links:
    url_a = link
    for i in range(1, 10):
        time.sleep(3)
        if i == 1:
            url = url_a
            jpg(i)
        else:
            url = url_a + f"?p={i}"
            jpg(i)













