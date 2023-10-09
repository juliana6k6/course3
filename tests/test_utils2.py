from src.utils2 import format_date

def test_format_date():
    assert format_date("2018-03-23T10:45:06.972075") == "23.03.2018"
