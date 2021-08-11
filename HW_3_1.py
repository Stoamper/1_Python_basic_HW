# перевод числительных от 0 до 10 с английского на русский

# создаем словать с ключами из английских слов и значениями из русских
numbers_translate = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

# функция сравнения введенного слова с имеющимися в словаре и вывода перевода
def num_translate(number):
    number = number.lower()         # приведение к нижнему регистру вне зависимости от того, как пользователь ввел слово
    for key, val in numbers_translate.items():
        if key == number:
            return val              # возвращаем перевод слова

user_number_en = input('Введите числительное на английском, которое хотите перевести: ')
result = num_translate(user_number_en)
print(f'С английского {user_number_en} переводится на русский как {result}')       # вывод результата работы функции


