import csv
import json
import re
import threading
import time
import random
from fake_useragent import UserAgent
import pandas as pd
import requests

ua = UserAgent()
df = pd.read_excel('year_link.xlsx')
links = df['ln']

headers = {
    'User-Agent': ua.random
    ,'Cookie':'akacd_default=2147483647~rv=45~id=ac196788baf1103ed97aeac8c711f555; TLTSID=853553f6afbc16549e0400e0ed6ab7dd; TLTUID=853553f6afbc16549e0400e0ed6ab7dd; az_bt_cl=hPp0YAbH2l1Jzlm4TTBcIYdKkuXtQB2w06/Qokqu4J+m+8m3MsrmVrDziHlFS1Qx; az_bt_al=0377fda23fd6f17a63fed94298c1ab80; _pxhd=aa364eeaaa7c5abac8676d95d211ca8791d41d1b371d5326874e7e8f310f6a72:02ede793-270e-11ef-a818-3588b0dfcfe5; _pxdc=100; _abck=6F93F75B63D5282BF3569061B34B9E59~-1~YAAQlgcsF1ONNvuPAQAA8c6IAQz2ey2TgwFp6SXXQuCEx9+tGb5ldz7STGwQYw9rNWS+jiNEh7zq3yhw5VcYe4j7D2qp8O4QSaeh24yQoeleotaAKVA59KOVYXIyop4mRlnjDCoCDxWRu9sh9i7aQGOrLTsRMgsrDwvFlKhKaGSGOpGzfKxeDIUfObErTofb/it7ghOwvjmFjLAyQhKYYWAD/7H3eeesBjMdJuH3iyzhJUAMmucyp4h7Hl6BojJo7m6rg7YJVqgfvc6iwUqD+MehBnPlj4TF9T5ufukLiWe6Vk3CEk+A49EyK/ORoETW7Z4EFLtrFqoP6KsyUSHl0cuh5SgOZ+hSiZByErYjzgHqbACA5DEr1GbTxIBrwHU=~-1~-1~-1; sbsd=sC5cxG9h+NowtNrCl5DidicmwhgbIM0g3HS34v17SKtwJv8wEzX4b6BGzA0HZ/6Ac6ZxPzEzP1kGMG5wELaVvu70ljKZlcV/HIPIs8PRKSwYsFBQ06ANk2tiLK0QnCcvmDG1xuiCU55auikVUW5/p0iEVceE139wkJn/UOJjAuBiW2bbo3EVe4VblXQZWbQT8'
}

f = open('year.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['name','count','link'])


for link in links:
    csv_writer.writeheader()
    time.sleep(0.5)
    response = requests.get(
        url=link,
        headers=headers)

    json_data = json.loads(response.text)

    for data in json_data:
        print(data['name'])
        print(data['count'])
        dit = {
            'name':data['name'],
             'count':data['count'],
            'link':link
        }

        csv_writer.writerow(dit)

    print(f'su============================{link}')






















