import json
import csv
import pandas as pd
from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
from openpyxl import Workbook
# 读取Excel表格数据
df = pd.read_excel('creat.xlsx')

# 指定要提取相似度的列名，这个是上面creat表格中，我要提取哪一列的第一个的名字，你可以自己改

column_name = '商品名称'

# 定义目标字符串，，这个位置是你想计算什么关键词的相似度，你就改什么，我随便填了休闲鞋ok
target_string = '休闲鞋'

# 提取指定列的数据
column_data = df[column_name]

# 计算每个字符串与目标字符串的相似度
similarities = column_data.apply(lambda x: fuzz.ratio(target_string, str(x)))

# 创建新的DataFrame保存相似度数据
similarity_df = pd.DataFrame({column_name: column_data, 'similarity': similarities})

# 按相似度降序排序
sorted_df = similarity_df.sort_values(by='similarity', ascending=False)

# 提取相似度高的前6项数据
top6 = sorted_df.head(6)
print(top6)


# 制作饼状图
labels = [f'{df["列名"][i]}-{df["列名"][j]}' for i, j, s in top6]
sizes = [s for i, j, s in top6]
plt.pie(sizes, labels=labels)
plt.title('Top 6 Similarities')
plt.show()

# 制作柱状图
x = [f'{df["列名"][i]}-{df["列名"][j]}' for i, j, s in top6]
y = [s for i, j, s in top6]
plt.bar(x, y)
plt.title('Top 6 Similarities')
plt.xlabel('Pairs')
plt.ylabel('Similarity')
plt.show()

























