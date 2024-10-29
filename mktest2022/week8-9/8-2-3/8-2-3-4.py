import pandas as pd

# 在终端显示 Excel 所有的列（不设置的话只会显示文件的一小部分）
pd.set_option('display.max_columns', None)
# 在终端显示 Excel 所有的行（不设置的话只会显示文件的一小部分）
pd.set_option('display.max_rows', None)

# 获取 Excel 中的数据
sheet1_data = pd.read_excel('../../files/接口自动化测试用例文件.xlsx')

# 获取 Excel 中所有“请求接口类别”是“登录”的数据
login_case_type = sheet1_data[sheet1_data["请求接口类别"] == "登录"]
# print(login_case_type)

# 数据解析
# 访问所有行中的“输入数据”
# for i in sheet1_data.index:
#     print(sheet1_data.iloc[i]['输入数据'])
login_case_data = login_case_type['输入数据'][0]  # 取出输入数据的 JSON 数据
print(login_case_data)  # {"userName":"imooc","password":"12345678"}

# json 解析
import json
login_case_data_dic = json.loads(login_case_data)
print(login_case_data_dic)  # {'userName': 'imooc', 'password': '12345678'}
print(type(login_case_data_dic))  # <class 'dict'>
username = login_case_data_dic['userName']
password = login_case_data_dic['password']
print(username)
print(password)
