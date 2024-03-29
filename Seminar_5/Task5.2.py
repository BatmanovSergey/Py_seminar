# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.

# Пример
# [9, 8, 1, 2, 5, 2, 11, 2, 9, 10]
# [[9, 11], [8, 11], [1, 2, 5, 11], [2, 5, 11], [5, 11], [2, 11], [2, 9, 10], [9, 10]]

# Пример
# [4, 8, 1, 1, 2, 4, 1, 8]
# [[4, 8], [1, 2, 4, 8], [1, 2, 4, 8], [2, 4, 8], [4, 8], [1, 8]]

from random import choices

def any_list(num):
    return choices(range(1, num+2), k=num)

def seq(some_list):
    temp_list = []
    for i in range(len(some_list)):
        maxx = some_list[i]
        out_list = [maxx]
        for j in range(i+1, len(some_list)):
            if some_list[j] > maxx:
                maxx = some_list[j]
                out_list.append(maxx)
        if len(out_list) > 1:
            temp_list.append(out_list)
    return temp_list

n_list = any_list(int(input("Введите натуральное число: ")))
print(n_list)
new_list = seq(n_list)
print(new_list)

