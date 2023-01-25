# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample


def random_list(count_digits):
    if count_digits <= 0:
        print("Ошибка, введите положительное число больше ")
        return []
    new_lst = sample(range(1, (count_digits + 1)*2), k=count_digits)
    return new_lst


def composition_pair_digits(lst, digit):
    composition_lst = []

    if len(lst) % 2 == 0:
        for i in range((len(lst)) // 2):
            pair_digits = lst[i] * lst[len(lst) - 1 - i]
            composition_lst.append(pair_digits)
        return composition_lst

    if len(lst) % 2:
        for i in range((len(lst)) // 2):
            pair_digits = lst[i] * lst[len(lst) - 1 - i]
            composition_lst.append(pair_digits)
        composition_lst.append(lst[((len(lst))//2)])
        return composition_lst


digit = int(input('Введите длину списка => '))

rnd_lst = random_list(digit)
print(rnd_lst)
pair_digits = composition_pair_digits(rnd_lst, digit)
print(pair_digits)
