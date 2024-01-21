import requests
from bs4 import BeautifulSoup

url = 'https://www.szse.cn/disclosure/listed/bulletinDetail/index.html?88537f76-fb27-43e6-946d-a2cfa16448b6'

header = {
    "Host":"www.szse.cn",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url=url,headers=header)
response.encoding = 'utf-8'
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

name = soup.select('body > div.g-container-wrap > div > div > div.bd_header.clearfix > div.bd-title.pull-left > h2')

print(name)




















