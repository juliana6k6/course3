import datetime


def format_date(date_old):
    """
    Форматирует дату
    """
    date_new = datetime.datetime.fromisoformat(date_old)
    date_new_format = date_new.strftime("%d.%m.%Y")
    return date_new_format


def encode_cards(card_number):
    """
    Шифрует частично номер карты
    """
    encoded_cn = card_number[0:6] + "*" * 6 + card_number[-4:]
    encoded_cn_split = encoded_cn[0:4] + " " + encoded_cn[4:8] + " " + encoded_cn[8:12] + " " + encoded_cn[12:16]
    return encoded_cn_split
