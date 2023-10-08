import json


def get_all_operations(filename):
    """
    функция открывает json-файл
    """
    with open(filename, "r", encoding="utf-8") as file:
        all_operations = json.load(file)
        return all_operations


def filter_operations(all_operations):
    """
    Возвращает выполненные операции из списка всех операций
    """
    filtered_operations = []
    for operation in all_operations:
        if operation.get("state") == "EXECUTED":
            filtered_operations.append(operation)
        continue
    return filtered_operations


