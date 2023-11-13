import pytest
from lib.present import *

def test_present_unwrap_for_no_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_present_wrap_if_already_wrapped():
    present = Present()
    present.wrap("Nintendo")
    with pytest.raises(Exception) as e:
        present.wrap("Switch")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_present_wrap_and_unwrap():
    present = Present()
    present.wrap("Nintendo Switch")
    result = present.unwrap()
    assert result == "Nintendo Switch"
