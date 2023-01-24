# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

with open('text_words.txt', 'w', encoding='UTF-8') as my_f:
    my_f.write(input('Введите текст для сжатия => '))

with open('text_words.txt', 'r', encoding='UTF-8') as my_f:
    string = my_f.readline()


def coding(my_text_words):
    encoding_str = ''
    count = 1
    if not my_text_words:
        return ''
    for i in range(1, len(my_text_words)):
        if my_text_words[i] == my_text_words[i - 1]:
            count += 1
        else :
            if count == 1:
                encoding_str += my_text_words[i - 1]
            else:
                encoding_str += str(count) + my_text_words[i - 1]
                count = 1
    else:
        if count == 1:
            encoding_str += my_text_words[i]
        else:
            encoding_str += str(count) + my_text_words[i]
        return encoding_str


def decoding(encoding_str):
    decode_str = ''
    count = ''
    for i in encoding_str:
        if i.isdigit():
            count += i
        else:
            decode_str += i * int(count)
            count = ''
    return decode_str


with open('text_words.txt', 'r', encoding='UTF-8') as my_f:
    my_text_words = my_f.read()

with open('text_code_word.txt', 'w', encoding='UTF-8') as my_f:
    my_text_code_word = coding(my_text_words)
    my_f.write(my_text_code_word)   

print(f'Раскодированная запись: {my_text_words}')
print(f'Закодированная запись:  {coding(my_text_words)}')