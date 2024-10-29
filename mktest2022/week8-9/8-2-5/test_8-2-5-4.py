import pytest

@pytest.mark.run(order=2)
def test_01():
    print(1)


@pytest.mark.run(order=-1)
def test_03():
    print(3)


@pytest.mark.run(order=-2)
def test_04():
    print(4)


@pytest.mark.run(order=-4)
def test_09():
    print(9)


@pytest.mark.run(order=0)
def test_05():
    print(5)


def test10():
    print(10)


@pytest.mark.tryfirst
def test11():
    print(11)


class TestLogin():
    def test_06(self):
        print(6)


    @pytest.mark.run(order=1)
    def test_07(self):
        print(7)

    @pytest.mark.run(order=-3)
    def test_08(self):
        print(8)


    @pytest.mark.trylast
    def test12(self):
        print(12)

"""
5
7
1
6
9
8
4
3
"""

if __name__ == "__main__":
    pytest.main(['test_8-2-5-4.py'])