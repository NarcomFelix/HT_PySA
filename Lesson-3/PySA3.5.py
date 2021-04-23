"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

# Копипаст кода, создающего массив
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

minus_array = []
for i in range(len(array)):
    if array[i] < 0:
        minus_array.append(array[i])

minimum = (minus_array[0])
for i in range(len(minus_array)):
    if abs(minus_array[i]) < abs(minimum):
        minimum = minus_array[i]


print(minus_array)
print(f'Максимальный отрицательный элемент = {minimum}')
print(f'Позиция в массиве: ', array.index(minimum))
