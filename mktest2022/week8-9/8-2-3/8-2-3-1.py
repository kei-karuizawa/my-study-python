import pandas as pd

# 在终端显示 Excel 所有的列（不设置的话只会显示文件的一小部分）
pd.set_option('display.max_columns', None)
# 在终端显示 Excel 所有的行（不设置的话只会显示文件的一小部分）
pd.set_option('display.max_rows', None)

# 获取 Excel 中的数据
sheet1_data = pd.read_excel('../../files/接口自动化测试用例文件.xlsx')
# sheet1_data = pd.read_excel('../../files/接口自动化测试用例文件.xlsx', sheet_name='sheet2')
print(sheet1_data)
print(type(sheet1_data))  # <class 'pandas.core.frame.DataFrame'>

# 单独访问一列的数据
print(sheet1_data['编号'])
print(type(sheet1_data['编号']))  # <class 'pandas.core.series.Series'>

# 单独访问一行的数据
print(sheet1_data.iloc[[0]])
print(type(sheet1_data.iloc[[0]]))  # <class 'pandas.core.frame.DataFrame'>

# 访问指定列的数据
print(sheet1_data[['编号', '标题']])
print(type(sheet1_data[['编号', '标题']]))  # <class 'pandas.core.frame.DataFrame'>

# 访问指定单元格的数据
print(sheet1_data['编号'][0])
print(type(sheet1_data['编号'][0]))  # <class 'str'>
