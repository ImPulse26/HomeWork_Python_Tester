# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

digit = int(input("Введите натуральное число => "))
first_simple_digit = 2
lst = []
while first_simple_digit <= digit:
    if digit % first_simple_digit == 0:
        lst.append(first_simple_digit)
        digit //= first_simple_digit
        first_simple_digit = 2
    else:
        first_simple_digit += 1
print(lst)
