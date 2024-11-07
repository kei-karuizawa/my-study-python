import pytest


@pytest.fixture()
def first_fixture():
    print("我是第一个 fixture")
    return 1, 2, 3


@pytest.fixture()
def second_fixture():
    return "第二个 fixture 返回值"


# 先打印“我是第一个 fixture”
def test_case(first_fixture, second_fixture):
    print('这是我的测试用例')
    a, b, c = first_fixture
    print(a, b, c)  # 1 2 3
    assert (1, 2, 3) == first_fixture
    r = second_fixture
    print(r)  # 第二个 fixture 返回值


if __name__ == '__main__':
    pytest.main([__file__])
