'''
1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Date:

    # Статический метод проверяет валидность даты (по-простому, без учета того, что в некоторые месяца 30 и менее дней)
    @staticmethod
    def date_valid(date):
        date_list = date.split('-')
        # return date_list
        if int(date_list[0]) < 0 or int(date_list[1]) < 0 or int(date_list[2]) < 0 or int(date_list[0]) > 31 or int(date_list[1]) > 12:
            raise Exception('Неверная дата. Необходимо изменить значения (формат ДД-ММ-ГГГГ)')
        else:
            return date_list

    # Метод класса, который извлекает число, месяц, год и преобразовывает их тип к типу «Число»
    # (выводит список со значениями дня, месяца и года в формате "Число" вместо "Строка")
    @classmethod
    def extract_date(cls, date):
        date_list = date.split('-')
        # print(type(date_list[0]))     # для проверки изначального формата даты
        for i in range(len(date_list)):
            date_list[i] = int(date_list[i])
        # print(type(date_list[0]))     # для проверки окончательного формата даты
        return date_list

user_date = input('Введите дату в формате ДД-ММ-ГГГГ: ')
d = Date()
print(d.date_valid(user_date))
print(d.extract_date(user_date))