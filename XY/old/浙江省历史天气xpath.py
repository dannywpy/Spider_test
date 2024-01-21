
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()



headers = {
'User-Agent': ua.random,
    "Cookie":'ASP.NET_SessionId=rrowqwvad0o3oc45y3oyfi55; Hm_lvt_f48cedd6a69101030e93d4ef60f48fd0=1715782911,1715870021; __51cke__=; __gads=ID=d081f14b139332e2:T=1715782910:RT=1715870019:S=ALNI_MbGeAQIUXbFLGIRkAAA61vGUaPecg; __gpi=UID=00000e1e55416bc2:T=1715782910:RT=1715870019:S=ALNI_MZpwhxIqv-X7OHQZohXuE8ZGHS2YQ; __eoi=ID=c66282bd0d775649:T=1715782910:RT=1715870019:S=AA-AfjYgYPhaX0jXIHLtPvejjl4S; __tins__21287555=%7B%22sid%22%3A%201715870021302%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201715872046443%7D; __51laig__=5; Hm_lpvt_f48cedd6a69101030e93d4ef60f48fd0=1715870246'
}

response = requests.get(url='http://www.tianqihoubao.com/weather/province.aspx?id=330000',headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

base_url = 'http://www.tianqihoubao.com/weather/'
urls = []
for link in links[13:84]:
    url = base_url + link.get('href')
    urls.append(url)
    print(link.get('href'))
    for ul in urls:
        time.sleep(2)
        print(ul)
        response = requests.get(url=ul, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        td_elements = soup.find_all('td')
        td_values = [td.get_text(strip=True).replace('\r\n', '').strip() for td in td_elements]
        data = []

        # 假设 response.text 包含了您想要解析的 HTML 内容
        html = response

        # 创建一个 XPath 解析器
        parser = etree.HTMLParser()
        tree = etree.fromstring(html, parser)

        # 提取 "城市" 列的文本
        city_text = tree.xpath('//*[@id="content"]/h1')[0]
        print(city_text)

        # 提取 "日期" 列的文本
        date_text = tree.xpath('//tr/td[2]/b/text()')[0]
        print(date_text)

        # 提取 "白天" 列的文本
        light = tree.xpath('//tr/td[3]/b[1]/text()')
        print(light[0])

        # 提取 "夜间" 列的文本
        night = tree.xpath('//tr/td[4]/b[1]/text()')
        print(night[0])

        stata = tree.xpath('//tr[2]/td[1]/b/text()')
        print(stata[0])

        high = tree.xpath('//tr[2]/td[3]/b[1]/text()')
        print(high[0])

        low = tree.xpath('//tr[2]/td[4]/b[1]/text()')
        print(low[0])
        soup = BeautifulSoup(response, 'html.parser')
        td_elements = soup.find_all('td')
        td_values = [td.get_text(strip=True).replace('\r\n', '').strip() for td in td_elements]
        for td_value in td_values:
            print(td_value)

        print(f'Successfully processed: {ul}')


















