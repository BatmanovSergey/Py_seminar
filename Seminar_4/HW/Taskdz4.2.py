# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# Пример:
# in >> 54
# out >> [2, 3, 3, 3]

# in >> 9990
# out >> [2, 3, 3, 3, 5, 37]

# in >> 650
# out >> [2, 5, 5, 13]

def num_dividers(num):
    dividers = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            dividers.append(divisor)
            num = num // divisor
        else:
            divisor += 1
    return dividers


number = int(input("Введите натуральное число: "))
result = num_dividers(number)
print(result)
