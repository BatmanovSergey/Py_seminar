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
        new_list.append(round((random.uniform(1, amount)), 2))
    return new_list


def diff_fract_part(new_list):
    fractional_list = []
    min_frac = 1
    max_frac = 0
    diff = 0
    for i in range(len(new_list)):
        fractional_list.append(round((new_list[i] % 1), 2))

    for i in range(len(fractional_list)):
        if fractional_list[i] > max_frac:
            max_frac = fractional_list[i]

    for i in range(len(fractional_list)):
        if fractional_list[i] < min_frac:
            min_frac = fractional_list[i]

    diff = round((max_frac - min_frac), 2)
    return max_frac, min_frac, diff


num = int(input('Введите натуральное число: '))
n_list = create_list(num)
print(n_list)
d = diff_fract_part(n_list)
print(f'MAX: {d[0]}, MIN: {d[1]}. Разница: {d[2]}')
