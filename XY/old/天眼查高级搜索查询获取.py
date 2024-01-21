import json

import pandas as pd
import requests
# from fake_useragent import UserAgent
# ua = UserAgent()
# url = 'https://capi.tianyancha.com/cloud-tempest/advance'
# df = pd.read_excel('text.xlsx')
# re = df['re']
# re = '北京市'
# value = '00110102V2020'
# time_data = '2018-06-01-2019-06-01'
# heanders = {
#     'User-Agent': ua.random,
#     'Content-Type': 'application/json; charset=UTF-8',
#     'Host':'capi.tianyancha.com',
#     'Origin':'https://www.tianyancha.com',
#     'Referer':'https://www.tianyancha.com/',
#     'X-Tycid':'ccd4d2201c2211ef9bd7070a72555e10',
#
# }

# data = {
#   'establishTimeRangeSet': [1527782400000,1559318400000],
#   'customAreaCodeSet': [value],
#   'pageNum': 1,
#   'pageSize': 20,
#   'resultTagList': [f"成立时间：{time_data}",f"地区：{re}"],
#   'searchType': 2
# }

# data = '^^{^\\^establishTimeRangeSet^\\^:^[1683561600000,1714492800000^],^\\^customAreaCodeSet^\\^:^[^\\^00110101V2020^\\^^],^\\^pageNum^\\^:1,^\\^pageSize^\\^:20,^\\^resultTagList^\\^:^[^\\^^\u6210^\u7ACB^\u65F6^\u95F4^\uFF1A2023-05-09-2024-05-01^\\^,^\\^^\u5730^\u533A^\uFF1A^\u5317^\u4EAC^\u5E02^\\^^],^\\^searchType^\\^:2^}^'
#
# response = requests.post(url=url, data=data, headers=heanders)
# print(response)
# print(response.text)


import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://www.tianyancha.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.tianyancha.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-TYCID': 'ccd4d2201c2211ef9bd7070a72555e10',
    '^sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    '^sec-ch-ua-platform': '^\\^Windows^\\^^',
}

data = '^^{^\\^establishTimeRangeSet^\\^:^[1683561600000,1714492800000^],^\\^customAreaCodeSet^\\^:^[^\\^00110111V2020^\\^^],^\\^pageNum^\\^:1,^\\^pageSize^\\^:20,^\\^resultTagList^\\^:^[^\\^^\u6210^\u7ACB^\u65F6^\u95F4^\uFF1A2023-05-09-2024-05-01^\\^,^\\^^\u5730^\u533A^\uFF1A^\u5317^\u4EAC^\u5E02^\\^^],^\\^searchType^\\^:2^}^'

response = requests.post('https://capi.tianyancha.com/cloud-tempest/advance', headers=headers, data=data)

print(response)
print(response.text)
