import pandas as pd

# 假设Excel文件名为'movies.xlsx'，包含在当前目录下
df = pd.read_excel('movies.xlsx')

# 确保票房列为数值类型，并处理任何无法转换为数值的值
df['票房'] = pd.to_numeric(df['票房'], errors='coerce')

# 查看数据的前几行
print("数据预览：")
print(df.head())

# 查看数据的基本统计信息
print("\n基本统计信息：")
print(df.describe())

# 按年份统计票房总和
total_revenue_by_year = df.groupby('movie_year')['票房'].sum()
print("\n按年份统计票房总和：")
print(total_revenue_by_year)

# 票房最高的电影
highest_grossing_movie = df.loc[df['票房'].idxmax()]
print("\n票房最高的电影：")
print(highest_grossing_movie)

# 按年份统计电影数量
movie_count_by_year = df['movie_year'].value_counts()
print("\n每年电影数量：")
print(movie_count_by_year)

