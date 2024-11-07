import pytest


@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('b:我是模块级别的作用域')


# 会先打印“我是会话级别的作用域“
def test_b():
    print('我是一个测试用例')