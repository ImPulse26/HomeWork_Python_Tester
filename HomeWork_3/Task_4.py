# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

from random import uniform


def random_list(count_digits):
    lst = []
    if count_digits <= 0:
        print("Ошибка, введите положительное число больше 0")
        return [0.0]
    for i in range(count_digits):
        num = round((uniform(0, (count_digits+1) * 2)), 2)
        lst.append(num)
    return lst


def difference_min_max(lst):
    min_digit = lst[0] % 1
    max_digit = 0
    for i in range(len(lst)):
        if max_digit < lst[i] % 1:
            max_digit = lst[i] % 1
        if min_digit > lst[i] % 1:
            min_digit = lst[i] % 1
    difference = round((max_digit - (min_digit)), 2)
    print(f"Минимум {min_digit:.2f} максимум {max_digit:.2f} разница {difference:.2f}")
    return difference

digit = int(input('Введите длину списка => '))

rnd_lst = random_list(digit)
print(rnd_lst)
difference_min_max(rnd_lst)
