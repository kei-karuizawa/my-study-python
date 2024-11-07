import pytest


# @pytest.fixture(scope='session', autouse=True)
# def session_fixture():
#     print('我是会话级别的作用域')
#     yield
#     print('会话执行完毕后执行我')
#
#
# @pytest.fixture(scope='module', autouse=True)
# def module_fixture():
#     print('我是模块级别的作用域')


# @pytest.fixture(scope='class', autouse=False)
# def class_fixture():
#     print('我是类级别的作用域')


@pytest.fixture(scope='function', autouse=True)
def function_fixture():
    print('我是函数（方法）级别的作用域')


def test_01():
    print('我是一个测试用例')


class TestClass:
    def test_of_method1(self):
        print('我是类中的方法 1')


    def test_of_method2(self):
        print('我是类中的方法 2')


# 会先打印“我是会话级别的作用域“
# def test01():
#     print('我是一个测试用例')


if __name__ == '__main__':
    pytest.main([__file__])