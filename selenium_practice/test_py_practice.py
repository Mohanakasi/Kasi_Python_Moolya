import pytest



def test_1():
    print("temp1")

@pytest.mark.xfail
@pytest.Mark.sanity
def test_2():
    name = 'kasi'
    assert 'sunil' == name
    print('test2')