# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Пример
# in -> "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out -> {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

# # Мои решения:

# # Метод 1

def dict_creater_1(string: str)-> dict: 
    name_list = string.split()
    my_dict = {}

    for name in name_list:
        if name[0] in my_dict:
            my_dict[name[0]].append(name)
            my_dict[name[0]].sort() # Сортировка списка после добавления нового элемента по ключу
        else:
            my_dict[name[0]] = [name]
    my_dict = sorted(my_dict.items()) # Сортировка по всем значениям -> получаем список кортежей
    my_dict = dict(sorted(my_dict)) # Преобразуем кортежи снова в словарь
    
    return my_dict

# # Метод 2

def dict_creater_2(string: str)-> dict: 
    name_list = sorted(string.split()) # Сортировка только один раз начального списка имён
    my_dict = {}
    for name in name_list:
        if name[0] in my_dict:
            my_dict[name[0]].append(name)
        else:
            my_dict[name[0]] = [name]

    return my_dict

our_names = input('Введите имена через пробел: ')

by_first_method = dict_creater_1(our_names)
print('Работа первого метода')
print(by_first_method)

by_second_method = dict_creater_2(our_names)
print('Работа второго метода')
print(by_second_method)

# # Решение на семинаре 1 вариант

# def thesaurus(*args): # означает неограниченное количество аргументов принимает функция
#     names_dict = {}
#     for i in sorted(args):
#         letter = i[0]
#         if letter not in names_dict:
#             names_dict[letter] = [i]
#         names_dict[letter] += [i] # конкатенация списков

#     return names_dict

# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

# # Решение на семинаре 2 вариант

# from itertools import groupby

# def thesaurus(*args):
#     if "" not in args:
#         return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
#     return "Error"

# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))

# # # Решение на семинаре 3 вариант

# def thesaurus(*args):
#     if "" not in args:
#         return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
#     return "Error"

# thesaurus('Кармен', 'Андрей', 'Василий', 'Алексей', 'Дмитрий', 'Виктор', 'Инна', 'Александра', 'Игнат', 'Спартак',
#           'Якоб', 'Люция', 'Дионис', 'Агора', 'Игорь')
