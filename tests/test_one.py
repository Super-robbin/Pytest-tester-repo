from lib.one import *

def test_one():
    result = greet('Rob')
    assert result == f'Hello, Rob!'