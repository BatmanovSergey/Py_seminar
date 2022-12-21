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

