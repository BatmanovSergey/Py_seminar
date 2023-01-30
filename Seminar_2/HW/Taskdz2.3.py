# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.
# пример
# in -> 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

# # Решение 1

n = int(input("Введите число: "))
summ = 0
num_list = []
for i in range(1, n + 1):
    num_list.append(round(((1 + 1/i) ** i), 3))
print(num_list)

for i in range(0, n):
    summ = summ + num_list[i]
print(summ)

# # Решение 2

# num = int(input("Введите число: "))
# sum_nums = 0
# list_nums = []
# for i in range(1, num + 1):
#     result = round((1 + 1 / i) ** i, 3)
#     list_nums.append(result)
#     sum_nums += result
# print(list_nums)
# print(sum_nums)