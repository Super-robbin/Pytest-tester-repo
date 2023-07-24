from lib.string_builder import *

def test_string_builder():
    string = StringBuilder()
    string.add('Hello') 
    # result = string.size()
    # assert result == 5
    assert string.size() == 5
    assert string.output() == 'Hello'

    # Note it works with both variable like result and assert method directly like: assert string.output() == 'Hello'