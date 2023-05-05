
from programm import date

def main(path):
   sort_oper = date(path)
   print("Добро пожаловать! Вот ваши 5 последние опрерации:")

   for i in sort_oper:
      print(f"\n{i['date']} {i['description']} \n{i['from']} - {i['to']} \n{i['summa']}{i['currency']}")


main('../operations.json')










