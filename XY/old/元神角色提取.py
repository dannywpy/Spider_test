import json
import time

import requests

import re
from bs4 import BeautifulSoup
i = 1
for num in range(727,732):
    urls = f'https://api-takumi-static.mihoyo.com/content_v2_user/app/16471662a82d418a/getContentList?iAppId=43&iChanId={num}&iPageSize=50&iPage=1&sLangKey=zh-cn&iOrder=6'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Cookie':'_MHYUUID=bcb6b319-d105-4131-b7db-5a05856c5e8c; Hm_lvt_c0310361bff66bad9e56464d5b62a3e0=1716437769; DEVICEFP_SEED_ID=632d69e118f05996; DEVICEFP_SEED_TIME=1716437768662; DEVICEFP=38d7fa7ed1986; Hm_lpvt_c0310361bff66bad9e56464d5b62a3e0=1716437994'
    }
    time.sleep(2)
    response = requests.get(urls, headers=headers).text

    json_data = json.loads(response)

    all = json_data['data']['list']

    for each in all:
        name = each['sTitle']
        details = each['sExt']
        json_deta = json.loads(details)
        chinese_name = json_deta['732_5']
        produce = json_deta['732_7']
        produce_text = re.sub(r'<[^>]+>', '', produce)
        other_name = json_deta['732_6']
        big_jpg_link = json_deta['732_1'][0]['url']
        vioce = json_deta['732_9'][0]['url']
        time.sleep(1)
        print('=' * 50)
        print(f'名称: {name}')
        print(f'简介: {produce_text}')
        print(f'别名: {other_name}')
        print(f'中文名: {chinese_name}')
        print(f'大图链接: {big_jpg_link}')
        print(f'语音链接: {vioce}')
        print('=' * 50)
        print()

        i += 1

    print(f'总数为{i}')