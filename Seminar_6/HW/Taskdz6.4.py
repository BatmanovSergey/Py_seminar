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

# # Моё решение

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

# print("Введите имя и фамилию:") # вводить по строчно через терминал
# names = list(iter(input, ''))
# print(names)

# newlist = [word for line in names for word in line.split()]
# # for i in range(len(names)):
# #     newlist = []
# #     newlist.append(names[i].split())
# print(newlist)
# преобразование списка вида ["Иван Сергеев", "Инна Серова", "Петр Алексеев"]
# в список вида ["Иван", "Сергеев", "Инна", "Серова", "Петр", "Алексеев"]

# names = input("Введите имя и фамилию: ").split(', ')
names = "Иван Сергеев, Инна Серова, Петр Алексеев, "\
        "Илья Иванов, Анна Савельева, Юнона Ветрякова, "\
        "Борис Аркадьев, Антон Серов, Павел Анисимов, Юрий Антонов".split(', ')

result = dict_creater(names)
print(result)

# # Решения на семинаре вариант 1

from collections import OrderedDict

def thesaurus_adv(*args):
    s_n_sort = {}
    for s_n in args:
        s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
    return dict(OrderedDict(sorted(s_n_sort.items(), key=lambda x: x[0])))

fio_name = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                         "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
                         "Борис Аркадьев", "Антон Серов", "Павел Анисимов")
print(fio_name)

# # Решение от Александра

listNames=["Иван Сергеев", "Инна Серова", "Петр Алексеев",
"Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
"Борис Аркадьев", "Антон Серов", "Павел Анисимов"]
print(listNames)

dictSurname = {}
for Surname in listNames:
    firstLetterSurname=Surname.split()[1][0]
    # if firstLetterSurname in dictSurname:#.keys():
    #     dictSurname[firstLetterSurname].append(Surname)
    # else:
    #     dictSurname[firstLetterSurname]=[Surname]
    dictSurname.setdefault(firstLetterSurname,[])
    dictSurname[firstLetterSurname].append(Surname)

for firstLetterSurname,listNames in dictSurname.items():
    # print(listNames)
    setNames=sorted(set(listNames))
    # print(setNames)
    dictNames = {}
    for Name in setNames:
        # if Name[0] in dictNames:#.keys():
        #     dictNames[Name[0]].append(Name)
        # else:
        #     dictNames[Name[0]]=[Name]

        dictNames.setdefault(Name[0],[])
        dictNames[Name[0]].append(Name)
    # print(dictNames)
    dictSurname[firstLetterSurname] = dictNames
print(dictSurname)

