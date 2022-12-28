# 1. Вычислить число c заданной точностью d
# in
# пример
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988


from decimal import Decimal
number = Decimal(input("Введите натуральное число: "))
accuracy = str(input("Введите требуемую точность в формате '0.0001': "))
print(number.quantize(Decimal(accuracy)))

# # Решение 2 (работает только для вещественных чисел)

# from decimal import Decimal, getcontext

# number = Decimal(input("Введите натуральное число: "))
# accuracy = Decimal(input("Введите требуемую точность: "))
# count = 1
# while accuracy != int(accuracy):
#     accuracy = accuracy * 10
#     count+=1

# getcontext().prec = count
# print(number*1)
