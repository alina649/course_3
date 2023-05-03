from program_class import Operation
import json
import os.path

def operation_list(path):
    """"Загрузка данных с файла .json"""
    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as file:
        list = json.load(file)
        list2 = [x for x in list if x != {}]
    return list2


def play_operation(path):
    """Создание списка экземляра Operations"""
    # список операций
    operation_data = operation_list(path)

    if operation_data is None:
        return None

    operations = []
    for operation_dict in operation_data:
        try:
            operetion = Operation(data = operation_dict["date"], leveldescription = operation_dict["description"],
                           where_from = operation_dict["from"], where_to = operation_dict["to"],
                          amount = operation_dict["operationAmount"]["amount"], currency = operation_dict["operationAmount"]["currency"]["name"])

        except KeyError:
            operetion = Operation(data = operation_dict["date"], leveldescription = operation_dict["description"],
                                  where_from = "Информация отсутствует", where_to=operation_dict["to"],
                                  amount = operation_dict["operationAmount"]["amount"],
                                  currency = operation_dict["operationAmount"]["currency"]["name"])
        operations.append(operetion)
    return operations


print(operation_list('../operations.json'))
print(play_operation('../operations.json'))