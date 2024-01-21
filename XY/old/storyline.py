import requests

url = 'https://www.imdb.com/title/tt2379713/?ref_=fn_tt_tt_1'

headers = {
    'Cookie':'session-id=144-0160090-6525209; session-id-time=2082787201l; csm-hit=tb:s-21EN12MFMVFFF9F4T41Y|1716553714211&t:1716553714706&adb:adblk_no; ad-oo=0'
    ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

}


response = requests.get(url=url,headers=headers).text
print(response)







