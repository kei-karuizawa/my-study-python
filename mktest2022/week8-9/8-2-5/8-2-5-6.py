import pytest

def setup_module():
    print('前置的模块级别函数')


def teardown_module():
    print('后置的模块级别函数')


def setup_function():
    print('前置的函数级别的函数')


def teardown_function():
    print('后置的函数级别的函数')


def test1():
    print('测试方法 1')


def test2():
    print('测试方法 2')


class TestClass():
    def setup_class(self):
        print('类中的前置的类级别方法')


    def teardown_class(self):
        print('类中的后置的类级别方法')


    def setup_method(self):
        print('类中前置的方法级别的方法')


    def teardown_method(self):
        print('类中后置的方法级别的方法')


    def test_of_method1(self):
        print('类中测试方法 1')


    def test_of_method2(self):
        print('类中测试方法 2')


"""
前置的模块级别函数
前置的函数级别的函数
测试方法 1   PASSED
后置的函数级别的函数
前置的函数级别的函数
测试方法 2   PASSED
后置的函数级别的函数
类中的前置的类级别方法
类中前置的方法级别的方法
类中测试方法 1   PASSED
类中后置的方法级别的方法
类中前置的方法级别的方法
类中测试方法 2   PASSED
类中后置的方法级别的方法
类中的后置的类级别方法
后置的模块级别函数
"""

if __name__ == '__main__':
    pytest.main(['test_8-2-5-4.py'])