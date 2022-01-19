'''
7.	Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.
'''

class Complex_number:
    def __init__(self, number):
        self.number = number

    # Метод сложения комплесных чисел
    def __add__(self, other):
        return Complex_number(self.number + other.number)

    # Метод произведения комплексных чисел
    def __mul__(self, other):
        return Complex_number(self.number * other.number)

    def __str__(self):
        return f'{self.number}'


cn_1 = Complex_number(10 + 2j)
cn_2 = Complex_number(2 - 3j)
print(f'Сумма комплексных чисел {cn_1} и {cn_2} равна {cn_1 + cn_2}')
print(f'Произведение комплексных чисел {cn_1} и {cn_2} равно {cn_1 * cn_2}')