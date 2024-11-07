import pytest


if __name__ == '__main__':
    pytest.main([
        'week8-9/8-2-5/test_8-2-5-13.py',
        '-v', '-s', '-q',
        '--alluredir=./result'
    ])