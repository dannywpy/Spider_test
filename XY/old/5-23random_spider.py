import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    'User-Agent': ua.random,
    "Cookie": 'ASP.NET_SessionId=rrowqwvad0o3oc45y3oyfi55; Hm_lvt_f48cedd6a69101030e93d4ef60f48fd0=1715782911,1715870021; __51cke__=; __gads=ID=d081f14b139332e2:T=1715782910:RT=1715870019:S=ALNI_MbGeAQIUXbFLGIRkAAA61vGUaPecg; __gpi=UID=00000e1e55416bc2:T=1715782910:RT=1715870019:S=ALNI_MZpwhxIqv-X7OHQZohXuE8ZGHS2YQ; __eoi=ID=c66282bd0d775649:T=1715782910:RT=1715870019:S=AA-AfjYgYPhaX0jXIHLtPvejjl4S; __tins__21287555=%7B%22sid%22%3A%201715870021302%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201715872046443%7D; __51laig__=5; Hm_lpvt_f48cedd6a69101030e93d4ef60f48fd0=1715870246'
}

link = 'http://www.tianqihoubao.com/weather/top/beilun.html'
response = requests.get(url=link, headers=headers).text
soup = BeautifulSoup(response, 'html.parser')
td_elements = soup.find_all('td')
td_values = [td.get_text(strip=True).replace('\r\n', '').strip() for td in td_elements]
data = []
for i in range(0, len(td_values), 8):
    # 从第五个元素开始提取数据
    row = [val if val else '-' for val in td_values[i+4:i+8]]
    data.append(row)

# 打开CSV文件进行写入
with open('weather_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 写入列标题
    writer.writerow(['日期', '天气状况', '最低气温/最高气温', '风力风向(夜间/白天)'])
    # 写入数据
    writer.writerows(data)

print(f'Successfully processed: {link}')
