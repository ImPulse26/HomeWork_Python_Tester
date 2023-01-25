# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def sort_name (name_lst):
    final_lst = {}
    for name in name_lst:
        first_letter = name[0]
        if first_letter not in final_lst:
            final_lst[first_letter] = []
        final_lst[first_letter].append(name)
    return final_lst

name = input('Введите имена через пробел => ').split()
print(sort_name(name))