import json
import time
import re
import requests
import chardet

from bs4 import BeautifulSoup
from lxml import html

for i in range(1,99):
    urls = f'https://www.dy2018.com/html/tv/hytv/index_{i}.html'
    base_link = 'https://www.dy2018.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Cookie':'guardok=2mLr9Gr4lPi7YCootRn9hat6iZNfE5IZMVLua4Eg2NOdb291rAZjhggfZmnvOovBRVjeWpOJ3Ci2nWpFn4qwGQ==; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1715947670,1716601374,1716641062; Hm_lvt_8e745928b4c636da693d2c43470f5413=1715947670,1716601375,1716641062; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1715947670,1716601375,1716641062; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1716642513; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1716642513; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1716642513'
    }
    headers1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Cookie':'guardok=2mLr9Gr4lPi7YCootRn9hat6iZNfE5IZMVLua4Eg2NOdb291rAZjhggfZmnvOovBRVjeWpOJ3Ci2nWpFn4qwGQ==; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1715947670,1716601374,1716641062; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1716641062; Hm_lvt_8e745928b4c636da693d2c43470f5413=1715947670,1716601375,1716641062; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1716641062; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1715947670,1716601375,1716641062; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1716641062'
        }
    response = requests.get(urls, headers=headers).text

    soup =  BeautifulSoup(response, 'html.parser')
    #提取电视的link
    links = soup.find_all('a',class_='ulink')

    for lin in links:
        ul = lin.get('href')
        urls = base_link + ul
        print(urls)
        time.sleep(3)
        response = requests.get(url=urls, headers=headers1)
        content_type = response.headers.get('Content-Type')
        encoding = chardet.detect(response.content)['encoding']

        decoded_content = response.content.decode(encoding)


        soup = BeautifulSoup(decoded_content, 'html.parser')


        titles = soup.title.string

        pattern = r"《(.*?)》"

        matches = re.findall(pattern, titles)
        #电视剧名
        for title in matches:
            print(title)
        time.sleep(1)
        pattern = r"^\d+"
        #时间
        match = re.findall(pattern, titles)
        print(match)
        time.sleep(1)

        # 查找所有的<br>标签
        br_tags = soup.find_all('div', id='Zoom')

        for br_tag in br_tags:
            print(br_tag.get_text().strip())
        time.sleep(1)
            # 下载链接
        downloads = soup.select('#downlist > table')

        for download_link in downloads:
            print(download_link.text.strip())





