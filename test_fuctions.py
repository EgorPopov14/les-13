from fustions import salary,a
def test_a_max():
    assert a('Max')=='Hello,Max'
    assert a('Egor')=='Hello,Egor'
    assert a('Grisha')=='Hello,Grisha'
    assert a('Kirill')=='Hello,Kirill'
    assert a('Ivan')=='Hello,Ivan'
def test_salary():
    assert(2,2)!=8
    assert(3,1)!=6