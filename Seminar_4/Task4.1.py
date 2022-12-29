# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# пример:
# in >> 11 23 90 -8 12 7 45 -44
# out >> -44 90

# in >> 1, 6. 8: 91 -4
# out >> -4 9

# in >> 1 у 6 г 8
# out >> 'The data is incorrect'

# in >> 5ц 7ч 7
# out >> 'The data is incorrect'


def check ():
    enter_list = input("Введите числа через пробел: ").split()
    print(enter_list)
    right_list = []
    for i in range(len(enter_list)):
        enter_list[i] = enter_list[i].strip("!,;:?")
        if enter_list[i].isdigit:
            right_list.append(enter_list[i])
    print(right_list)
    # filter_list = list(filter(None, right_list)) # добавил строку, чтобы убрать пустые элементы списка
    # print(filter_list)
    return right_list # filter_list

def max_min_finder(any_list):
    if any_list: # если список содержит хоть что-то (не пустой) - true или 1
        return max(any_list, key=int), min(any_list, key=int)
    return []

print(*max_min_finder(check())) # * это распаковка списка