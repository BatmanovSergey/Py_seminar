# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

# # Решение 1

n = float(input("Введите число: "))
while n != int(n):
    n = n * 10
summ = 0

while n > 0:
    summ = summ + n % 10
    n = n // 10
print(int(summ))

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
