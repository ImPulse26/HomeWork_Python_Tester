# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import sample

def random_list(count_digits):
    if count_digits <= 0:
        print("Ошибка, введите положительное число больше ")
        return []
    new_lst = sample(range(1, (count_digits + 1)*2), k=count_digits)
    return new_lst


def amount_odd_positions(lst):
    sum_pos = 0
    for i in range(0, len(lst), 2):
        sum_pos += lst[i]
    return sum_pos


digit = int(input('Введите длину списка => '))

rnd_lst = random_list(digit)
print(rnd_lst)
sum_pos = amount_odd_positions(rnd_lst)
print(sum_pos)
