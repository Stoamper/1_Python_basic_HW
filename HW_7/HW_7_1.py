'''
1.	Написать скрипт, создающий ста|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authappртер (заготовку) для проекта со следующей структурой папок:

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные
о вложенных папках и файлах (добавлять детали)?
'''

import os

# print(os.getcwd())
# записываем имена папок в переменные на случай возможного их изменения в будущем
dir_root = r'my_project'
dir_setting = r'settings'
dir_mainapp = r'mainapp'
dir_adminapp = r'adminapp'
dir_authapp = r'authapp'

# создаем коренную папку, если она отсутсвует
if not os.path.exists(dir_root):
    os.mkdir(dir_root)

# меняем директорию для возможности создания папок внутри корневой
os.chdir(dir_root)
# print(os.getcwd())

# создаем оставшиеся директории (добавляем проверку их наличия)
if not os.path.exists(dir_setting):
    os.mkdir(dir_setting)

if not os.path.exists(dir_mainapp):
    os.mkdir(dir_mainapp)

if not os.path.exists(dir_adminapp):
    os.mkdir(dir_adminapp)

if not os.path.exists(dir_authapp):
    os.mkdir(dir_authapp)