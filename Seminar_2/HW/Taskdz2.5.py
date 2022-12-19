#  5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import os
clear = lambda: os.system('cls')
clear()

# # Решение 1
from random import randrange

num_list = list(range(int(input("Введите число: "))))
print(num_list)

for i in range(len(num_list)):
    index = randrange(len(num_list))
    temp = num_list[i]
    num_list[i] = num_list[index]
    num_list[index] = temp
print(num_list)

# # Решение 2

# import random

# n = int(input("Введите число: ")) # вариант задания списка через append
# num_list = []
# for i in range(n):
#     num_list.append(i)
# print(num_list)

# for i in range(n):
#     index = random.randrange(n)
#     temp = num_list[i]
#     num_list[i] = num_list[index]
#     num_list[index] = temp
# print(num_list)

# n = int(input("Введите число: ")) # вариант задания списка через list(range(n))
# num_list = list(range(n))
# print(num_list)

