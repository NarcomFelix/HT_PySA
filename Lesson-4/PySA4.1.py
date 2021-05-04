"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""


"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
# Запишем как функцию (у меня просто два цикла было), и немного скорректируем задачу
# (будем менять диапазон натуральных чисел) и диапазон от 2 до 4


import timeit
import cProfile

def frequency(a,b):
    for i in range(2,5):
        n = 0
        for j in range(a,b):
            if j % i == 0:
                n += 1
        # если вывод делать - то очень долго до timeit ждать
        #print(f'кратность числу {i} в диапазоне от {a} до {b}: {n}')


print(timeit.timeit('frequency(0,10)', number=1000, globals=globals()))     # 0.010248999999999994
print(timeit.timeit('frequency(0,100)', number=1000, globals=globals()))    # 0.0463939
print(timeit.timeit('frequency(0,1_000)', number=1000, globals=globals()))  # 0.29812059999999996
print(timeit.timeit('frequency(0,10_000)', number=1000, globals=globals())) # 2.8355777
print(timeit.timeit('frequency(0,20_000)', number=1000, globals=globals())) # 5.7902087

cProfile.run("frequency(0,1_000_000)")

   #       4 function calls in 0.302 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.302    0.302 <string>:1(<module>)
   #      1    0.302    0.302    0.302    0.302 PySA4.1.py:22(frequency)
   #      1    0.000    0.000    0.302    0.302 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def frequency_while(a,b):
    for i in range(2,5):
        n = 0
        j = a
        while j < b:
            if j % i == 0:
                n += 1
            j += 1
        # если вывод делать - то очень долго до timeit ждать
        # print(f'кратность числу {i} в диапазоне от {a} до {b}: {n}')

print(timeit.timeit('frequency_while(0,10)', number=1000, globals=globals()))     # 0.004989199999999999
print(timeit.timeit('frequency_while(0,100)', number=1000, globals=globals()))    # 0.05493039999999999
print(timeit.timeit('frequency_while(0,1_000)', number=1000, globals=globals()))  # 0.6111970999999999
print(timeit.timeit('frequency_while(0,10_000)', number=1000, globals=globals())) # 5.5885183000000005
print(timeit.timeit('frequency_while(0,20_000)', number=1000, globals=globals())) # 10.791103000000001

cProfile.run("frequency_while(0,1_000_000)")

   #       4 function calls in 0.591 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.591    0.591 <string>:1(<module>)
   #      1    0.591    0.591    0.591    0.591 PySA4.1.py:50(frequency_while)
   #      1    0.000    0.000    0.591    0.591 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вот такое придумал, не знаю правильно ли, но код по факту разный
def frequency_for(a,b):
    # проверяем на кратность числам 2, 3, 4 (просто без цикла
    n = 0
    for j in range(a, b):
        if j % 2 == 0:
            n += 1
        # если вывод делать - то очень долго до timeit ждать
    #print(f'кратность числу 2 в диапазоне от {a} до {b}: {n}')
    n = 0
    for j in range(a, b):
        if j % 3 == 0:
            n += 1
    # если вывод делать - то очень долго до timeit ждать
    #print(f'кратность числу 3 в диапазоне от {a} до {b}: {n}')
    n = 0
    for j in range(a, b):
        if j % 4 == 0:
            n += 1
    # если вывод делать - то очень долго до timeit ждать
    #print(f'кратность числу 4 в диапазоне от {a} до {b}: {n}')

print(timeit.timeit('frequency_for(0,10)', number=1000, globals=globals()))     # 0.004798499999999997
print(timeit.timeit('frequency_for(0,100)', number=1000, globals=globals()))    # 0.022615800000000005
print(timeit.timeit('frequency_for(0,1_000)', number=1000, globals=globals()))  # 0.22348669999999998
print(timeit.timeit('frequency_for(0,10_000)', number=1000, globals=globals())) # 2.690346
print(timeit.timeit('frequency_for(0,20_000)', number=1000, globals=globals())) # 5.233605599999999

cProfile.run("frequency_for(0,1_000_000)")

   #       4 function calls in 0.283 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.282    0.282 <string>:1(<module>)
   #      1    0.282    0.282    0.282    0.282 PySA4.1.py:81(frequency_for)
   #      1    0.000    0.000    0.283    0.283 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод здесь: https://docs.google.com/spreadsheets/d/1RO4UlJLFC7q6G4AiaRUGeXCQgDbrt5kFGYqoYyltONQ/edit?usp=sharing