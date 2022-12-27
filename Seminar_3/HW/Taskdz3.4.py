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

from random import uniform
import os
def clear(): return os.system('cls')
clear()

# # Решение 1

def create_list(amount):
    new_list = []
    for i in range(amount):
        new_list.append(round((uniform(1, amount)), 2))
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

# # Решение 2

# def list_rand_nums(count: int):
#     list_nums = []
#     if count <= 0:
#         print("Negative value of the number of numbers!")
#         return [0.0]
#     for i in range(count):
#         list_nums.append(round (uniform(1, count), 2))
#     return list_nums

# def dif_max_min(list_nums: list):
#     num_max = num_min = list_nums[0] % 1 # назначаем макс и мин первый элемент
#     for k in range(1, len(list_nums)): # по этому range начинаем с 1
#         num = round(list_nums[k] % 1, 2)
#         if num > num_max:
#             num_max = num
#         elif num < num_min: # else нельзя, так как туда попадут и уловия "равно"
#             num_min = num
#     result = round(num_max - num_min, 2)
#     print(f"Min: {num_min:.2f}, Max: {num_max:.2f}, Difference: {result}")
#     return result 
# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(dif_max_min(all_list))   