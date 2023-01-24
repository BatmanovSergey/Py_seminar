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

# # Моё решение

from random import sample

def list_rand_nums(count: int)-> list:
    if count < 0:
        print("Negative value of the number of numbers!")
        return []
    list_nums = sample(range(1, (count*2)), count)
    return list_nums

def values_previous_element(any_list: list):
    new_list =[any_list[i] for i in range(1, len(any_list)) if any_list[i] > any_list[i-1]]
    return new_list

num = int(input('Введите натуральное число: '))
our_list = list_rand_nums(num)
print(our_list)
result_list = values_previous_element(our_list)
print(result_list)

# # Решение 1 на семинаре

# from random import sample

# def more_then(num):
#     my_list = sample(range(num * 3), num)
#     print(my_list)
#     return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]

# print(more_then(int(input())))

# # Решение 2 на семинаре

# from random import randint

# def more_then(num):
#     original_list = [randint(0, 1000) for _ in range(num)]
#     print(original_list)
#     return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]

# print(more_then(int(input())))





    
