import json

import pandas
import pandas as pd

with open('../DrissionPage/text.txt', 'r', encoding='utf-8') as f:
    provice = json.load(f)

for pro in range(len(provice)):
    p =  provice[pro]['label']
    if 'children' in provice[pro]:
        for city in range(len(provice[pro]['children'])):
            label = provice[pro]['children'][city]

            if 'children' in label:
                for lab in range(len(label['children'])):
                    value = label['children'][lab]['value']
                    la = label['children'][lab]['label']
                    print(p,value,la)
            # 对 lab 执行一些操作
            else:
        # 处理 'children' 键不存在的情况
                pass


    else:
# 处理 'children' 键不存在的情况
        pass











