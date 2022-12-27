#  5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import os
clear = lambda: os.system('cls')
clear()

# # Решение 1 - временная перемернная

# from random import randrange

# num_list = list(range(int(input("Введите число: "))))
# print(num_list)

# for i in range(len(num_list)):
#     index = randrange(len(num_list))
#     temp = num_list[i]
#     num_list[i] = num_list[index]
#     num_list[index] = temp
# print(num_list)

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

# # Решение 3 - кортеж

# from random import randrange

# num = int(input("Введите число: ")) # вариант задания списка через list(range(n))
# nums_list = list(range(num))
# print(nums_list)
# for i in range(num):
#     n_1, n_2 = randrange(num), randrange(num)
#     nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1] 
#     # кортеж чтобы уйти от третьей переменной
# print(nums_list)

# # Решение 4 - метод enumerate

from random import randrange

# n = int(input('Enter the length of the list: '))
some_list = list(range(33, 45)) # метод enumerate
# some_list = list(range(n))
print(some_list)
for i, val in enumerate(some_list):
    j = randrange(len(some_list))
    some_list[i], some_list[j] = some_list[j], some_list[i]
print(some_list)



