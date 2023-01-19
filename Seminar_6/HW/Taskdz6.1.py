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

def list_rand_nums(count: int):
    if count < 0:
        print("Negative value of the number of numbers!")
        return []
    list_nums = sample(count*2, k=count)
    return list_nums

print(list_rand_nums(10))





    
