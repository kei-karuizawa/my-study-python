import pytest

def add(a, b):
    return a + b

def test_dengyu():
    assert 3 == add(1,2)

def test_budengyu():
    assert 5 != add(1,3)

def test_dayu():
    assert 5 > add(1,3)

def test_dayudengyu():
    assert 5 >= add(1,3)

def test_xiao():
    assert 1 < add(1,2)

def test_xiaoyudengyu():
    assert 1 <= add(1,3)

def test_baohan():
    assert 1 in [1,2,3]

def test_bubaohan():
    assert 1 not in [1,2,3]

def test_iftrue():
    assert bool(1) is True

def test_iffalse():
    assert 0 is False

if __name__ == "__main__":
    pytest.main(['test_8-2-5-2.py'])