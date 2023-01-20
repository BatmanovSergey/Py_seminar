# 2. Для чисел в пределах от 20 до N найти числа, 
# кратные 20 или 21. 
# Use comprehension.
# in -> 100
# out -> [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in -> 424
# out -> [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 
# 120, 126, 140, 147, 160, 168, 180, 189, 200, 210,
# 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 
# 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]


def list_nums(count: int)-> list:
    if count < 20:
        print("Negative value of the number of numbers!")
        return []
    list_nums = [i for i in range(20, count+1)]
    return list_nums

def multi(any_list: list)-> list:
    new_list =[any_list[i] for i in range(len(any_list)) if not any_list[i] % 20 or not any_list[i] % 21]
    return new_list

num = int(input('Введите натуральное число: '))
our_list = list_nums(num)
result_list = multi(our_list)
print(result_list)
