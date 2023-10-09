import datetime


def format_date(date_old):
    """
    Форматирует дату
    """
    date_new = datetime.datetime.fromisoformat(date_old)
    date_new_format = date_new.strftime("%d.%m.%Y")
    return date_new_format



