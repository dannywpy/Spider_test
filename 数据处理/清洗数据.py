import pandas as pd
import re

# 读取 Excel 文件
file_path = 'test.xlsx'  # 请将 'your_input_file.xlsx' 替换为实际的输入文件路径
df = pd.read_excel(file_path)

# 定义正则表达式模式
pattern = r'<imgclass=".*?alt="">'

# 清洗数据：去除每一行数据中的 '<img class="...' 到 'alt="">'
df_cleaned = df.apply(lambda x: x.str.replace(pattern, '', regex=True))

# 写入新的 Excel 文件
output_file_path = 'your_output_file.xlsx'  # 请将 'your_output_file.xlsx' 替换为实陃的输出文件路径
df_cleaned.to_excel(output_file_path, index=False)

print("数据清洗并成功写入新的 Excel 文件。")

