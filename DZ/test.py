import pandas as pd

# 创建要写入 Excel 的数据
data = {'列1': ['数值1', '数值2', '数值3'],
        '列2': ['数值4', '数值5', '数值6']}

# 创建 DataFrame 对象
df = pd.DataFrame(data)

# 将 DataFrame 写入 Excel 文件
filename = 'output.xlsx'
writer = pd.ExcelWriter(filename, engine='openpyxl')
df.to_excel(writer, index=False)
writer._save()
