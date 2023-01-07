# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Примеры:
# in -> 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in -> 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample
import os
def clear(): return os.system('cls')
clear()

# # Решение 1

def create_list(amount):
    new_list = sample(range(1, (amount+1)*2), k=amount)
    return new_list

def multiplication_elements(new_list):
    mulpli_list = []
    if len(new_list) % 2 == 0:
        for i in range(len(new_list)//2):
            mulpli_list.append(new_list[i]*new_list[-1-i])
    else:
        for i in range(len(new_list)//2):
            mulpli_list.append(new_list[i]*new_list[-1-i])
        mulpli_list.append(new_list[len(new_list)//2])

    return mulpli_list

def multiplication_elements(new_list): # более кореектная запись метода
    mulpli_list = []
    for i in range(len(new_list)//2):
        mulpli_list.append(new_list[i]*new_list[-1-i])
    if len(new_list) % 2 != 0:
        mulpli_list.append(new_list[len(new_list)//2])
    return mulpli_list

num = int(input('Введите количество чисел: '))
num_list = create_list(num)
print('Наш случайный список')
print(num_list)
m_list = multiplication_elements(num_list)
print('Новый список, где элементы это произведение пар чисел случайного списка')
print(m_list)

# # Решение 2

# def list_rand_nums(count):
#     if count < 0:
#         print("Negative value of the number of numbers!")
#         return []

#     list_nums = sample(range(1, count * 2), count)
#     return list_nums

# def prod_pairs(list_nums: list):
#     res_list = []
#     len_list = len(list_nums)
#     for k in range(len_list // 2):
#         res_list.append(list_nums[k] * list_nums[len_list - k - 1])
#     if len_list % 2:
#         res_list.append(list_nums[len_list // 2])
#     return res_list

# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(prod_pairs(all_list))

# # Решение 3

# def mult_lst(lst):
#     l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
#     new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
#     if len(lst) % 2 != 0:
#         new_lst[-1] = lst[len(lst) // 2]
#     return new_lst

# def num_list(num_count):
#     new_list = sample(range(1, (num_count + 1) * 2), k=num_count)
#     return new_list

# num = int(input("Ваедите размер списка: "))
# n_list = num_list(num)
# print(n_list)
# m_list = mult_lst(n_list)
# print(m_list)
