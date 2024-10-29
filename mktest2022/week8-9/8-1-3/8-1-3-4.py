import pymysql
from flask import Flask

# 这里是 MySQL 的基本连接信息
connect = pymysql.connect(
    host='<HOST>',
    port=3306,
    user='root',
    password='<PASSWORD>',
    database='<DATABASE>',
    charset='utf8'
)

# 用这个对象执行 SQL 语句
cursor = connect.cursor()

app = Flask(__name__)

@app.route('/')
def hello_world():
    sql = 'select * from imc_level'
    # 这个结果是数据的条数
    result = cursor.execute(sql)
    print(result)
    print(type(result))  # <class 'int'>
    # 得到查询后的真正结果
    r = cursor.fetchall()
    print(r)
    print(type(r))  # <class 'tuple'>，数据库执行 SQL 后返回的是元组类型
    return str(r)  # 元组类型需要转换成字符串返回


if __name__ == "__main__":
    app.run()
