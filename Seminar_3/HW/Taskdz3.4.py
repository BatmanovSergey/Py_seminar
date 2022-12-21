# * 4. Задайте список из произвольных вещественных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# in -> 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in -> 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36


from decimal import Decimal
import random

def create_list(amount):
    new_list = []
    for i in range(amount):
        new_list.append(round((random.uniform(1, amount)),2))
    return new_list

def fractional_part(new_list):
    fractional_list = []
    for i in range(len(new_list)):
       fractional_list.append(round((new_list[i]%1), 2))
    return fractional_list


    

num = int(input('Введите натуральное число: '))
n_list = create_list(num)
print (n_list)
f_list = fractional_part(n_list)
print (f_list)