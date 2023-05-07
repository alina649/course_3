import json
import os.path
import re
import datetime

def operation_list(path):
    """"Загрузка данных с файла .json"""
    if not os.path.exists(path):
       return None

    with open(path, "r", encoding="utf-8") as file:
        """Удаляет {}"""
        list = json.load(file)
        list2 = [x for x in list if x != {}]
    return list2

def operation_sort_acoompl(path):
    """Проверка: Выполнена функция или нет."""
    operation_data = operation_list(path)

    if operation_data is None:
        return None

    operations = []
    for operation_dict in operation_data:
        if operation_dict["state"] == "EXECUTED":
           operations.append(operation_dict)

    return operations

def sort_date(path):
       """Сортировка операций по дате.Выбор 5 последних выполненных операция"""
       operation_date = operation_sort_acoompl(path)
       date = sorted(operation_date, key = lambda x: x["date"])
       date.reverse()
       return date[0:5]

def sort_list(path):
    """Создаем новый лист, где будут добавлены все необходимые данные об операции"""
    operation_date = sort_date(path)
    list = []

    for operation in operation_date:
        list_values = {}

        list_values['date'] = operation['date']
        list_values['description'] = operation['description']

        try:
            list_values['from'] = operation['from']

        except KeyError:
            list_values['from'] = 'Hidden'



        list_values['to'] = operation['to']
        list_values['summa'] = operation['operationAmount']['amount']
        list_values['currency'] = operation['operationAmount']['currency']['name']

        list.append(list_values)
    return list

def changing_from(path):
    """Скрываем номер откуда была  совершена операция"""
    list = sort_list(path)
    list2 = []

    for i in list:
        where_from = i["from"]
        if where_from == 'Hidden':
            list2.append(i)
        else:
               line = re.findall(r'[a-zA-Zа-яА-Я]+', where_from)
               number = re.findall(r'\d+', where_from)

               c = number[0]

               number_from = c[0:4] + f" {c[4:6]}" + "**-****" + f" {c[-4:-1]}"
               i["from"] = f"{line[0]} {number_from}"
               list2.append(i)
    return list2

def changing_to(path):
    """Скрываем номер куда была совершена операция"""
    list = changing_from(path)
    list2 = []

    for i in list:
        where_from = i["to"]
        line = re.findall(r'[a-zA-Zа-яА-Я]+', where_from)
        number = re.findall(r'\d+', where_from)

        c = number[0]

        number_from = "**" + f"{c[2:6]}"
        i["to"] = f"{line[0]} {number_from}"
        list2.append(i)
    return list2

def date(path):
    """Приводим дату в надлежащий форма - %d.%m.%Y"""

    date_list = changing_to(path)
    list = []
    for data in date_list:
        date_time_str = data["date"]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f')
        date_time_obj.strftime("%d.%m.%Y")
        data["date"] = date_time_obj.strftime("%d.%m.%Y")
        list.append(data)
    return list
