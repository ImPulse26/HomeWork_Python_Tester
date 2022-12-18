# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D
#  пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

x1 = int(input("Введите x1 => "))
y1 = int(input("Введите y1 => "))
x2 = int(input("Введите x2 => "))
y2 = int(input("Введите y2 => "))

AC = x2 - x1
BC = y2 - y1

AB = (AC**2 + BC**2)**0.5

print(f'При координатах x1 = {x1}, x2 = {x2}, y1 = {y1} и y2 = {y2} расстояние равно {AB:.3f}')
