# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

# # Решение 1

# from decimal import Decimal

# n = Decimal(input("Введите число: "))
# while n != int(n):
#     n = n * 10
# summ = 0

# while n > 0:
#     summ = summ + n % 10
#     n = n // 10
# print(int(summ))

# # Решение 2

# n = input("Введите число: ")
# m = len(n)
# nf = float(n)
# nf = nf * (10 ** (m-2))
# summ = 0
# while nf > 0:
#     summ = summ + nf % 10
#     nf = nf // 10
# print(int(summ))

# # Решение 3

# num = input("Введите число: ") # изначально у нас строка в неё пользователь ввёл число
# sum_digits = 0
# power = len(num)-2 # степень
# num = float(num) # перевод строки в вещественное
# num *= int(10 ** power) #  перевод в целое число
# while num: # означает по num значимое, т.е. больше нуля, то делаем тело цикла
#     sum_digits += int(num % 10)
#     num //= 10
# # 0.0000000000000000000001
# print(int(sum_digits))

# # Решение 4

# print(sum(map(int, list(input("Введите дробное число: ").replace(".", "")))))
