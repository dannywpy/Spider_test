# 导入所需的库
import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('movie_data.xlsx', engine='openpyxl')

# 查看数据框架的前几行
print(df.head())

# 获取数据的基本信息
print(df.info())

# 确保票房列的数据类型为整数或浮点数
df['票房'] = pd.to_numeric(df['票房'], errors='coerce')

# 重新检查数据框架的前几行，以确保数据类型已正确转换
print(df.head())

# 计算票房收入的平均值、中位数、标准差等
print("平均票房：", df['票房'].mean())
print("中位数票房：", df['票房'].median())
print("票房标准差：", df['票房'].std())

# 检查票房收入的分布情况，例如，计算票房收入的四分位数
print("票房收入四分位数：")
print(df['票房'].quantile([0.25, 0.5, 0.75]))

# 根据年份对票房收入进行分组，并计算每组的平均票房
print("按年份分组的平均票房：")
print(df.groupby('movie_year')['票房'].mean())


