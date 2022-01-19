'''
5.	Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
'''

account_equipment = {}
equipment_quantity = {}

class Storage:
    def __init__(self, _info):
        self._info = _info
    def __str__(self):
        return f'Информация о складе: {self._info}'

    # метод отражения движения техники на склад и со склада в подразделения
    @classmethod
    def motion_equipment(cls, eq_model, in_out):
        # print(equipment, in_out)
        account_equipment[eq_model] = in_out
        return f'Информация по приему/выдаче техники со склада: {account_equipment}'

    # метод отражения количества техники на складе
    @classmethod
    def equipment_quantity(cls, eq_model, quantity):
        equipment_quantity[eq_model] = quantity
        return f'Информация по количеству техники на складе: {equipment_quantity}'


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
    def get_format(self):
        return f'available scan formats: {self.format}'


class Xerox(Equipment):
    def __init__(self, type_of, name, model, is_wifi):
        super().__init__(type_of, name, model)
        self.is_wifi = is_wifi
    def is_wifi_available(self):
        return f'wireless connection: {self.is_wifi}'

# storage_info = Storage('Склад хранения офисной техники цеха 28')
# p_1 = Printer('Принтер', 'HP', 'PCL400', 'only black')
# s_1 = Scanner('Сканер', 'Konica', 'SC1000', 'A4 only')
# x_1 = Xerox('Ксерокс', 'Lenovo', 'A4', 'wifi available')
# print(storage_info)
# print(f'{p_1}; {p_1.get_color()}')
# print(f'{s_1}; {s_1.get_format()}')
# print(f'{x_1}; {x_1.is_wifi_available()}')

st = Storage('Склад хранения офисной техники цеха 28')
pr = st.motion_equipment('HP PCL400', 'out (выдан в технологическое бюро)')
print(pr)
sc = st.motion_equipment('Konica SC1000', 'in (принят из экономического отдела)')
print(sc)
pr_q = st.equipment_quantity('HP PCL400', 0)
pr_q = st.equipment_quantity('Konica SC1000', 1)
print(pr_q)
