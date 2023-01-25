# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

n = int(
    input("Введите N для заполнения пустого списка в диапзоне [-N, N] => "))
position_one = int(input("Укажите номер позиции первого числа => "))
position_two = int(input("Укажите номер позиции второго числа => "))

if 0 <= position_one <= n*2+1 and 0 <= position_two <= n*2+1:
    lst = list(range(-n, n+1))
    print(lst)

    # lst = []                  /второй способ
    # for i in range(n*2+1):
    #     lst.append(-n + i)
    # print(lst)

    multiplication_positions = lst[position_one-1] * lst[position_two-1]

    print(
        f'Произведение элементов на позициях {position_one}({lst[position_one-1]}) и {position_two}({lst[position_two-1]}) равно {multiplication_positions}')
else:
    print('В заданном диапазоне данных(-ой) позиций(-ии) не существует')
