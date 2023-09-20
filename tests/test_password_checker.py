import pytest
from lib.password_checker import PasswordChecker

def test_password_valid():
    passwordchecker = PasswordChecker()
    result = passwordchecker.check("Password")
    assert result == True

def test_password_not_valid():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as err:
        passwordchecker.check("Pass")
    message = str(err.value)
    assert message == "Invalid password, must be 8+ characters."