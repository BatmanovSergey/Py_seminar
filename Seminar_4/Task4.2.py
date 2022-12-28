# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.
# Пример
# Enter the coefficient 'a': 1
# Enter the coefficient 'b': 2
# Enter the coefficient 'c': -3

# Enter the coefficient 'a': 5
# Enter the coefficient 'b': 6
# Enter the coefficient 'c': -7

# Enter the coefficient 'a': 8
# Enter the coefficient 'b': 9
# Enter the coefficient 'c': -10

# 1x ** 2 + 2x + -3
# The first root: 1.00
# The first root: -3.00
# 5x ** 2 + 6x + -7
# The first root: 0.73
# The first root: -1.93
# 8x ** 2 + 9x + -10
# The first root: 0.69
# The first root: -1.81

from math import sqrt
def find_r(a, b, c):
    d = b**2 - 4*a*c
    with open("Diskr.txt", "a", encoding="utf-8") as my_f:
        my_f.write(F"{a}x2 + {b}x + {c} = 0\n")
        if d > 0:
            x1 = (-b - sqrt(d))/ (2*a)
            x2 = (-b + sqrt(d))/ (2*a)
            my_f.write(f"{x1, x2}\n")
        elif d == 0:
            x = -b/ (2*a)
            my_f.write(f"{x}\n")
        else:
            my_f.write("нет корней\n")

find_r(8, 9, -10)
