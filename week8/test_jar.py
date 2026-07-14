from jar import Jar
import pytest


def test_capacity():
    jar = Jar(5)
    assert jar.capacity == 5


def test_str():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    

def test_size_deposit():
    jar = Jar(4)
    jar.deposit(1)
    assert jar.size == 1


def test_capacity_fail():
    with pytest.raises(ValueError):
        Jar('banana')
    

def test_deposit_fail():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(6)


def test_withdraw_fail():
    with pytest.raises(ValueError):
        jar = Jar(4)
        jar.deposit(2)
        jar.withdraw(5)