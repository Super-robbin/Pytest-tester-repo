import pytest
from lib.present import *

"""
When we wrap an item
We get it back unwrapping
"""

def test_wrap_and_then_unwrap():
    pres = Present()
    pres.wrap(33)
    assert pres.unwrap() == 33

"""
If we unwrap before wrapping
We get an error message
"""

def test_unwrap_without_wrapping():
    pres = Present()
    with pytest.raises(Exception) as e:
        pres.unwrap()
    error_msg = str(e.value)
    assert error_msg == 'No contents have been wrapped'

"""
If we try to wrap an alread-wrapped present
We get an error message
"""

def test_wrapping_already_wrap():
    pres = Present()
    pres.wrap(44) 
    with pytest.raises(Exception) as e:
        pres.wrap(66)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."




    