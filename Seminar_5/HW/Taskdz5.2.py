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