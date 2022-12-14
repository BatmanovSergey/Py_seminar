# 5. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

import math
print('Введите координаты первой точки')
x1 = int(input('X1: '))
y1 = int(input('Y1: '))
print('Введите координаты второй точки')
x2 = int(input('X2: '))
y2 = int(input('Y2: '))

result = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
print(f'Расстояние между заданными точками = {round(result, 3)}')
