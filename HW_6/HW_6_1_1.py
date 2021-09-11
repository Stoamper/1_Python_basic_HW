'''1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

parse_data = []     # создание пустого списка для последующего заполнения данными

with open('nginx_logs.txt', 'r') as f:      # открываем файл для работы с ним
    for line in f:
        remote_addr = line[:line.find(' ')]     # выделаем данные
        request_type = line[line.find('"') + 1:line.find('"') + 4]  # выделаем данные
        requested_resource = line[line.find('"') + 5:line.find('H') - 1]    # выделаем данные
        #print(remote_addr)
        #print(request_type)
        #print(requested_resource)
        united_data = (remote_addr, request_type, requested_resource)   # создаем кортеж из данных
        #print(united_data)
        #print(type(united_data))
        parse_data.append(united_data)      # добавляем данные в список
        #print(parse_data)
print(parse_data)   # выводим список кортежей




