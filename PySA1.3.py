"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки.
"""
x1 = float(input("Введите координаты x1: "))
y1 = float(input("Введите координаты y1: "))
x2 = float(input("Введите координаты x2: "))
y2 = float(input("Введите координаты y2: "))

k = (y2-y1)/(x2-x1)
b = y1 - (y2-y1)/(x2-x1)*x1

print("y = ", round(k,2),"*x +", round(b,2))