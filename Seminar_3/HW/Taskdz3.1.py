# 1. Задайте список, состоящий из произвольных чисел,
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# Пример
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample
import os
def clear(): return os.system('cls')
clear()

# # Решение 1

def create_list(amount):
    new_list = sample(range(1, (amount+1)*2), k=amount)
    return new_list

def sum_elements(new_list):
    summ = 0
    for i in range(0, len(new_list), 2):
        summ += new_list[i]
    return summ

num = int(input('Введите количество чисел: '))
num_list = create_list(num)
print(num_list)
summ_elem = sum_elements(num_list)
print(summ_elem)

# # Решение 2

# def list_rand_nums(count: int) -> list: # аннотация типов
#     if count < 0:
#         print("Negative value of the number of numbers!")
#         return []
    
#     list_nums = sample(range(1, count * 2), count)
#     return list_nums

# def sum_odd_pos(list_nums: list):
#     sum_nums = 0
#     for k in range(0, len(list_nums), 2):
#         sum_nums += list_nums[k]
#     return sum_nums

# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(sum_odd_pos(all_list))