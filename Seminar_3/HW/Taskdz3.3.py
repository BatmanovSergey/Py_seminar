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

def dec_number(number):
    binary = 0
    decade = 1
    while number>0:
        binary = binary + number%2*decade
        number//=2
        decade*=10
    return binary

num = int(input('Введите натурльное число: '))
bin_number = dec_number(num)
print(bin_number)


