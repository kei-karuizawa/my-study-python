import pymysql
import pandas as pd

db_info = {
    'host': 'localhost',
    'user': 'root',
    'password': '<PASSWORD>',
    'database': 'test',
    'charset': 'utf8'
}

connect = pymysql.connect(**db_info)

# 结合 Pandas 执行 SQL
sql = 'select * from 接口自动化测试用例文件'
result = pd.read_sql(sql, connect)
print(result)
print(type(result))  # <class 'pandas.core.frame.DataFrame'>