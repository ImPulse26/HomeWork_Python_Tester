# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба............
#
# бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

from random import sample


def rnd_list(digit: int):
    lst = []
    word = 'абв'
    temp = 0
    if digit < 0:
        print("Некорректное значение")
    else:
        while temp < digit:
            rnd_word = sample(word, k=3)
            lst.append(''.join(rnd_word))
            temp += 1
    return lst


def removing_words(lst):
    new_lst = []
    temp = [new_lst.append(i) for i in lst if i != 'абв']
    return new_lst


digit = int(input('Укажите количество слов => '))
lst1 = rnd_list(digit)
print(lst1)
lst2 = removing_words(lst1)
print(lst2)