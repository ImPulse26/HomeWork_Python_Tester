# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

material_digit = input('Введите вещественное число => ')
summ_digits = 0
for i in material_digit:
    if i.isdigit():
        summ_digits += int(i)

print(f"Сумма цифр числа {material_digit}, равна {summ_digits}")


# 2 способ

# nmaterial_digit = input('Введите вещественное число => ')
# summ_digits = 0
# for i in material_digit:
#     if i != "." and i != "-":
#         summ_digits = summ_digits + int(i)
# print(f"Сумма цифр числа {material_digit}, равна {summ_digits}")