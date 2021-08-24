'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
'''

def odd_nums_gen(user_number):      # функция с генератором для выбора нечетных чисел из диапазона
    for number in range(1, user_number + 1, 2):
        yield number

user_number = int(input('Введите максимальное значение диапазона: '))   # ввод пользователем верхней границы диапазона
odd_nums = odd_nums_gen(user_number)        # работа функции
print('В диапазоне есть следующие нечетные числа: ')
for i in range(user_number):        # вывод значений до тех пор, пока они есть с помощью next
    try:
        print(next(odd_nums))
    except StopIteration:
        print('Конец диапазона')
        break

