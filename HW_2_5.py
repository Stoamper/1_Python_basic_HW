#5 Работа со списком цен товаров
import random

commodity_prices = [round(random.uniform(1, 100), 2) for i in range (15)]
print(id(commodity_prices))     #Проверка id
commodity_prices.sort()         #Выполнение сортировки
print(id(commodity_prices))     #Проверка id после сортировки на идентичность

rev_commodity_prices = commodity_prices.copy()[::-1]    #Реверсивный первоначальному список цен

#Функция перевода цен в корректный вид
def price(lists):
    new_list = []
    for i in lists:
        i = str(i)      #Переводим в тип "строка"
        lists = i.split('.')    #Разделяем число по точке
        strocke = f'{lists[0]} руб {lists[1]} коп'  #Каждый разделенный элемент записываем на свое место
        new_list.append(strocke)    #Добавляем запись в новый лист
    text = ', '.join(new_list)      #Соединяем все воедино в одну строку
    return text                     #text - результат работы функции (возвращаем)

print('Первоначальные цены 15-ти товаров:\n', price(commodity_prices), '\n')
print('Реверсивный список цен 15-ти товаров:\n', price(rev_commodity_prices), '\n')
print('5 самых дорогих товаров в списке:\n', price(rev_commodity_prices[:5]))


