from numb3rs import validate


def test_validate_C():
    assert validate("255.255.0.89") == True
    

def test_validate_W():
    assert validate("0.256.0.0") == False