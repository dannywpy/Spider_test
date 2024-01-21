import pandas as pd
import os

# 假设所有Excel文件都放在同一个文件夹中
directory = 'C:/Users/D_Wang/PycharmProjects/Spider_dome/DZ/test'

import pandas as pd
import os
import re

# 设置包含Excel文件的目录

# 遍历文件夹中的每个Excel文件
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(directory, filename)

        # 读取Excel文件
        df = pd.read_excel(file_path)
        print(f"原始数据({filename}): {df.shape}")  # 显示原始数据行数和列数

        # 去除数据中的 "</div>"
        for col in df.columns:
            if df[col].dtype == object:  # 处理字符串类型的列
                df[col] = df[col].replace(to_replace=r'</div>', value='', regex=True)

        # 去除以 <img class= 开头且以 alt=""> 结尾的数据
        img_regex = r'<imgclass=.*?alt="">'
        for col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].replace(to_replace=img_regex, value='', regex=True)

        print(f"清洗后的数据({filename}): {df.shape}")  # 显示清洗后的数据行数和列数

        # 写入清洗后的数据到原文件
        df.to_excel(file_path, index=False)

print("所有文件处理完毕")
