'''
3.	Реализовать базовый класс Worker (работник):
●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь,
    содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
    и дохода с учётом премии (get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position,
    передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

class Worker:
    name = 'Thomas'
    surname = 'Anderson'
    position = 'Junior programmer'
    _income = {'wage': 1000, 'bonus': 500}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {Worker.name} {Worker.surname}')

    def get_total_income(self):
        sum_income = Worker._income['wage'] + Worker._income['bonus']
        print(f'Доход сотрудника с учетом премии: {sum_income} USD')

p = Position()
p.get_full_name()
p.get_total_income()