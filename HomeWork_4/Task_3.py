# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
#  исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import *


def random_list(count_digits: int):
    if count_digits <= 0:
        print("Ошибка, введите положительное число")
        return []
    new_lst = choices(range(1, count_digits+1), k=count_digits)
    return new_lst


def unique_numbers(lst: list):
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            new_lst.append(i)
    return new_lst


digit = int(input('Введите длину списка => '))
rnd_lst = random_list(digit)
print(rnd_lst)
unique_num = unique_numbers(rnd_lst)
print(unique_num)
