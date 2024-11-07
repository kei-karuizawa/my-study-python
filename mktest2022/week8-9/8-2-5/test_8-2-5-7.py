import pytest

# 这是一个 fixture，相当于一个插件
@pytest.fixture()
def first_fixture():
    print('这是我人生中第一个 fixture')
    return 1


# 这也是一个 fixture，也是一个插件
# 但这个插件它又“组装了”其他插件（`first_fixture`）
@pytest.fixture()
def second_fixture(first_fixture):
    print('这是我人生中第二个 fixture')
    return first_fixture + 2


# 这个测试用例组装了 `first_fixture`，
# 所以会先调用 `first_fixture`
# 这里会先打印“这是我人生中第一个 fixture”
def test_case1(first_fixture):
    print('这是我的第一个测试用例')
    r = first_fixture
    print(r)  # 1


# 这个测试用例组装了 `second_fixture`，
# 而 `second_fixture` 组装了 `first_fixture`，
# 这里会先打印“这是我人生中第一个 fixture”，
# 再打印“这是我人生中第二个 fixture”
def test_case2(second_fixture):
    print('这是我的第二个测试用例')
    print(second_fixture)  # 3


if __name__ == '__main__':
    pytest.main([__file__])
