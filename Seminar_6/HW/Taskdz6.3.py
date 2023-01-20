# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Пример
# in -> "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out -> {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

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