# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

# lst = [28 20 10 5 1 24 7 15 23 25]

original_lst = [int(i) for i in input('Введите числа через пробел => ').split()]
final_lst = [original_lst[i] for i in range(1, len(original_lst)) if original_lst[i] > original_lst[i-1]]
print(f'Исходный список => {original_lst}')
print(f'Итоговый список => {final_lst}')