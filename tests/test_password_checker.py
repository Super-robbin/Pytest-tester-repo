import pytest
from lib.password_checker import *

def test_password_valid():
    checker = PasswordChecker()
    result = checker.check('september')
    assert result == True

def test_password_invalid():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check('makers')
    error_msg = str(e.value)
    assert error_msg == "Invalid password, must be 8+ characters."