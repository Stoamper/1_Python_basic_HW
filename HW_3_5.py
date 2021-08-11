# возврат шуток по исходным данным (random) без ключа для запрета повторов

from random import randrange

def get_jokes(n):
    joke_list = []          # создаем пустой список для будущих шуток
    for joke in range(n):   # перебираем в зависимости от указанного пользователем количества шуток
        joke = ' '.join([nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))], adjectives[randrange(len(adjectives))]])   # составляем рандомную шутку
        joke_list.append(joke)      # записываем шутку в список
    print(joke_list)        # выводим шутку

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

get_jokes(5)
