# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк. Без использования встроенной функции
# преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

decimal_digit = int(input('Введите число => '))
digit = decimal_digit
lst = []
while decimal_digit > 0:
    binary_digit = decimal_digit % 2
    lst.append(binary_digit)
    # print(lst)
    decimal_digit = decimal_digit//2

print(f'Число {digit} в двоичной сиситеме счисления равно {list(reversed(lst))}')
