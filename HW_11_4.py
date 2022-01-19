'''
4.	Начать работу над проектом «Склад оргтехники».
Создать класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''

'''
Осталось добавить уникальные параметры для каждого типа оргтехники
'''

class Storage:
    def __init__(self, info):
        self.info = info
    def __str__(self):
        return f'Информация о складе: {self.info}'

class Equipment:
    def __init__(self, type_of, name, model):
        self.type_of = type_of
        self.name = name
        self.model = model
    def __str__(self):
        return f'Type_of: {self.type_of}, name: {self.name}, model: {self.model}'

class Printer(Equipment):
    def __init__(self, type_of, name, model, color):
        super().__init__(type_of, name, model)
        self.color = color
    def get_color(self):
        return f'available print colors: {self.color}'

class Scanner(Equipment):
    def __init__(self, type_of, name, model, format):
        super().__init__(type_of, name, model)
        self.format = format
    def _get_format(self):
        return f'available scan formats: {self.format}'

class Xerox(Equipment):
    def __init__(self, type_of, name, model, is_wifi):
        super().__init__(type_of, name, model)
        self.is_wifi = is_wifi
    def is_wifi_available(self):
        return f'wireless connection: {self.is_wifi}'


storage_info = Storage('Склад хранения офисной техники цеха 28')
p_1 = Printer('Принтер', 'HP', 'PCL400', 'only black')
s_1 = Scanner('Сканер', 'Konica', 'SC1000', 'A4 only')
x_1 = Xerox('Ксерокс', 'Lenovo', 'A4', 'wifi available')
# print(storage_info)
print(f'{p_1}; {p_1.get_color()}')
print(f'{s_1}; {s_1._get_format()}')
print(f'{x_1}; {x_1.is_wifi_available()}')
