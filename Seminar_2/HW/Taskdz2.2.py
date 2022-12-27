# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# N - 4 -> [1, 2, 6, 24]
# N - 6 -> [1, 2, 6, 24, 120, 720]

# # Решение 1

# n = int(input("Введите число: "))
# num_list = []
# k = 1
# for i in range(1, n + 1):
#     num_list.append(i*k)
#     k = i*k
# print(num_list)

# # Решение 2

num = int(input("Введите число: "))
sum_dig = 1
num_list = []
for i in range(num):
    sum_dig *= i + 1
    num_list.append(sum_dig)
print(num_list)