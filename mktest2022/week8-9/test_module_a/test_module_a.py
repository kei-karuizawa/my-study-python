import pytest


@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    print('我是会话级别的作用域')
    yield
    print('会话执行完毕后执行我')


@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('a:我是模块级别的作用域')


# 会先打印“我是会话级别的作用域“
def test_a():
    print('我是一个测试用例')