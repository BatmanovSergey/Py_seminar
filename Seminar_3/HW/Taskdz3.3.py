# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# Пример
# in -> 88
# out -> 1011000
# in -> 11
# out -> 1011

import os
def clear(): return os.system('cls')
clear()

# # Решение 1

def dec_number(number):
    binary = 0
    decade = 1
    while number>0:
        binary = binary + number%2*decade
        number//=2
        decade*=10
    return binary

num = int(input('Введите натуральное число: '))
bin_number = dec_number(num)
print(f'Число {num} в двоичной системе выглядит как {bin_number}')

# # Решение 2

# def conv_bin(num: int):
#     list_nums = []
#     while num > 0:
#         list_nums.insert(0, num % 2) # добавляет новый элемент списка на индекс[0] на каждой итерации
#         num //= 2
#     print(*list_nums, sep="")

# conv_bin(int(input('Введите натуральное число: ')))
