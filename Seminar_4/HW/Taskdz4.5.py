# ** 5. Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример:
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        file_list = []
        for line in file:
            file_list.append(line.strip("= 0\n"))
        return file_list

poly_1_list = read_file("poly_1.txt")
poly_2_list = read_file("poly_2.txt")

if len(poly_1_list) == len(poly_2_list):
    with open("poly_u.txt", "a", encoding="utf-8") as poly_u:
        for i in range(len(poly_1_list)):
            poly_string = poly_1_list[i] + " + " + poly_2_list[i] + " = 0"
            poly_u.write(f'{poly_string}\n')
        print('Информация в файл записана')
else:
    with open("poly_u.txt", "a", encoding="utf-8") as poly_u:
        poly_u.write('Содержимое файлов не совпадает')
    print('Содержимое файлов не совпадает')

        




