import csv
import random
import threading
import time
import schedule

import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()
f = open('第一次.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['title','Kingdom', 'Phylum','Class','Subclass','Order','Family','Genus','Species','原始链接'])
csv_writer.writeheader()
f2 = open('aeepted.csv', mode='a', encoding='utf-8', newline='')
csv_writer2 = csv.DictWriter(f2, fieldnames=['title','name', 'link' ])
csv_writer2.writeheader()
f3 = open('Synonyms.csv', mode='a', encoding='utf-8', newline='')
csv_writer3= csv.DictWriter(f3, fieldnames=['title','name','link' ])
csv_writer3.writeheader()
f4 = open('native.csv', mode='a', encoding='utf-8', newline='')
csv_writer4 = csv.DictWriter(f4, fieldnames=['title','name', 'detail','link' ])
csv_writer4.writeheader()
# f5 = open('缺少的link.csv', mode='a', encoding='utf-8', newline='')
# csv_writer5 = csv.DictWriter(f5, fieldnames=['title','name', 'link' ])
# csv_writer5.writeheader()
f6 = open('缺失.csv', mode='a', encoding='utf-8', newline='')
csv_writer6 = csv.DictWriter(f6, fieldnames=['link'])
csv_writer6.writeheader()
#url = 'https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:44854-1'
sem=threading.Semaphore(30)
def get_Classfication(link):
    # df = pd.read_excel('test.xlsx')
    # column_name = 'ln'
    # links = df[column_name]
    # #代理服务器
    # proxyHost = "110.42.9.74"        #代理IP
    # proxyPort = "50001"      #代理端口
    # proxyUser = "JBWRXMlaKg"  #代理账户
    # proxyPass = "JBp4S9VfFW"  #代理密码
    #
    #
    # # Python3
    # proxyMeta = f"http://{proxyUser}:{proxyPass}@{proxyHost}:{proxyPort}"
    #
    # proxies = {
    #     "http"  : proxyMeta,
    #     "https"  : proxyMeta
    # }
    headers = {'User-Agent': ua.random}

    # for link in links:
    response = requests.get(url=link, headers=headers).text
    accepted(response)
    Synonyms(response,link)
    native(response,link)

    soup = BeautifulSoup(response, 'html.parser')
    try:
        title = soup.select('#main > div.taxon-header > div.taxon-header__summary > div > h1')
        names = soup.select('#higher-classification > div > div.taxon-section__content.paftol-content > ul > li > span.cl-rank.col-4.col-sm-4')
        texts = soup.select('#higher-classification > div > div.taxon-section__content.paftol-content > ul > li > span.cl-value.col-8.col-sm-8')
        original_text = "View Order Tree opens in a new tab"
        updated_text = original_text.replace("opens in a new tab", "")
        dit={'title':title[0].text,
            'Kingdom':texts[0].text,
            'Phylum':texts[1].text,
            'Class':texts[2].text,
            'Subclass':texts[3].text,
            'Order':texts[4].text.replace('View Order Tree opens in a new tab', "").strip(),
            'Family':texts[5].text.replace("View Family Tree opens in a new tab", "").strip(),
            'Genus':texts[6].text.replace("View in Tree of Life opens in a new tab", "").strip(),
            'Species':texts[7].text,
             '原始链接':link
                    }
        csv_writer.writerow(dit)
        print(f'successful {link}')
        time.sleep(random.uniform(0.1, 0.3))
        sem.release()
    except IndexError:
        dit6={
            'link':link
        }
        csv_writer6.writerow(dit6)
        print(f'已经写入表格 {link}')
        time.sleep(random.uniform(0.5, 1))
        sem.release()
def accepted(re):
    AI = 'Accepted Infraspecifics'
    if AI in re:
        soup = BeautifulSoup(re, 'html.parser')
        accept_names= soup.select('#children > div > div.col-12.col-sm-9 > div > ul > li')
        accept_links = soup.select('#children > div > div.col-12.col-sm-9 > div > ul > li > a')
        title = soup.select('#main > div.taxon-header > div.taxon-header__summary > div > h1')
        for accept_name,accept_link in zip(accept_names,accept_links):
            dit2 = {'title':title[0].text,
                'name': accept_name.text,
                   'link': accept_link.get('href')}

            csv_writer2.writerow(dit2)
def Synonyms(res,link):
    SY = 'Synonyms'
    if SY in res:
        soup = BeautifulSoup(res, 'html.parser')
        synonyms = soup.select('#synonyms > div > div.col-12.col-sm-9 > div > ul > li > a')
        title = soup.select('#main > div.taxon-header > div.taxon-header__summary > div > h1')
        synonyms_title = soup.select('#synonyms > div > div.col-12.col-sm-3.taxon-section__left > h2')

        # if not synonyms_title[0].text:
        #     # sy_name = soup.select('#main > div.taxon-header > div.taxon-header__summary > div > div.name-status.p-strong > a > em')
        #     # dit5 = {
        #     #     'title': title[0].text,
        #     #     'name': sy_name[0].text,
        #     #     'link': link
        #     # }
        #     # csv_writer5.writerow(dit5)
        #     # print(f'写入表格缺少link表格 {link}')
        #
        # else:
        for synonym in synonyms:
            dit3 = {
                'title':title[0].text,
                'name': synonym.text,
                'link': link
                   }
            csv_writer3.writerow(dit3)
        # else:
        #     sy_name = soup.select(
        #         '#main > div.taxon-header > div.taxon-header__summary > div > div.name-status.p-strong > a > em')
        #     dit3 = {
        #         'title': title[0].text,
        #         'name': sy_name.text,
        #         'link': link
        #     }


def native(resp,link):
    soup = BeautifulSoup(resp, 'html.parser')
    nats = soup.select('#distribution-listing > h3')
    nat_texts = soup.select('#distribution-listing > p')
    title = soup.select('#main > div.taxon-header > div.taxon-header__summary > div > h1')
    for nat,nat_text in zip(nats,nat_texts):
        dit4 = {
            'title': title[0].text,
            'name': nat.text,
            'detail':nat_text.text.strip(),
            'link':link
        }
        csv_writer4.writerow(dit4)
if __name__ == '__main__':
    # import threading
    #
    # import pandas as pd
    #
    # import AC
    # from AC import get_Classfication
    df = pd.read_excel('150.xlsx')
    column_name = 'ln'
    links = df[column_name]

    threads = []
    for link in links:
        sem.acquire()
        t = threading.Thread(target=get_Classfication, args=(link,))
        t.start()
    print('have done 11111111111111111111111111111111')