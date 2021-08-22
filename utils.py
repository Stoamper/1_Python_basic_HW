'''
2.	Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
'''

import requests
import datetime
import sys

currencies = {}     # пустая библиотека для будущего описания валют с их курсом

# создание функции для вывода курса по указанной пользователем валюте
def foreign_currencies(user_currency):
    user_currency = user_currency.upper()   # вне зависимости от регистра
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    data = response.text    # записываем всю строку с данными

    # парсинг строки с данными
    data = data.replace('<', '  ').replace('<', '  ').replace('>', '  ').replace(',', '.')  # заменяем символы
    data_list = data.split('  ')    # преобразуем строку в список

    # Заполнение словаря информацией (выделяем только валюту и ее курс)
    for i in range(len(data_list)):
         if data_list[i] == 'CharCode':
             currencies[data_list[i+1]] = float(data_list[i+13])

    # Ищем в словаре валюту, которую указал пользователь
    for key,val in currencies.items():
        if user_currency == key:
            print(f'Курс {key} к RUR на {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")} равен {val}')

if __name__ == '__main__':
    resilt = foreign_currencies(sys.argv[1])
    print(resilt[1])
#user_currency = input('Введите валюту: ')
#foreign_currencies(user_currency)