import pytest
from lib.password_checker import *

def test_password_checker_correct_length():
    password_checker = PasswordChecker()
    situation = password_checker.check("123456789")
    assert situation == True

def test_password_checker_incorrect_length():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

