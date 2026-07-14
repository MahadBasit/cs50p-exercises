from seasons import validate_dob
import pytest
from datetime import date

def test_validate_valid():
    assert validate_dob("2000-11-25") == date(2000, 11, 25)


def test_validate_invalid():
    with pytest.raises(SystemExit):
        validate_dob('11 Jan, 2006')