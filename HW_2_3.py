#3 Обработка списка "in place"

list_initial = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, list_initial in enumerate(list_initial):    #Используем функцию enumerate для перебора списка
    if list_initial.isdigit():                     #Если символы - цифры
        list_initial = '{0:02d}'.format(int(list_initial))#Дополняем до двух разрядов
    elif list_initial[1:].isdigit():               #Условие для поиска цифр после символа + или другого
        list_initial = '{0}{1:02d}'.format(list_initial[0], int(list_initial))#Дополняем число до двух разрядов
    print(list_initial, end=' ')                   #Для корректного отображения используем разделитель строк end
