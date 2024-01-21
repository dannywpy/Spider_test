import requests





header = {
        "Cookie":'H5Channel=mnoreferseo%2CSEO; H5CookieId=0441b64e-1414-4667-b5f7-ed58e27f5ad5; firsttime=1715081343769; hotel_lang=zh-cn; indate=2024-05-07; outdate=2024-05-08; cityid=1923; searchEntranceId=h5_home; lasttime=1715083387070; JSESSIONID=0616F59D8297B53AB83570E0193F85B0',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

data = {
    'can_sale_ota_category_ids':[],
    'keyword': "",
    'objectId': "69242301",
    'pageIndex': '1',
    'pageSize': '10',
    'searchFeatures': []
}
url = 'https://www.elong.com/tapi/getCommentList'
response = requests.post(url, data=data,headers=header)

print(response.text)


















