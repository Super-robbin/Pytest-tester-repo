from lib.report_length import *

def test_report_length():
    result = report_length('Hello!')
    assert result == 'This string was 6 characters long.'