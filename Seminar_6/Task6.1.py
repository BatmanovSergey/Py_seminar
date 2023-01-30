# Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции
# +,-,/,* приоритет операций стандартный.
# * Добавьте скобки,  приоритет операций меняется.

# exp = "4 * 3 - 1 / 9 - 7 * -1".split()
# exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()
#
actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

def sort_s(string):
    spl = string.split()
    fn_spl = []
    i = 0
    while i < len(spl):
        if spl[i] == "(":
            bracket = spl.index(")")
            fn_spl.append(spl[i + 1:bracket])
            i = bracket
        else:
            fn_spl.append(spl[i])
        i += 1
    return fn_spl

def culc(any_list):
    for i, v in enumerate(any_list):
        if isinstance(v, list):
            any_list[i] = culc(v)
    ch = [i for i, v in enumerate(any_list) if v in '*/']
    while ch:
        sm = ch[0]
        a, b, c = any_list[sm-1:sm+2]
        any_list.insert(sm-1, actions[b](a, c))
        del any_list[sm:sm+3]
        ch = [i for i, v in enumerate(any_list) if v in '*/']
    while len(any_list) > 1:
        a, b, c = any_list[:3]
        del any_list[:3]
        any_list.insert(0, actions[b](a, c))
    return any_list[0]

d = input('введите цифры:')
print(sort_s(d))
print(culc(sort_s(d)))
print(eval(d)) # # делает тоже самое, что весь код выше

# # List Comprehension и тернарный оператор

# num=[]
# for i in range(10):
#     if i % 2 == 0:
#         num.append(i)
# print(num)

# num1= [i for i in range(10) if i % 2 == 0 ]
# print(num1)

# num2= [i for i in range(10) if not i % 2 ]
# print(num2)

# num3= [i+10 if i % 2 == 0 else i**3 for i in range(10)]
# print(num3)
