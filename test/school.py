import csv
import requests
from bs4 import BeautifulSoup

f = open('collage.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['学院名称', '学院链接','具体专业'])

csv_writer.writeheader()

headers = {
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
base_url = 'https://www.gkd.edu.cn'

dit={}

#学院名称
url = 'https://www.gkd.edu.cn/'

response = requests.get(url, headers=headers)

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

college = soup.select('#bs-example-navbar-collapse-1 > ul > li:nth-child(3) > ul > li> a')

def open():
    if each['href'] == '/zdhgc/':
        program('https://www.gkd.edu.cn/zdhgc/channels/5619.html','body > div:nth-child(5) > div > div.col-sm-9.list-box > ul > li > a')
        program('https://www.gkd.edu.cn/zdhgc/channels/5620.html','body > div:nth-child(5) > div > div.col-sm-9.list-box > ul > li > a')
        print('111')
    elif each['href'] == '/yscm/':
        program(link,'#Hui-navbar > ul > li:nth-child(5) > ul > li > a')
    elif each['href'] == '/xxgc/':
        program(link,'#Hui-navbar > ul > li:nth-child(4) > ul > li> a')
    elif each['href'] == '/wywm/':
        program(link,'#Hui-navbar > ul > li:nth-child(4) > ul > li > a')
    elif each['href'] == '/jzgcxy/':
        program('https://www.gkd.edu.cn/jzgcxy/channels/1056.html','body > div.container > div > div.col-sm-9.list-box > ul > li> a')
    elif each['href'] == '/jkxy/':
        program('https://www.gkd.edu.cn/jkxy/channels/4574.html','body > div.container-lg.bg-white > div > div.col-12.col-sm-7.col-lg-9.mt-3 > div > div.bg-light > ul > li > a')
    elif each['href'] == '/glxy/':
        program('https://www.gkd.edu.cn/glxy/channels/9030.html','body > div.container > div > div.col-sm-9.list-box > ul > li > a')
def program(url, pram):

    response = requests.get(url, headers=headers)

    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    program_BK = soup.select(pram)

    for each in program_BK:
        name = each.text
        print(name)
        dit = {
            '学院名称': c_name,
            '学院链接': link,
            '具体专业': name,
        }
        csv_writer.writerow(dit)

for each in college:
    name = each.text
    c_name = name.strip()
    link = (base_url + each['href'].replace(" ", ""))
    open()








