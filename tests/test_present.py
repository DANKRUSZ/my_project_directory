import pytest
from lib.present import Present

def test_present_wrapped():
    present = Present()
    present.wrap("Lego")
    result = present.unwrap()
    assert result == "Lego"

def test_raises_error_already_wrapped():
    present = Present()
    present.wrap("Xbox")
    with pytest.raises(Exception) as err:
        present.wrap("Wii")
    message = str(err.value)
    assert message == "A contents has already been wrapped."

def test_raises_error_nothing_wrapped():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    message = str(err.value)
    assert message == "No contents have been wrapped."


