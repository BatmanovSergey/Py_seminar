# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Примеры
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaavvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaavbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1v2b2w2P3u2T1Y1y2W2Q

# # Моё решение 

def string_to_rle(string):
    new_string = ""
    temp = string[0]
    count = 0
    for i in string:
        if temp == i:
            count+=1
        else:
            new_string += str(count)+temp
            temp = i
            count = 1
    new_string += str(count)+temp
    return new_string

def rle_to_string(string):
    new_string = ""
    amount = ""
    for i in string:
        if i.isdigit():
            amount += i
        else:
            num = int(amount)
            new_string += num*i
            amount = ""
    return new_string
    
with open('our_rle_text.txt', 'w', encoding='UTF-8') as file:
    our_rle_text = string_to_rle(input("Введите текст для сжатия: "))
    file.write(our_rle_text)
    print("Введёный текст сжат и записан!!!")

with open('our_rle_text.txt', 'r', encoding='UTF-8') as file:
    rle_text = file.readline()
    text_from_rle = rle_to_string(rle_text)
    with open('our_text.txt', 'w', encoding='UTF-8') as file:
        file.write(text_from_rle)
        print("Текст восстановлен и записан!!!")
    
# r = string_to_rle(input("Введите текст для сжатия: ").replace(" ", "")) удаляет все пробелы и склеивает строку

# # Решение на семинаре

# https://www.youtube.com/watch?v=q_N2Y6-O1xw&ab_channel=dinsky

from itertools import groupby, starmap
from os import path

def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")


def rle_decode(name):
    if path.exists(name):
        with open(name) as my_f:
            n = ""
            for k in my_f:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("The files do not exist in the system!")

# def rle_decode(name):
#     if path.exists(name):
#         with open(name) as my_f:
#             for i in my_f:
#                 word_nums = ["".join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
#                 print("".join([f"{int(word_nums[i]) * word_nums[i + 1]}" for i in range(0, len(word_nums), 2)]))
#     else:
#         print("The files do not exist in the system!")

# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
rle_decode(input("Enter the name of the file to decode: "))
