#  5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import os
clear = lambda: os.system('cls')
clear()

n = int(input("Введите число: "))
num_list = []
for i in range(n):
    num_list.append(i)
print(num_list)

