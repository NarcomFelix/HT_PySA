"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы
с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

● написать 3 варианта кода (один у вас уже есть);

● проанализировать 3 варианта и выбрать оптимальный;

● результаты анализа (количество занятой памяти в вашей среде разработки)
вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС
и интерпретатора Python;

● написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.
"""


"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

# Windows 10 х64
# Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32


import random
import sys

############## 1


SIZE = 10 #28
MIN_ITEM = 0 #24
MAX_ITEM = 100 #28
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array) #464 = 280+184
#544

# lst = [i for i in range(11)]
# print(array) # 184
#
# print(sys.getsizeof(array))
# for item in array:
#     print(sys.getsizeof(item)) # 280


maximum = array[0] #28
minimum = array[0] #28

for i in range(len(array)):
    if array[i] >= maximum:
        maximum = array[i]
        pos_max = i #28 вот тут значения меняются от 24 до 28, в зависимости от random, в цикле они могут
                    # появиться несколько раз, но насколько я понимаю, они перезаписываются
    if array[i] <= minimum:
        minimum = array[i]
        pos_min = i #28
#112

print(f'{maximum = }')
print(f'{minimum = }')
print(f'{pos_max = }')
print(f'{pos_min = }')

new_array = array #464

new_array[pos_max], new_array[pos_min] = new_array[pos_min], new_array[pos_max]
#здесь новые переменные не создаются - или я не прав? но память то

print(new_array)
print('#####################')
#!!!!Результат 1120 = 544 + 112 + 464

############## 2

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
#544

maximum = array[0]
minimum = array[0]
for i in range(len(array)):
    if array[i] >= maximum:
        maximum = array[i]
        pos_max = i
    if array[i] <= minimum:
        minimum = array[i]
        pos_min = i
#112
print(f'{maximum = }')
print(f'{minimum = }')
print(f'{pos_max = }')
print(f'{pos_min = }')

new_array = array #464

new_array.pop(pos_max)
new_array.insert(pos_max, minimum)
new_array.pop(pos_min)
new_array.insert(pos_min, maximum)

print(new_array)
print('#####################')
#!!!!Результат 1120 = 544 + 112 + 464
############## 3

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
#544

maximum = array[0] #28
minimum = array[0] #28
i = 0 #28 (т.к меняться будет)
while i < len(array):
    if array[i] >= maximum:
        maximum = array[i]
        pos_max = i #28
    if array[i] <= minimum:
        minimum = array[i]
        pos_min = i #28
    i += 1
# 140
print(f'{maximum = }')
print(f'{minimum = }')
print(f'{pos_max = }')
print(f'{pos_min = }')

new_array = array #464

new_array[pos_max], new_array[pos_min] = new_array[pos_min], new_array[pos_max]
new_array = tuple(new_array) # - 464 + 400 мы же можем на кортеж заменить финальные значения
                             # (по ассимтотике не очень, но для нашеё задачи хорошо)
print(new_array)

# lst = [i for i in range(11)]
# print(new_array) # 120
#
# print(sys.getsizeof(new_array))
# for item in new_array:
#     print(sys.getsizeof(item)) # 280

#!!!!Результат 1084 = 544 + 140 + 464 - 464 + 400

# Вывод.
# 1. Варианты решения 1 и 2 одинаковы по затратам памяти на переменные. Тут я "попал в ловушку по ассимптотике".
# (понял уже, когда сделал и переслушивал разбор задания). В 3ьем варианте поменял на кортеж - ассимптокику ухудшил,
# но на хранение данных меньше памяти.
# 2. При написаниии кода нужно учитывать очень много (с практикой приходит автоматизм). Конкретно к этому заданию:
# и данные учитывать нужно, и ассимптотику.
# 3. Если бы использовал только массивы и добавлял каждый раз в массив новую переменную, то в конце бы у меня
# получился массив со всеми переменными. И вот его - то можно бы было посчитать, а не как я каждый раз.