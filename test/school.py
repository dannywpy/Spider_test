import csv
import requests
from bs4 import BeautifulSoup

f = open('collage.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['学院名称', '学院链接','具体专业'])

csv_writer.writeheader()

url = 'https://www.gkd.edu.cn/'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

college = soup.select('#bs-example-navbar-collapse-1 > ul > li:nth-child(3) > ul > li> a')

base_url = 'https://www.gkd.edu.cn'
dit={}

#学院名称
for each in college:
    name = each.text
    c_name = name.strip()
    link = (base_url + each['href'].replace(" ", ""))
    key1 = '学院名称'
    value1= c_name
    key2 = '链接'
    value2= link
    if each['href'] == '/zdhgc/':
        BK_url ='https://www.gkd.edu.cn/zdhgc/channels/5619.html'
        response = requests.get(url=BK_url, headers=headers)

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        program_BK = soup.select('body > div:nth-child(5) > div > div.col-sm-9.list-box > ul > li > a')
        for each in program_BK:
            name = each.text
            dit = {
                '学院名称': c_name,
                '学院链接': link,
                '具体专业': name,
            }
            print(name)
            csv_writer.writerow(dit)
        Zk_url = 'https://www.gkd.edu.cn/zdhgc/channels/5620.html'
        response = requests.get(url=Zk_url, headers=headers)

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        program_BK = soup.select('body > div:nth-child(5) > div > div.col-sm-9.list-box > ul > li > a')
        for each in program_BK:
            name = each.text
            dit = {
            '学院名称': c_name,
            '学院链接': link,
            '具体专业': name,
            }
            print(name)
        print('111')
    elif each['href'] == '/yscm/':

        response = requests.get(url=link, headers=headers)

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        program_BK = soup.select('#Hui-navbar > ul > li:nth-child(5) > ul > li > a')

        for each in program_BK:
            name = each.text
            print(name)
            dit = {
                '学院名称': c_name,
                '学院链接': link,
                '具体专业': name,
            }
        print('222')
    elif each['href'] == '/xxgc/':
        response = requests.get(url=link, headers=headers)

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        program_BK = soup.select('#Hui-navbar > ul > li:nth-child(4) > ul > li> a')

        for each in program_BK:
            name = each.text
            print(name)
            dit = {
                '学院名称': c_name,
                '学院链接': link,
                '具体专业': name,
            }
        print('777')
    elif each['href'] == '/wywm/':
        response = requests.get(url=link, headers=headers)

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        program_BK = soup.select('#Hui-navbar > ul > li:nth-child(4) > ul > li > a')

        for each in program_BK:
            name = each.text
            print(name)
            dit = {
                '学院名称': c_name,
                '学院链接': link,
                '具体专业': name,
            }
        print('333')
    elif each['href'] == '/jzgcxy/':
        response = requests.get(url='https://www.gkd.edu.cn/jzgcxy/channels/1056.html', headers=headers)

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        program_BK = soup.select('body > div.container > div > div.col-sm-9.list-box > ul > li> a')

        for each in program_BK:
            name = each.text
            print(name)
            dit = {
                '学院名称': c_name,
                '学院链接': link,
                '具体专业': name,
            }
        print('444')
    elif each['href'] == '/jkxy/':
        response = requests.get(url='https://www.gkd.edu.cn/jkxy/channels/4574.html', headers=headers)

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        program_BK = soup.select('body > div.container-lg.bg-white > div > div.col-12.col-sm-7.col-lg-9.mt-3 > div > div.bg-light > ul > li > a')

        for each in program_BK:
            name = each.text
            print(name)
            dit = {
                '学院名称': c_name,
                '学院链接': link,
                '具体专业': name,
            }
        print('555')
    elif each['href'] == '/glxy/':
        response = requests.get(url='https://www.gkd.edu.cn/glxy/channels/9030.html', headers=headers)

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        program_BK = soup.select('body > div.container > div > div.col-sm-9.list-box > ul > li > a')

        for each in program_BK:
            name = each.text
            print(name)
            dit = {
                '学院名称': c_name,
                '学院链接': link,
                '具体专业': name,
            }
        print('666')

    csv_writer.writerow(dit)
    print(dit)



def lll(url, pram):
    response = requests.get(url=url, headers=headers)

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