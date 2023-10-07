import json


def get_all_operations(filename):
    """
    функция открывает json-файл
    """
    with open(filename, "r", encoding="utf-8") as file:
        all_operations = json.load(file)
        return all_operations


