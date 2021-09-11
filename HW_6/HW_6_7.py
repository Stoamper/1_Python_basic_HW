'''
7. Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
'''
import sys

if __name__=='__main__':
    n, num = sys.argv[1:]
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        for _ in range(int(n) - 1):
            line = f.readline().strip()
        f.seek(f.tell())
        f.write(num)
    print(f'значение № {n} заменено на {num}')
    exit()