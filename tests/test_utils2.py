from src.utils2 import format_date, encode_cards, encode_score

def test_format_date():
    assert format_date("2018-03-23T10:45:06.972075") == "23.03.2018"

def test_encode_cards():
    assert encode_cards("1234567812345678") == "1234 56** **** 5678"


def test_encode_score():
    assert encode_score("12345678912345678912") == "67****"


