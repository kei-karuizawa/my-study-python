import pytest

test_data = [
    {
        'case_name': '登录成功的测试',
        'username': 'admin',
        'password': '123',
    },
    {
        'case_name': '登录失败的测试',
        'username': 'admin',
        'password': '111111',
    },
    {
        'case_name': '用户名为空的登录',
        'username': '',
        'password': '222222',
    },
]

@pytest.fixture(params=test_data)
def param_data(request):
    return request.param


def test_login(param_data):
    username = param_data.get('username')
    print(username)
    password = param_data.get('password')
    print(password)
    case_name = param_data.get('case_name')
    print(case_name)


"""
PASSED
admin
123
登录成功的测试
PASSED
admin
111111
登录失败的测试
PASSED
''
222222
用户名为空的登录
"""

if __name__ == '__main__':
    pytest.main([__file__])
