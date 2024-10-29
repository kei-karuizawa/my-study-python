import pandas as pd

# 在终端显示 Excel 所有的列（不设置的话只会显示文件的一小部分）
pd.set_option('display.max_columns', None)
# 在终端显示 Excel 所有的行（不设置的话只会显示文件的一小部分）
pd.set_option('display.max_rows', None)

# 获取 Excel 中的数据
sheet1_data = pd.read_excel('../../files/接口自动化测试用例文件.xlsx')

# 获取所有的列名
# print(sheet1_data.columns)

# 把所有列的值依次取出来
for column_name in sheet1_data.columns:
    print(sheet1_data[column_name])

# 按照行来访问所有的数据
for i in sheet1_data.index:
    print(sheet1_data.iloc[i])

# 访问 Excel 中每一个单元格中的数据
for i in sheet1_data.index:
    for j in sheet1_data.iloc[[i]]:
        print(sheet1_data[j][i])