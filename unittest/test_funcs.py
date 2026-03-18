# TODO: 사용자 모듈 import
from my_func import even_odd,avg,max_val,min_val

# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
def test_even_odd():
    assert True == even_odd(2)
    assert False == even_odd(3)

li = [2,4,6,8]
def test_average():
    assert 5 == avg(li)

def test_max_val():
    assert 8 == max_val(li)

def test_min_val():
    assert 2 == min_val(li)
