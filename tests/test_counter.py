from lib.counter import *

def test_counter():
    number = Counter()
    number.add(12)
    result = number.report()
    assert result == 'Counted to 12 so far.'