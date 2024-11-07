import os

import pytest


def add(a, b):
    return a + b

def test_dengyu():
    assert 3 == add(1,2)

def test_budengyu():
    assert 5 != add(1,3)

def test_dayu():
    assert 5 > add(1,3)


if __name__ == '__main__':
    pytest.main([__file__])
    #pytest.main([__file__, '--alluredir=./result'])
    #os.system("allure generate ./result -o ./report_allure --clean")