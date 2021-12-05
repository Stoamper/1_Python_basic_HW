'''
1.	Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError.
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
'''
import re

def email_parse(user_email):
    username = re.match(r'\w{3,}', user_email)  # выбираем username из почтового адреса
    domain = re.search(r'@(([A-Za-z_0-9.-]+).*)', user_email)   # выбираем домент из почтового адреса
    if domain is None or username is None or domain == [] or (re.findall(r'[\.]\w{2,4}', domain[0]) == []):
        raise ValueError('wrong email', user_email) # исключение при неправильно введенных данных
    else:
        usermail_dict = {
            'username': username.group(),
            'domain': domain[0][1:]     # вводим значение в словарь без символа @
        }
        print(usermail_dict)

# user_email = input('Insery your email: ')
# user_email = 'sgek911@yandex.ru'  # адрес для проверки с простым доменом
user_email = 'sgek911@yandex.asus.ru'     # адрес для проверки с составным доменом
# user_email = 'sgekyandex.ru' # для проверки выполнения исключения
# user_email = 'sgek@yandexru' # для проверки выполнения исключения

email_parse(user_email)









