# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
#  точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

number_quarter = int(input("Введите номер четверти => "))

if 0 <= number_quarter >= 5:
    print('Такой четверти нет')
if number_quarter == 1:
    print('x > 0, y > 0')
if number_quarter == 2:
    print('x < 0, y > 0')
if number_quarter == 3:
    print('x < 0, y < 0')
if number_quarter == 4:
    print('x > 0, y < 0')