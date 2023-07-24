from lib.gratitudes import *

def test_gratitudes():
    grateful = Gratitudes()
    grateful.add('Makers')
    grateful.add('Food')
    grateful.add('Water')
    assert grateful.format() == 'Be grateful for: Makers, Food, Water'