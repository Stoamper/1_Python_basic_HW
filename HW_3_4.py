# обработка имен сотрудников и возврат словаря с упорядоченными именами (ключи - первая буква фамилии / имени)

def thesaurus_adv(*args):
    surnames_dict = {}          # создаем пустой словарь для будущих фамилий
    main_dict = {}              # создаем пустой основной словарь, в котором будет вся информация
    for name in args:           # цикл выделения первых букв фамилий для добавления в словарь
        surname = name.split(' ')[-1].title()       # отделение фамилий по пробелу, -1 - считаем с конца
        key_surname = surname[0]                    # выделяем первую букву фамилии
        surnames_dict[key_surname] = surnames_dict.get(key_surname, []) + [name]    # заводим ключ в словарь и добавляем имена
    for names_list in surnames_dict.values():
        names_dict = {}                             # создаем пустой словарь для имен
        for name in names_list:                     # цикл выделения первых букв имен
            surname = name.split(' ')[-1].title()   # отделяем фамилию
            key_surname = surname[0]                # выделяем первую букву фамилии
            key_name = name[0]                      # выделяем первую букву имени
            names_dict[key_name] = sorted(names_dict.get(key_name, []) + [name])    # заводим отсортированные ключи имен в словарь с именами
            main_dict[key_surname] = main_dict.get(key_surname, names_dict)         # заводим в основной словарь с учетом фамилий
    return dict(sorted(main_dict.items()))          # результат работы функции - отсортированный словарь

print(thesaurus_adv('Иван Иванов', 'Максим Пешков', 'Антон Чехов', 'Константин Симонов', 'Юрий Серов', 'Всеволод Павлов'))