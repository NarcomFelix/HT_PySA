"""
Определить, какое число в массиве встречается чаще всего.
"""
# Копипаст кода, создающего массив
import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

pos_array = []
for i in range(len(array)):
    n = 0
    for j in range(len(array)):
        if array[i] == array[j]:
            n += 1
    pos_array.append(n)


maximum = pos_array[0]
for i in range(len(pos_array)):
    if pos_array[i] >= maximum:
        maximum = pos_array[i]
        pos_max = i

print(f'{array[pos_max]} встречается {maximum} раз') #яплохогаваритьпаруски