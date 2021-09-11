'''
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
'''


import sys
from itertools import zip_longest

# указываем позиции файлов при их вводе через консоль (0 - имя файла, поэтому с 1)
users = sys.argv[1]
hobby = sys.argv[2]
united_list = sys.argv[3]
if __name__ == '__main__':
    with open(users, 'r') as user_names:
        with open(hobby, 'r') as user_hobbies:    # открываем ранее созданные файлы с данными
            names = user_names.read().splitlines()
            hobbies = user_hobbies.read().splitlines()      # создаем списки разделенных строк из исходных файлов

# создаем генератор (чтобы не хранить лишнюю информацию в ОП)
users_hobbies_gen = ((names, hobbies) for names, hobbies in zip_longest(names, hobbies, fillvalue=None))

# создаем окончательный файл с данными об именах и хобби
with open(united_list, 'w', encoding='UTF-8') as f:
    for user_hobby in users_hobbies_gen:
        f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')

# парсинг данных из конечного файла
# # создаем пустые списки для заполнения данными при парсинге
surnames = []
names = []
hobbies = []
#
# открываем файл для парсинга
with open('users_hobbies_HW_4_1.doc', 'r', encoding='UTF-8') as f:
    for line in f:
        surname = line[:line.find(',')]     # сортировка фамилий
        name = line[line.find(',') + 1: line.find(':')].replace(',',' ')    # сортировка имени и отчества
        hobby = line[line.find(':') + 1:].replace('\n', '').replace('None', 'Hobby is not defined')  # сортировка хобби
        surnames.append(surname)    # добавление фамилии в список
        names.append(name)          # добавление имени и отчества в список
        hobbies.append(hobby)       # добавление хобби в список
    # записываем результаты парсинга в отдельный файл
    with open('parse_result.doc', 'w', encoding='utf-8') as f1:
        f1.writelines(['Фамилии пользователей:', str(surnames), '\n'])
        f1.writelines(['Имена и отчества пользователей:', str(names), '\n'])
        f1.writelines(['Хобби пользователей:', str(hobbies)])

