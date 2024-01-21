import csv
import json
from bs4 import BeautifulSoup
import requests

cookies = {
    '^Cookie: Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1716380371',
    '_lxsdk_cuid': '18fa03e073bc8-08831fef0c7635-26001d51-240000-18fa03e073bc8',
    '_lxsdk': '89F5DEE0183511EFA7D89144D35F720D0AF124EB6E4F4B3882286D2DB401DAB9',
    'theme': 'moviepro',
    '_lxsdk_s': '19016fab025-1f5-002-be1^%^7C^%^7C45^',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://piaofang.maoyan.com/movie/257706',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Uid': 'e938ed4b6b3d30bffbfbba13ccb286a83af62374',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    '^sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    '^sec-ch-ua-platform': '^\\^Windows^\\^^',
}

response = requests.get('https://piaofang.maoyan.com/movie/257706/moresections', headers=headers, cookies=cookies)
json_data = json.loads(response.text)
js_data = json_data['sectionHTMLs']['techSection']
html_data = js_data['html']
soup = BeautifulSoup(html_data,'html.parser')
text = soup.find(class_='tech-section')
print(text.text)