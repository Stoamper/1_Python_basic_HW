'''
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей
и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга.
'''
from itertools import zip_longest

with open('users_1.csv', 'r') as user_names:
    with open('hobbies_1.csv', 'r') as user_hobbies:    # открываем ранее созданные файлы с данными
        names = user_names.read().splitlines()
        hobbies = user_hobbies.read().splitlines()      # создаем списки разделенных строк из исходных файлов

# создаем генератор (чтобы не хранить лишнюю информацию в ОП)
users_hobbies_gen = ((names, hobbies) for names, hobbies in zip_longest(names, hobbies, fillvalue=None))
#
# создаем окончательный файл с данными об именах и хобби
with open('users_hobbies_HW_4_1.doc', 'w', encoding='UTF-8') as f:
    for user_hobby in users_hobbies_gen:
        f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')

# парсинг данных из конечного файла
# создаем пустые списки для заполнения данными при парсинге
surnames = []
names = []
hobbies = []

# открываем файл для парсинга
with open('users_hobbies_HW_4_1.doc', 'r', encoding='UTF-8') as f:
    for line in f:
        surname = line[:line.find(',')]     # сортировка фамилий
        name = line[line.find(',') + 1: line.find(':')].replace(',',' ')    # сортировка имени и отчества
        hobby = line[line.find(':') + 1:].replace('\n', '').replace('None', 'Hobby is not defined')  # сортировка хобби
        surnames.append(surname)    # добавление фамилии в список
        names.append(name)          # добавление имени и отчества в список
        hobbies.append(hobby)       # добавление хобби в список
    # вывод результатов парсинга файла
    print('Фамилии пользователей в файле:', surnames)
    print('Имена пользователей в файле:', names)
    print('Хобби пользователей:', hobbies)