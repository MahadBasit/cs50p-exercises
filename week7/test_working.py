from working import convert
import pytest

def test_convert1():
    assert convert("12:00 AM to 5:00 PM") == "00:00 to 17:00"

def test_convert2():
    assert convert("1 PM to 4 AM") == "13:00 to 4:00"

def test_convert3():
    with pytest.raises(ValueError):
        convert("12:60 to 1 pm")
