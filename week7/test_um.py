from um import count

def test_count1():
    assert count("hello,um,um,world") == 2
    
def test_count2():
    assert count('yummy') == 0

def test_count3():
    assert count('hello') == 0