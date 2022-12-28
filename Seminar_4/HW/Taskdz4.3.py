# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности в том же порядке.
# Пример:
# in >> 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in >> -1
# out
# Negative value of the number of numbers!
# []

# in >> 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import choice
from collections import Counter

def num_list(count: int) -> list: 
    if count < 0:
        print('Отрицательное значение количества чисел!')
        return []
    else:
        list_num = []
        for i in range(count):
            list_num.append(choice(range(0, count+1)))
    return list_num

# # Решение 1 метод через count

def no_repeat_el_count(any_list: list) -> list:
    non_rep_el = []
    for i in range(len(any_list)):
        if any_list.count(any_list[i]) == 1:
            non_rep_el.append(any_list[i])

    return non_rep_el

# # Решение 2 метод через Counter

def no_repeat_el_counter(any_list: list) -> list:
    non_rep_el = []
    for i in range(len(any_list)):
        if Counter(any_list).get(any_list[i]) == 1:
            non_rep_el.append(any_list[i])

    return non_rep_el

num = int(input('Введите число: '))
work_list = num_list(num)
print(work_list)
n_r_e = no_repeat_el_count(work_list)
n_r_e_c = no_repeat_el_counter(work_list)
print(f'Решение методом 1:\n{n_r_e}')
print(f'Решение методом 2:\n{n_r_e_c}')




