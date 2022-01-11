'''
4.	Реализуйте базовый класс Car:
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''

class Car:
    speed = 0
    color = None
    name = None
    is_police = bool

    def go(self):
        print('Авто поехало')

    def stop(self):
        print('Авто остановилось')

    def turn(self, direction = None):
        if direction == 'right':
            print('Авто повернуло направо')
        elif direction == 'left':
            print('Авто повернуло налево')
        else:
            print('Авто едет прямо')

    def show_speed(self, speed):
        print(f'Текущая скорость авто {speed}. Зафиксировано превышение скорости')

class TownCar(Car):
    def description(self, speed, color, name, is_police):
        print('Характеристики авто TownCar')
        print(f'Цвет: {color}')
        print(f'Марка: {name}')
        print(f'Относится ли автомобиль к полиции (0 - нет, 1 - да): {is_police}')
        print(f'Скорость: {speed}')
        if speed > 60:
            Car.show_speed(self, speed)
            print('Необходимо сбавить до 60')

class SportCar(Car):
    def description(self, speed, color, name, is_police):
        print('Характеристики авто SportCar')
        print(f'Цвет: {color}')
        print(f'Марка: {name}')
        print(f'Относится ли автомобиль к полиции (0 - нет, 1 - да): {is_police}')
        print(f'Скорость: {speed}')

class WorkCar(Car):
    def description(self, speed, color, name, is_police):
        print('Характеристики авто WorkCar')
        print(f'Цвет: {color}')
        print(f'Марка: {name}')
        print(f'Относится ли автомобиль к полиции (0 - нет, 1 - да): {is_police}')
        print(f'Скорость: {speed}')
        if speed > 40:
            Car.show_speed(self, speed)
            print('Необходимо сбавить до 40')

class PoliceCar(Car):
    def description(self, speed, color, name, is_police):
        print('Характеристики авто PoliceCar')
        print(f'Цвет: {color}')
        print(f'Марка: {name}')
        print(f'Относится ли автомобиль к полиции (0 - нет, 1 - да): {is_police}')
        print(f'Скорость: {speed}')

t = TownCar()
t.description(70, 'Black', 'Lincoln', 0)
t.go()
t.turn()

print('\n')

s = SportCar()
s.description(150, 'Yellow', 'Lotus', 0)
s.go()
s.turn('right')

print('\n')

w = WorkCar()
w.description(40, 'White', 'Tata', 0)
w.go()
w.turn('left')

print('\n')

p = PoliceCar()
p.description(50, 'Black and White', 'Ford', 1)
p.stop()







