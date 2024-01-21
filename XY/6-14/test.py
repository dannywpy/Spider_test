import csv
import json
import re

import requests
from bs4 import BeautifulSoup
f = open('movies.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['累计票房', '首日票房', '首周票房 ', '预测', '分账', '片方', '影院', '其他', '物料', '微博', '微信', '百度','date','real'])
csv_writer.writeheader()
cookies = {
    '^Cookie: Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1716380371',
    '_lxsdk_cuid': '18fa03e073bc8-08831fef0c7635-26001d51-240000-18fa03e073bc8',
    '_lxsdk': '89F5DEE0183511EFA7D89144D35F720D0AF124EB6E4F4B3882286D2DB401DAB9',
    'theme': 'moviepro',
    '_lxsdk_s': '19016fab025-1f5-002-be1^%^7C^%^7C45^',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://piaofang.maoyan.com/rankings/year',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    '^sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    '^sec-ch-ua-platform': '^\\^Windows^\\^^',
}

response = requests.get('https://piaofang.maoyan.com/movie/257706', headers=headers, cookies=cookies)
soup = BeautifulSoup(response.text,'html.parser')
contens = soup.find_all(class_='info-detail-col')

# 使用正则表达式匹配
match = re.search(r'(?s)(?<=</div>).*?<script id="pageData" type="application/json">(.*?)</script>', response.text, re.DOTALL)

# 如果找到匹配项，则打印结果
if match:
    js_data = match.group(1).strip()
    json_data = json.loads(js_data)
    date_n = json_data["boxshowChartData"]["chartData"]["box"]["date"]
    real_data = json_data["boxshowChartData"]["chartData"]["box"]["real"]
    dit = {
        '累计票房': contens[0].text,
        '首日票房': contens[1].text
        , '首周票房 ': contens[2].text, '预测': contens[3].text, '分账': contens[4].text, '片方': contens[5].text,
        '影院': contens[6].text, '其他': contens[7].text, '物料': contens[8].text, '微博': contens[9].text,
        '微信': contens[10].text, '百度': contens[11].text,
        'date':date_n,
        'real':real_data

    }
    csv_writer.writerow(dit)
else:
    print("No JSON data found")







