# * 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.
# Пример
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

from random import choice

def polynomial(n: int, path: str) -> str:
    poly_string = ""
    with open(path, "a", encoding="utf-8") as file:
        y = choice(range(1, 9))
        poly_string = poly_string +(f"{y}*x^{n} ")
        n-=1
        while n >= 0:
            y = choice(range(0, 9))
            if n > 1:
                if y > 0:
                    poly_string = poly_string + (f"+ {y}*x^{n} ")
                elif y < 0:
                    poly_string = poly_string + (f"- {y*-1}*x^{n} ") 
            elif n == 1:
                if y > 0:
                    poly_string = poly_string + (f"+ {y}*x ")
                elif y < 0:
                    poly_string = poly_string + (f"- {y*-1}*x ")        
            if n == 0:
                if y > 0:
                    poly_string = poly_string + (f'+ {y} = 0')
                elif y < 0:
                    poly_string = poly_string + (f'- {y*-1} = 0')
                else:
                    poly_string = poly_string + '= 0'
            n-=1   
        file.write(f'{poly_string}\n')
        return poly_string

number = input('Введите натуральное число: ')
if number.isdigit() and int(number) > 0:
    print(polynomial(int(number), "poly_2.txt"))
    print('Информация в файл записана')
else:
    print('Введено некорректное значение.')
