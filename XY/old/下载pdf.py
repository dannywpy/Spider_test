import os

import pandas as pd
import requests
df = pd.read_excel('2021_减少注册资本1.xlsx')
column_link = '下载链接'
column_name = '公告标题'
downs= df[column_link]
names = df[column_name]
for down,name in zip(downs,names):
    down_link = f"https://www.szse.cn/api/disc/info/download?id={down}"
    response_down = requests.get(down_link)
    save_location = r'C:\Users\D_Wang\PycharmProjects\Spider_dome\XY\2021_减少注册资本'
    file_name = name+'.pdf'
    filepath = os.path.join(save_location,file_name)
    if response_down.status_code == 200:
        with open(filepath, "wb") as file:
            file.write(response_down.content)
        print(f"PDF {file_name}saved successfully.")
    else:
        print(f"Failed to download {file_name}PDF.")
