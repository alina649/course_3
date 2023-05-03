class Operation:
    """Класс с иформацией об операциях"""
    #дата перевода
    #описание перевода
    #откуда
    #куда
    #сумма перевода
    #ваоюта / currency
    def __init__(self, data ="", leveldescription = "", where_from = "", where_to = "", amount ="", currency = "" ):

        self.data = data
        self.leveldescription = leveldescription
        self.where_from = where_from
        self.where_to = where_to
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"{self.__class__.__name__}(data ={self.data}, leveldescription = {self.leveldescription}, " \
               f"where_from = {self.where_from}, where_to = {self.where_to},amount = {self.amount}," \
               f"currency = {self.currency})"



