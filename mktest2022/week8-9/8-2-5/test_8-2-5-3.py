import pytest
import pymysql

def add(a, b):
    return a + b


# @pytest.mark.parametrize(['a', 'b'], [(1, 2), (3, 4), (5, 6)])
# def test_add1(a, b):
#     assert 3 == add(a, b)


db_info={
    'host': '10.231.1.218',
    'user': 'root',
    'password': 'bS)P/hcMP50-',
    'database': 'test',
    'charset': 'utf8'
}
connect = pymysql.connect(**db_info)
cursor = connect.cursor()
sql = 'select * from 接口自动化测试用例文件'
cursor.execute(sql)
result = cursor.fetchall()

@pytest.mark.parametrize([
    'id', 'title', 'api_type', 'api_address',
    'request_type', 'request_login', 'input_data',
    'data_formatter', 'expect_result'
], result)
def test_mysql_params1(
        id, title, api_type, api_address,
        request_type, request_login, input_data,
        data_formatter, expect_result
):
    print(title)


# xy = [(1, 2), (3, 4), (5, 6)]
# @pytest.mark.parametrize(['a', 'b'], xy)
# def test_add2(a, b):
#     assert 3 == add(a, b)


if __name__ == "__main__":
    pytest.main(['test_8-2-5-3.py'])