# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Примеры:
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample
import os
def clear(): return os.system('cls')
clear()

def find_number(amount):
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

num = int(input('Введите количество чисел: '))
num_list = find_number(num)
print('Наш случайный список')
print(num_list)
m_list = multiplication_elements(num_list)
print('Новый список, где элементы это произведение пар чисел случайного списка')
print(m_list)
