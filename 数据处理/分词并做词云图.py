import pandas as pd
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('test2.xlsx', sheet_name='感受')

# 提取文本列
text_col = df['review']

# 将所有文本连接成一个字符串
text = ' '.join(text_col.astype(str))

# 使用jieba进行分词
word_list = jieba.cut(text, cut_all=False)

# 统计词频
word_freq = Counter(word_list)

# 生成词云
wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=600, max_words=200, max_font_size=100).generate_from_frequencies(word_freq)

# 显示词云图
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

