# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

import os
def clear(): return os.system('cls')
clear()

n = int(input("Введите число: "))
num_list = []
for i in range(-n, n+1):
    num_list.append(i)
print(num_list)
print("Введите позиции элементов.")
pos1 = int(input("Первая позиция: "))
pos2 = int(input("Вторая позиция: "))
composition = 1
if pos1 <= len(num_list) and pos2 <= len(num_list):
    composition = num_list[pos1-1] * num_list[pos2-1]
    print(num_list)
    print(composition)
else:
    print('В данном списке нет элементов с такими позициями')
    print(num_list)
