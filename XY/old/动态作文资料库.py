import codecs
import json
import re

import openpyxl
import requests

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(['Author', 'Text'])
header = {
    "Cookie":"PHPSESSID=kajcr6hjt7nt6tjb1ek2s8a03b; PHPSESSID_NS_Sig=oenCV6mfwm96vVbo; VGOTCN_OnLineCount=U2",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
for i in range(1,7):
    response = requests.get(url = f'http://hsk.blcu.edu.cn/index/nav_zfcsample_data2?page={i}&psize=100&ae=%3Aeq%3A%3A%3A%3A%3Aeq%3A%3Aeq%3A%E6%AF%94%20%E6%9B%B4%3Aa%3A',headers=header)
    data = response.text
    cleaned_data = data.encode('utf-8').decode('utf-8-sig')
    # 解析 JSON 数据
    json_datas = json.loads(cleaned_data)
    # 提取中文数据
    all_data = json_datas['data']
    for data in all_data:
        author = data[0]
        text = data[1]
        sheet.append([author, text])
    print(i)

    workbook.save('比——更.xlsx')

























