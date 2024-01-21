import re
import requests
import chardet
from bs4 import BeautifulSoup

def get_tv_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Cookie': 'guardok=2mLr9Gr4lPi7YCootRn9hat6iZNfE5IZMVLua4Eg2NOdb291rAZjhggfZmnvOovBRVjeWpOJ3Ci2nWpFn4qwGQ==; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1715947670,1716601374,1716641062; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1716641062; Hm_lvt_8e745928b4c636da693d2c43470f5413=1715947670,1716601375,1716641062; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1716641062; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1715947670,1716601375,1716641062; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1716641062'
    }

    response = requests.get(url, headers=headers)
    encoding = chardet.detect(response.content)['encoding']
    content = response.content.decode(encoding)

    soup = BeautifulSoup(content, 'html.parser')

    # 电视剧名
    title = re.search(r'《(.+?)》', soup.title.string).group(1)
    print(f"电视剧名: {title}")

    # 时间
    time_info = re.search(r'^\d+', soup.title.string).group()
    print(f"时间: {time_info}")

    # 剧情简介
    intro = soup.find('div', id='Zoom').get_text().strip()
    print(f"剧情简介: {intro}")

    # 下载链接
    downloads = soup.select('#downlist > table')
    print("下载链接:")
    for download in downloads:
        print(download.text.strip())

base_url = 'https://www.dy2018.com/'
tv_list_url = base_url + 'html/tv/hytv/'

response = requests.get(tv_list_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

tv_links = [base_url + link['href'] for link in soup.select('a.ulink')]

for tv_link in tv_links:
    print(f"\n当前电视剧链接: {tv_link}")
    get_tv_info(tv_link)

