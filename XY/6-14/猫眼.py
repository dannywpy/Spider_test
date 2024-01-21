import csv
import json
import re
import time

import requests
from bs4 import BeautifulSoup
f = open('movies.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['name','累计票房', '首日票房', '首周票房 ', '预测', '分账', '片方', '影院', '其他', '物料', '微博', '微信', '百度','date','real','text'])
csv_writer.writeheader()
def get_base_links():
    cookies = {
        '^Cookie: Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1716380371',
        '_lxsdk_cuid': '18fa03e073bc8-08831fef0c7635-26001d51-240000-18fa03e073bc8',
        '_lxsdk': '89F5DEE0183511EFA7D89144D35F720D0AF124EB6E4F4B3882286D2DB401DAB9',
        'theme': 'moviepro',
        '_lxsdk_s': '19016fab025-1f5-002-be1^%^7C^%^7C26^',
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

    response = requests.get('https://piaofang.maoyan.com/rankings/year', headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text,'html.parser')
    ids = soup.select('#ranks-list > ul')
    m_names = soup.find_all(class_='first-line')
    for id,m_name in zip(ids,m_names):
        name = m_name.text
        link = id.get('data-com')
        # 使用正则表达式匹配并提取数字

        match = re.search(r'/(\d+)', link)

        # 如果找到匹配项，则提取数字
        number = match.group(1)

        print(name)
        base_url = 'https://piaofang.maoyan.com/movie/'
        last_link = base_url + number
        ts_text = get_ts(number)
        get_block(last_link,ts_text,name)



def get_ts(number):

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
    # time.sleep(2)
    base = 'https://piaofang.maoyan.com/movie/'
    last = '/moresections'
    link = base + number + last
    print(link)
    time.sleep(2)
    response = requests.get(url=link, headers=headers, cookies=cookies)
    json_data = json.loads(response.text)
    js_data = json_data['sectionHTMLs']['techSection']
    html_data = js_data['html']
    soup = BeautifulSoup(html_data, 'html.parser')
    text = soup.find(class_='tech-section')
    # dit1 = {
    #     'text':text.text
    # }
    # csv_writer.writerow(dit1)
    return text.text
def get_block(lin,ts_text,name):
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


    time.sleep(2)
    response = requests.get(url=lin, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    contens = soup.find_all(class_='info-detail-content')

    # 使用正则表达式匹配
    match = re.search(r'(?s)(?<=</div>).*?<script id="pageData" type="application/json">(.*?)</script>', response.text,
                      re.DOTALL)
    try:
        # 如果找到匹配项，则打印结果
        if match:
            js_data = match.group(1).strip()
            json_data = json.loads(js_data)
            date_n = json_data["boxshowChartData"]["chartData"]["box"]["date"]
            real_data = json_data["boxshowChartData"]["chartData"]["box"]["real"]

            dit = {
                'name':name,
                '累计票房': contens[0].text,
                '首日票房': contens[1].text
                , '首周票房 ': contens[2].text, '预测': contens[3].text, '分账': contens[4].text, '片方': contens[5].text,
                '影院': contens[6].text, '其他': contens[7].text, '物料': contens[8].text, '微博': contens[9].text,
                '微信': contens[10].text, '百度': contens[11].text,
                'date': date_n,
                'real': real_data,
                'text':ts_text

            }
            csv_writer.writerow(dit)
            print(f'successfully ================{lin}')
        else:
            print("No JSON data found")
    except IndexError:
        pass


if __name__ == '__main__':
    get_base_links()







