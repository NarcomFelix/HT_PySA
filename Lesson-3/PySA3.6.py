"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
# Копипаст кода, создающего массив
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

maximum = array[0]
minimum = array[0]
for i in range(len(array)):
    if array[i] >= maximum:
        maximum = array[i]
        pos_max = i
    if array[i] <= minimum:
        minimum = array[i]
        pos_min = i

print(f'{maximum = }')
print(f'{minimum = }')
print(f'{pos_max = }')
print(f'{pos_min = }')

summa = 0
if pos_min < pos_max:
    for i in range(pos_min + 1, pos_max):
        summa += array[i]
else:
    for i in range(pos_max + 1, pos_min):
        summa += array[i]
print(f'{summa = }')




