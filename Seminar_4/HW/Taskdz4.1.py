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

# from decimal import Decimal, getcontext
# number = Decimal(input("Введите натуральное число: "))
# accuracy = Decimal(input("Введите требуемую точность: "))
# print(accuracy)
# while accuracy<0:
#         accuracy*=10
# print(accuracy)    

# getcontext().prec=accuracy
# print(number)
