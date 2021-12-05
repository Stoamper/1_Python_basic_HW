'''
Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
'''
import re

def log_parse(src):     # функция с регулярным выражением для парсинга данных
    re_list = [r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
               r'\[(.*?)\]',
               r'\"([A-Z]{3})',
               r'\s(\/[\w\/]+)',
               r'\s(\d{3})\s',
               r'\s\d{3}\s(\d+)']
    return list(re.findall(x, src)[0] for x in re_list)

if __name__ == '__main__':
    with open('nginx_logs.txt') as f:
        count, line = 1100, f.readline()
        while line and count:
            print(log_parse(line))
            count -= 1
            line = f.readline()