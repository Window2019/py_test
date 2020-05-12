import  pytest

def test_case1(login):
    print('这是case需要登录')
    pass
def test_case2():
    print('这个case2不需要登录')
    pass
if __name__ =='__main__':
    pytest.main(-v)