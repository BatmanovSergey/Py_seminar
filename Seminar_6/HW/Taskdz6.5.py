# ** 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, 
# взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Пример:

# in -> 10 True
# out
# ['дом ночью мягкий', 'огонь завтра зеленый', 
# 'лес вчера яркий', 'автомобиль сегодня веселый', 
# 'город позавчера утопичный']

# in -> 10 False
# out
# ['автомобиль ночью мягкий', 'огонь вчера веселый', 
# 'автомобиль позавчера веселый', 'город вчера утопичный', 
# 'лес сегодня зеленый', 'дом вчера яркий', 
# 'автомобиль вчера зеленый', 'огонь позавчера яркий', 
# 'огонь где-то утопичный', 'автомобиль где-то мягкий']

from random import choice

def joke(num: int, uniq: int)-> list:
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"] 
    final_joke = []
    if uniq:
        list_of_lists = [nouns, adverbs, adjectives]
        shortest_length = min(len(i) for i in [nouns, adverbs, adjectives])
        for i in range(shortest_length):
            new_joke = []
            noun = choice(nouns)
            new_joke.append(noun)
            nouns.remove(noun)
            
            adverb = choice(adverbs)
            new_joke.append(adverb)
            adverbs.remove(adverb)
            
            adjective = choice(adjectives)
            new_joke.append(adjective)
            adjectives.remove(adjective)

            final_joke.append(" ".join(new_joke))
    else:
        for i in range(num):
            new_joke = []
            noun = choice(nouns)
            new_joke.append(noun)

            adverb = choice(adverbs)
            new_joke.append(adverb)
            
            adjective = choice(adjectives)
            new_joke.append(adjective)

            final_joke.append(" ".join(new_joke))
    return final_joke 

jo = int(input('Введите количество шуток: '))
un = int(input('Введите уникальность: да -> 1 или нет -> 0: '))

print(joke(jo, un))

