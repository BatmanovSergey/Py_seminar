# * 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», 
# возвращает словарь, ключи — первые буквы фамилий, 
# значения — словари, реализованные по схеме предыдущего задания.
# Пример:
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out
# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 
#  'И': ['Иван Сергеев', 'Инна Серова']}, 
#  'А': {'Б': ['Борис Аркадьев'], 
#  'П': ['Павел Анисимов', 'Петр Алексеев']}, 
#  'И': {'И': ['Илья Иванов']}, 
#  'В': {'Ю': ['Юнона Ветрякова']}}

def dict_creater(string: str)-> dict: 
    my_dict = {}
    for name in names:
        if name.split()[1][0] in my_dict:
            my_dict[name.split()[1][0]].append(name)
        else:
            my_dict[name.split()[1][0]] = [name]
    
    print(my_dict)

    for key, value in my_dict.items():
        value = sorted(value)
        new_my_dict = {}
        for name in value:
            if name[0] in new_my_dict:
                new_my_dict[name[0]].append(name)
            else:
                new_my_dict[name[0]] = [name]
        my_dict[key] = new_my_dict
    return my_dict

# print("Введите имя и фамилию:")
# names = list(iter(input, ''))
# print(names)

# names = input("Введите имя и фамилию: ").split(', ')

# newlist = [word for line in names for word in line.split()]
# # for i in range(len(names)):
# #     newlist = []
# #     newlist.append(names[i].split())
# print(newlist)

names = "Иван Сергеев, Инна Серова, Петр Алексеев, "\
        "Илья Иванов, Анна Савельева, Юнона Ветрякова, "\
        "Борис Аркадьев, Антон Серов, Павел Анисимов, Юрий Антонов".split(', ')


result = dict_creater(names)
print(result)

