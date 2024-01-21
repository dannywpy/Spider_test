import csv
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
f = open('111.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['价格', '标题','评价数','详情','排名','link'])
csv_writer.writeheader()
df = pd.read_excel('5000.xlsx')
column_link = 'link'
column_price = 'price'
column_name = 'name'
column_commit = 'commit'
commits = df[column_commit]
links = df[column_link]
prices = df[column_price]
names = df[column_name]
i = 0
for link, price,name,commit in zip(links,prices,names,commits):
    header = {
        "Cookie":"shshshfpa=05572fd2-068b-7e66-3299-2a91e562cc0f-1700304994; shshshfpx=05572fd2-068b-7e66-3299-2a91e562cc0f-1700304994; __jdu=1700304995388454387034; pinId=-SR6s0XHaj78poOIm1QhqA; pin=jd_dzauqoDZpbke; unick=jd_dzauqoDZpbke; _tp=LUjlz5Xwfi6%2F8enPTmGlRA%3D%3D; _pst=jd_dzauqoDZpbke; unpl=JF8EAMhnNSttCE0GAExQHRoRGF5WW1gLQx4CZjcAVVRZTFMFEgpPQhF7XlVdWBRKFx9vZRRXXVNIVw4eAysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAh0TEUlcUVZVDEkeCmpjAFZUXkpWACsDKxUge21TXF8BQhYzblcEZB8MF1cEEwUSG11LW1VfXwlOHwtrZQxdWFxOVgwdAxkXIEptVw; areaId=2; TrackID=1zwHVasg00kuBgVq4Lmpm4-n8Vt9vfkxHf9kCuZVgyVe3noGy9SpHoqKdMl8k0M-bYxsZjOJo5M28fo05iRPCkmOK9hBtqrl8tS4tq_b4F6I; thor=F9A20C59B45033876AEF1563EC33F7C27402236A5B8A6C38B131572022111FDE7A9F91E1EEC156E0E541BF65EBB7C284479A66A313B9F6D702F899B7F8FB7B8AAD4A0E88B6B21AFF883B7875976C9EAE59772440DE3824A12F696262F3E278AB6D8B91E3C3D4A13FD54EE84ED06D91778939687E64CFD3A7CA2BA91E3ED24A043F4C484E9FF7EC47D36E5BD0FD2598A829FAB9876C606E409170194C0262FC88; flash=2_zTbGejRPRTTqoRYmiDW1TOqslbbTsc05e6e_HafOOjSwbYAlqAxjYhbxLPytng97Mi-2zWufMcEFAgnqNlr3hoW_aCIBZvqAkgVRXavOqoV*; __jdv=76161171%7Cdirect%7C-%7Cnone%7C-%7C1706531324953; 3AB9D23F7A4B3C9B=KWEEVTCTVXIG7XR5MU7PVKYXXO6XVI4WVKWDFEZXVZARKKUUWH2ZSTJXABTKSHI6JNE3MNQO2AVL3KMUQZQRTCHOJY; ipLoc-djd=2-2833-51956-0; mba_muid=1700304995388454387034; __jda=181111935.1700304995388454387034.1700304995.1706963611.1707052018.36; __jdc=181111935; token=3a9f916647fcbf2c6138794ebda77250,3,948362; __tk=BUe1Are1ArjxAua04r4zjr4zkUbr4za54uaE4UptAVn,3,948362; jsavif=1; jsavif=1; mba_sid=17070520189795725040605601310.2; __jd_ref_cls=LoginDisposition_Go; x-rp-evtoken=N-nAb5Oj6OS1u8hkvixIgP5orH2T6Tw6pqgfs8n6SUNvAfROsPuNPsMQu1aptQs1yllofT7gLJWbUvyxUbgHbiBDQ7cZcDEt1FnhCRZtxq5rAz1EE7FsQp5lH-gE43TZfiaj-Lbr9Q2mzs_1_6FYgRmmuBuXmODdzowVNisguLuROvm1fVVw4HIz2PRFE9N9IcZVyACEmhRvmH0rjKXyb0eryn0vFxcoHdmFmwLYQlY%3D; shshshsID=4a999aba0c57c439547f5ae7fc82dd7e_2_1707052373950; shshshfpb=BApXeq45Id-hAoYHC9MyQ0oBQQ-ZepH3VBkJxTrtX9xJ1Mm--qYO2; __jdb=181111935.4.1700304995388454387034|36.1707052018; 3AB9D23F7A4B3CSS=jdd03KWEEVTCTVXIG7XR5MU7PVKYXXO6XVI4WVKWDFEZXVZARKKUUWH2ZSTJXABTKSHI6JNE3MNQO2AVL3KMUQZQRTCHOJYAAAAMNORABQEAAAAAADI2EUJZFTXDMZIX; _gia_d=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    time.sleep(4)
    response = requests.get(url = link,headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        number = soup.select('#detail > div.tab-main.large > ul > li:nth-child(5)')
        details = soup.select('#detail > div.tab-con > div:nth-child(1) > div.p-parameter > ul.parameter2.p-parameter-list')
        data = details[0].text
        dit = {
            '价格': price,
            '标题': name,
            '评价数': commit,
            '详情': data,
            '排名': i,
            'link': link
        }
        csv_writer.writerow(dit)
        print(f'第{i}页成功' + link)
        i += 1
        if i % 25 == 0:
            time.sleep(20)
    else:
        print(f'第{i}页请求失败'+ link)
        break























