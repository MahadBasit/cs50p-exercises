from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    
    with pytest.raises(ValueError):
        convert("abc/4")

    with pytest.raises(IndexError):
        convert("4")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"