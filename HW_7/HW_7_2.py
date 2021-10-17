'''
2.	*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе
«руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
'''

import os

# пропишем функцию создания директорий с проверкой того, что директория уже создана
def make_directory(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        print(f'Директория {dir} уже существует')
    finally:
        os.chdir(dir)

# пропишем функцию создания файлов
def make_files(files):
    files_divide = files.split(",")
    for j in range(len(files_divide)):
        file = open(files_divide[j], 'w')

# открываем исходный файл на чтение
with open('test_config.yaml', 'r') as f:
    lines = f.readlines()
    for line in lines:
        # разбиваем на список, используя в качестве разделителя :
        fol = line.strip().split(':')
        if fol[0] == 'base_dir':
            # создаем базовую директорию, в которой будут лежать все остальные файлы
            try:
                dir_name = fol[1]
                os.mkdir(dir_name)
            except FileExistsError:
                print(f'Директория {fol[1]} уже существует')
            finally:
                os.chdir(dir_name)
        # создаем поддиректории с файлами в зависимости от наполнения
        elif fol[0] == 'dir':
            make_directory(fol[1])
        elif fol[0] == 'files':
            make_files(fol[1])
            os.chdir('..')
        elif fol[0] == 'dir_mainapp':
            os.chdir('mainapp')
            make_directory(fol[1])
        elif fol[0] == 'dir_templates':
            make_directory(fol[1])
        elif fol[0] == 'files_templates_mainapp':
            make_files(fol[1])
            os.chdir('../../..')
        elif fol[0] == 'dir_authapp':
            os.chdir('authapp')
            make_directory(fol[1])
        elif fol[0] == 'dir_templates':
            make_directory(fol[1])
        elif fol[0] == 'files_templates_authapp':
            make_files(fol[1])
            os.chdir('../../..')

