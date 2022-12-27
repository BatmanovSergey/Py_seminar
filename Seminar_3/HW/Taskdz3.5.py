# ** 5. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# пример:
# in -> 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in ->5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

# # Решение 1

# import os
# def clear(): return os.system('cls')
# clear()

# def fibonachi (n):
#     fib_list = []
#     for i in range(n+1):
#         if i < 2:
#             fib_list.append(i)
#         else:
#             fib_list.append(fib_list[i-1] + fib_list[i-2])
#     return fib_list

# def neg_fibonachi (n):
#     fib_list = [1, -1]
#     for i in range(2,n):
#         fib_list.append(fib_list[i-2] - fib_list[i-1])
#     fib_list.reverse()
#     return fib_list

# num = int(input('Введите число: '))
# fib = fibonachi(num)
# neg_fib = neg_fibonachi(num)
# res = [*neg_fib, *fib]
# print(f'Общая последовательность чисел Фибоначчи:\n{res}') # вывод списком
# print('Общая последовательность чисел Фибоначчи:\n',*res) # распаковка списка

# # Решение 2

def neg_fiba(num: int):
    a, b = 1, 1
    list_nums = [0]
    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a * (-1)**i)
        a, b = b, b + a
    return list_nums

print(*neg_fiba(int(input('Введите число: '))))


