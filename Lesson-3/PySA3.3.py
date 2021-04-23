"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

new_array = array

new_array[pos_max], new_array[pos_min] = new_array[pos_min], new_array[pos_max]
# new_array.pop(pos_max)
# new_array.insert(pos_max, minimum)
# new_array.pop(pos_min)
# new_array.insert(pos_min, maximum)

print(new_array)

# Работает, вроде надёжно, но как-то некрасиво... всё с опытом