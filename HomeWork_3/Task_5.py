# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def negafibonacci(digit):
    digit_1 = 0
    digit_2 = 1
    fibonacci_1 = [0]
    for i in range(digit):
        digit_1, digit_2 = digit_2, digit_1 + digit_2
        fibonacci_1.append(digit_1)
    digit_1 = 0
    digit_2 = 1
    fibonacci_2 = []
    for i in range(digit):
        digit_1, digit_2 = digit_2, digit_1 - digit_2
        fibonacci_2.append(digit_1)
    fibonacci_2.reverse()
    res = fibonacci_2 + fibonacci_1
    return res


digit = int(input('Введите число => '))

negaf = negafibonacci(digit)
print(negaf)
