import requests
import csv
from bs4 import BeautifulSoup
import json
f = open('data.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '价格', '评论', '店名', '详情页'])
# 写入表头
csv_writer.writeheader()
url = 'https://www.gkd.edu.cn/'

headers = {
    "Cookie":"Hm_lvt_ef4a544159e5abd4f775c427fd66a685=1703679031,1703679049; Hm_lpvt_ef4a544159e5abd4f775c427fd66a685=1703679287",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

# 定位 HTML 元素
element = soup.find_all('ul',class_='dropdown-menu')

# 获取 HTML 元素中的文本
colleges = element[1].text

print(colleges)



