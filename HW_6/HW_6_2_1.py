'''
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов;
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''
from collections import Counter     # импортируем функцию Counter для подсчета количества повторов элемента

all_remote_addr = []

with open('nginx_logs.txt', 'r') as f:  # открываем файл и записываем из него все ip в один лист all_remote_addr
    for line in f:
        remote_addr = line[:line.find(' ')]
        #print(remote_addr)
        all_remote_addr.append(remote_addr)

count_all_remote_addr = str(Counter(all_remote_addr).most_common(1))    # ищем наиболее часто повторяющийся ip адрес
ip = count_all_remote_addr[count_all_remote_addr.find('(') + 1:count_all_remote_addr.find(',')]
repeat_count = count_all_remote_addr[count_all_remote_addr.find(',') + 2:count_all_remote_addr.find(')')]
print(' IP адрес спамера:', ip, '\n', 'Количество повторений:', repeat_count)    # выводим часто повторяющийся ip адрес
