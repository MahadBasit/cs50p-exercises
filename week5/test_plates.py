from plates import is_valid

def test_st_lt():
    assert is_valid("AA80") == True
    
def test_length():
    assert is_valid("1") == False

def test_no_zero_first():
    assert is_valid("aat09") == False

def test_no_letters_after_digits():
    assert is_valid("EW8aai") == False