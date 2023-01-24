# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.

# Пример 1
# in -> Number of words: 10
# out ->
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# Пример 2
# in -> Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# Пример 3
# in -> Number of words: -1
# out -> The data is incorrect

from random import sample

# # Моё решение 

def words_list (num, word="абв"):
    new_string = ""
    new_string_short = ""
    for i in range(num):
        w = sample(word, k=3) 
        m = ''.join (w)
        new_string += m +" "
        if m != "абв":
            new_string_short += m +" "
    return new_string, new_string_short

number = int(input('Введите число: '))
if number > 1:
    out_string = words_list(number)
    print("Первоначальная строка: ")
    print(out_string[0])
    print("Строка с удалёнными 'абв': ")
    print(out_string[1])
else:
    print("Введено некорректное число!!!")

# # Решение на семинаре

def list_rand_words(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        letters = sample(alp, 3)
        words_list.append("".join(letters))
    return " ".join(words_list)

# def list_rand_words(count: int, alp: str = 'абв'):
#     return " ".join("".join(sample(alp, 3)) for _ in range(count))

def simple_sentence(words: str) -> str:
    # return " ".join(words.replace("абв", "").split())
    return " ".join(i for i in words.split() if i != "абв")

all_list = list_rand_words(int(input("Number of words: ")))
print(all_list)
print(simple_sentence(all_list))
