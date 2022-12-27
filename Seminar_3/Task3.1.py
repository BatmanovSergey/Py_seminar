# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample
import os
def clear(): return os.system('cls')
clear()

def find_number(amount, user_number):
    new_list = sample(range(1, (amount+1)*2), k=amount)
    print(new_list)
    if user_number in new_list:
        return 'yes'
    return 'no'

num = int(input('Введите количество чисел - '))
find_num = int(input('Введите искомое число - '))
some_number = find_number(num,find_num)
print(some_number)

