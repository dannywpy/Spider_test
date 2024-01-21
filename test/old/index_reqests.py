import csv
import re
import time

import requests
import openpyxl
import json
url = 'https://deindex.h3c.com/API/CityInfoAllLevel.ashx?callback=jQuery112307914122435502673_1703588849760'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


pattern = re.compile(r"}\]\s*}\]\s*}\]")

f = open('2022.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
        '城市',
        '项目',
        '得分',
        '平均分',
        '排名',
]
               )

csv_writer.writeheader()

# def open_file():
# # 打开Excel文件
#     workbook = openpyxl.load_workbook('test_2017.xlsx')
#
#     # 选择一个工作表
#     worksheet = workbook['Sheet1']
#
#     # 读取第一列的数据
#     column_data = []
#     for column in worksheet.iter_cols(min_col=1, max_col=1, values_only=True):
#         column_data = list(column)
#     return column_data

# for city in open_file():
city = '随州'
data = {
    'IndexYear': 2022,
    'City': city
}
print(city)
time.sleep(3)
response = requests.post(url=url, headers=headers, data=data)
data = response.text
re_json = pattern.sub("}]}]", data)
new_s = re_json.replace(")", "]")
pos = new_s.find('"info":')

# 提取 "info": 后面的数据
data_json = new_s[pos + len('"info":'):].strip()

json_data = json.loads(data_json)
print(json_data)
city_name = {
    '城市':city
}
csv_writer.writerow(city_name)
for item in range(0,5):

    dit1 = {
        '项目': json_data[item]['distribution'][0]['name'],
        '得分': json_data[item]['distribution'][0]['score'],
        '平均分': json_data[item]['distribution'][0]['average'],
        '排名': json_data[item]['distribution'][0]['ranking']

    }
    dit2={
        '项目': json_data[item]['distribution'][1]['name'],
        '得分': json_data[item]['distribution'][1]['score'],
        '平均分': json_data[item]['distribution'][1]['average'],
        '排名': json_data[item]['distribution'][1]['ranking']
    }

    dit3 = {
        '项目': json_data[item]['distribution'][2]['name'],
        '得分': json_data[item]['distribution'][2]['score'],
        '平均分': json_data[item]['distribution'][2]['average'],
        '排名': json_data[item]['distribution'][2]['ranking']

    }

    # dit4 = {
    # '项目': json_data[item]['distribution'][3]['name'],
    #     '得分': json_data[item]['distribution'][3]['score'],
    #     '平均分': json_data[item]['distribution'][3]['average'],
    #     '排名': json_data[item]['distribution'][3]['ranking']
    # }
    # dit5 = {
    #     '项目': json_data[item]['distribution'][4]['name'],
    #     '得分': json_data[item]['distribution'][4]['score'],
    #     '平均分': json_data[item]['distribution'][4]['average'],
    #     '排名': json_data[item]['distribution'][4]['ranking']
    # }

    csv_writer.writerow(dit1)
    csv_writer.writerow(dit2)
    csv_writer.writerow(dit3)

    # csv_writer.writerow(dit4)
    # csv_writer.writerow(dit5)
# print(city,dit1, dit2, dit3, dit4)












