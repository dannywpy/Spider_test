import time
import re

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

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

        html_content = response
        # 提取<title>标签中的文本
        title_pattern = r'<title>(.*?)</title>'
        title_match = re.search(title_pattern, html_content, re.S)

        # 提取<meta name="Keywords" ...>中的content
        keywords_pattern = r'<meta name="Keywords" content="(.*?)"'
        keywords_match = re.search(keywords_pattern, html_content, re.S)
        if keywords_match:
            keywords_text = keywords_match.group(1)
            print("Keywords:", keywords_text)

        # 提取<meta name="description" ...>中的content
        description_pattern = r'<meta name="description" content="(.*?)"'
        description_match = re.search(description_pattern, html_content, re.S)
        if description_match:
            description_text = description_match.group(1)
            print("Description:", description_text)

        # 提取日期
        date_pattern = r'<a href=\'/lishi/anji/(\d+)\.html\'>'
        date_match = re.search(date_pattern, html_content)
        if date_match:
            date_text = date_match.group(1)
            print("Date:", date_text)

        # 提取天气现象
        weather_pattern = r'<td >&nbsp;(.*?)</td>'
        weather_matches = re.findall(weather_pattern, html_content)
        if weather_matches:
            weather_text = weather_matches[0]
            print("Weather:", weather_text)

        # 提取风力
        wind_pattern = r'<td>(.*?风 \d-\d级)</td>'
        wind_matches = re.findall(wind_pattern, html_content)
        if wind_matches:
            wind_text = wind_matches[0]
            print("Wind:", wind_text)

        # 提取最高温度
        max_temp_pattern = r'<td>(\d+)℃</td>'
        max_temp_match = re.search(max_temp_pattern, html_content)
        if max_temp_match:
            max_temp_text = max_temp_match.group(1)
            print("Max Temperature:", max_temp_text)

        # 提取天气状况
        condition_pattern = r'<td>(阴|晴|多云|小雨|中雨|大雨|阵雨|雷阵雨)</td>'
        condition_match = re.search(condition_pattern, html_content)
        if condition_match:
            condition_text = condition_match.group(1)
            print("Condition:", condition_text)