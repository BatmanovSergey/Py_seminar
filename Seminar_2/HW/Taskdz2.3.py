# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.
# пример
# in -> 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

n = int(input("Введите число: "))
summ = 0
num_list = []
for n in range(1, n + 1):
    num_list.append(round(((1 + 1/n) ** n), 3))
print(num_list)

for i in range(0, n):
    summ = summ + num_list[i]
print(summ)