# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange

list_length = int(input("Укажите длину списка => "))
lst = list(range(list_length))
print(f'{lst} - исходный список')

mixed_lst = lst
for i in range(list_length):
    rnd_index = randrange(list_length)
    temp = mixed_lst[i]
    mixed_lst[i] = mixed_lst[rnd_index]
    mixed_lst[rnd_index] = temp
print(f'{mixed_lst} - перемешанный список')