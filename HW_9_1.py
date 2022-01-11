'''
1.	Создать класс TrafficLight (светофор):
●	определить у него один атрибут color (цвет) и метод running (запуск);
●	атрибут реализовать как приватный;
●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
●	проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
import time
import random

'''
1 метод (простое переключение с красного до зеленого)
'''

# class Trafficlight:
#     _color = 0      # атрибут приватный, используем _ перед названием
#
#     def running(self):
#         print('Сигналы светофора:')
#         self._color = 'Красный'
#         print(self._color)
#         time.sleep(7)
#         self._color = 'Желтый'
#         print(self._color)
#         time.sleep(2)
#         self._color = 'Зеленый'
#         print(self._color)
#         time.sleep(7)
#
# t = Trafficlight()
# t.running()


'''
2 метод (с учетом того, какой цвет увидел водитель при подъезде)
'''

# class Trafficlight:
#
#     def running(self, _color):
#         if _color == 'Красный':
#             print(_color)
#             time.sleep(7)
#             _color = 'Желтый'
#             print(_color)
#             time.sleep(2)
#             _color = 'Зеленый'
#             print(_color)
#             time.sleep(7)
#         elif _color == 'Желтый':
#             print(_color)
#             time.sleep(2)
#             _color = 'Зеленый'
#             print(_color)
#             time.sleep(7)
#         elif _color == 'Зеленый':
#             print(_color)
#             time.sleep(7)
#
# driver_color = input('Введите цвет светофора, к которому вы подъехали: ')
# t = Trafficlight()
# t.running(driver_color)


'''
3 метод (цикличное переключение цвета с учетом возможной ошибки)
'''
colors = ('Красный', 'Желтый', 'Зеленый', 'Фиолетовый')

class Trafficlight:

    def running(self, _color):
        if _color == 'Красный':
            print(_color)
            time.sleep(7)
            _color = 'Желтый'
            print(_color)
            time.sleep(2)
            _color = 'Зеленый'
            print(_color)
            time.sleep(7)
        elif _color == 'Желтый':
            print(_color)
            time.sleep(2)
            _color = 'Зеленый'
            print(_color)
            time.sleep(7)
        elif _color == 'Зеленый':
            print(_color)
            time.sleep(7)

while True:
    index = random.randrange(len(colors))
    driver_random_color = colors[index]
    print(f'Цвет светофора: {driver_random_color}')
    if colors[index] == 'Фиолетовый':
        print('Светофор сломался. Дальнейшяя работа невозможна')
        break
    else:
        t = Trafficlight()
        t.running(driver_random_color)
