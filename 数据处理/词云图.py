# 首先，确保你已经安装了pandas和wordcloud库
# pip install pandas wordcloud

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取Excel文件
excel_file = "test.xlsx"
df = pd.read_excel(excel_file)

# 将Excel中的数据转换为词频字典
word_freq = dict(zip(df['词语'], df['频率']))

# 创建词云对象
wordcloud = WordCloud(font_path ="C:/Users/D_Wang/Downloads/shangshouqingzhuti.ttf",width=800, height=400, background_color='white')

# 生成词云
wordcloud.generate_from_frequencies(word_freq)

# 显示词云图像
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 关闭坐标轴
plt.show()
