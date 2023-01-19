# 1. Представлен список чисел. 
# Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. 
# Use comprehension.
# Примеры:

# in -> 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in -> 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]
from random import sample

def list_rand_nums(count: int)-> list:
    if count < 0:
        print("Negative value of the number of numbers!")
        return []
    list_nums = sample(range(1, (count*2)), count)
    return list_nums

def values_previous_element(any_list: list)-> list:
    new_list =[any_list[i] for i in range(1, len(any_list)) if any_list[i] > any_list[i-1]]
    return new_list

num = int(input('Введите натуральное число: '))
our_list = list_rand_nums(num)
print(our_list)
result_list = values_previous_element(our_list)
print(result_list)






    
