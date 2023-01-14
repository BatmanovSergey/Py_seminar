# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.

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

