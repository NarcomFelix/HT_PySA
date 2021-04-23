"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
"""

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a > b:
    if a > c:
        if b > c:
            print(f'среднее = {b}')
        else:
            print(f'среднее = {c}')
    else:
        print(f'среднее = {a}')
else:
    if b > c:
        if a > c:
            print(f'среднее = {a}')
        else:
            print(f'среднее = {c}')
    else:
        print(f'среднее = {b}')

