"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
data = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(data)

def selection_bubble(array):
    n = 1
    while n < len(array):
        spam = 0
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                spam = +1
        if spam == 0: # если нет перестановок, то прерываем
            break
        n += 1
        #print(array)
        #print(spam)

selection_bubble(data)
print(data)