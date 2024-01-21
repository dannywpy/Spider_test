import csv
import json
import time

import pandas as pd
import requests
# f = open('2022.csv', mode='a', encoding='utf-8', newline='')
# csv_writer = csv.DictWriter(f, fieldnames=['city','name', 'core','av_core','rank'])
# csv_writer.writeheader()
# df = pd.read_excel('city.xlsx')
# column_name = 'city'
# city_names = df[column_name]
# for city_name in city_names:
url = 'https://deindex.h3c.com/API/CityInfoAllLevel.ashx?callback=jQuery112301300763324871943_1711176868610'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

data = {
    "IndexYear": "2022",
    "City": '黄石'

}

resopnse = requests.post(url=url,data=data,headers=headers).text
data = resopnse.replace('jQuery112301300763324871943_1711176868610(','')
deal_data = data.replace('}]})','}]}')
json_data = json.loads(deal_data)
print(json_data)
# for item in range(0, 5):
#     dit1 = {
#         '项目': json_data[item]['distribution'][0]['name'],
#         '得分': json_data[item]['distribution'][0]['score'],
#         '平均分': json_data[item]['distribution'][0]['average'],
#         '排名': json_data[item]['distribution'][0]['ranking']
#
#     }
#     dit2 = {
#         '项目': json_data[item]['distribution'][1]['name'],
#         '得分': json_data[item]['distribution'][1]['score'],
#         '平均分': json_data[item]['distribution'][1]['average'],
#         '排名': json_data[item]['distribution'][1]['ranking']
#     }
#
#     dit3 = {
#         '项目': json_data[item]['distribution'][2]['name'],
#         '得分': json_data[item]['distribution'][2]['score'],
#         '平均分': json_data[item]['distribution'][2]['average'],
#         '排名': json_data[item]['distribution'][2]['ranking']
#
#     }
#
#     dit4 = {
#         '项目': json_data[item]['distribution'][3]['name'],
#         '得分': json_data[item]['distribution'][3]['score'],
#         '平均分': json_data[item]['distribution'][3]['average'],
#         '排名': json_data[item]['distribution'][3]['ranking']
#     }














