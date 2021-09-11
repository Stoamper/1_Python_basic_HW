'''
6. Реализовать простую систему хранения данных о суммах продаж булочной.
Должно быть два скрипта с интерфейсом командной строки:
для записи данных и для вывода на экран записанных данных.
При записи передавать из командной строки значение суммы продаж.
Для чтения данных реализовать в командной строке следующую логику:
    просто запуск скрипта — выводить все записи;
    запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
    запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
'''
# скрипт записи данных по суммам продаж булочной
import sys

sale = sys.argv[1:] # переменная для ввода значений продаж булочной

# создаем файл и записываем в него все введенные значения продаж булочной
if __name__ == '__main__':
    with open('sales_data.txt', 'w', encoding='utf-8') as f:
        f.writelines(sale)

