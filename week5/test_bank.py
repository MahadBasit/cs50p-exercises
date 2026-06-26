from bank import value

def test_value():
    assert value('HELLO') == 0
    assert value('h23r3r') == 20
    assert value('12345') == 100
    assert value("hello there") == 0
    assert value('Hello') == 0