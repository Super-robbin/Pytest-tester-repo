import pytest
from lib.present import *




def test_present_2():
    pres = Present()
    # pres.wrap(10)
    # assert pres.unwrap() == 10

    with pytest.raises(Exception) as e:
        pres.wrap('1')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

# def test_present():
#     pres = Present()

#     with pytest.raises(Exception) as x:
#         pres.unwrap()
#     error_msg = str(x.value)
#     assert error_msg == 'No contents have been wrapped'

    