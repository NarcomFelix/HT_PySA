"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
"""

import timeit
import cProfile
# Копируем код из урока 2 и дорабатываем
def sieve_Erratosfen(n):
    HOLE = 0
    lenth_array = 10_000
    sieve = [i for i in range(lenth_array)]  # [] только для этой задачи, а не для ПЗ к уроку 2

    sieve[1] = HOLE
    for i in range(2, lenth_array):
        if sieve[i] != HOLE:
            j = i + i
            while j < lenth_array:
                sieve[j] = HOLE
                j += i

    #print(sieve)
    res = [item for item in sieve if item != HOLE]
    #print(res)
    #print(res[n-1])
    return res[n-1]


print(timeit.timeit('sieve_Erratosfen(10)', number=1000, globals=globals()))    # 3.9675199
print(timeit.timeit('sieve_Erratosfen(100)', number=1000, globals=globals()))   # 4.0850809
print(timeit.timeit('sieve_Erratosfen(1_000)', number=1000, globals=globals())) # 3.9830705

cProfile.run("sieve_Erratosfen(1_000)")

   #       6 function calls in 0.004 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
   #      1    0.003    0.003    0.004    0.004 PySA4.2.py:16(sieve_Erratosfen)
   #      1    0.000    0.000    0.000    0.000 PySA4.2.py:19(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 PySA4.2.py:30(<listcomp>)
   #      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Долго пишем и в итоге на хабре находим 7 вариантов решения, 3 из которых не правильно написал сам (при проверке,
# не до конца правильно работали https://habr.com/ru/post/122538/ Ну и правим под себя:
def natural_number(n,lenth_array):
    array = [1]

    for i in range(2,lenth_array+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            array.append(i)
    #print(array)
    #print(array[n-1])
    return array[n-1]

print(timeit.timeit('natural_number(10, 1_000)', number=1000, globals=globals()))    # 5.9892219
print(timeit.timeit('natural_number(100, 1_000)', number=1000, globals=globals()))   # 6.074429799999999
#print(timeit.timeit('natural_number(1_000, 10_000)', number=1000, globals=globals()))
# Если велечину массива, из которого создаётся массив простых чисел, сделать, как в 1ом варианте lenth_array = 10_000
# То всё виснет
cProfile.run("natural_number(1_000,10_000)")

   #       1233 function calls in 0.485 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.485    0.485 <string>:1(<module>)
   #      1    0.485    0.485    0.485    0.485 PySA4.2.py:57(natural_number)
   #      1    0.000    0.000    0.485    0.485 {built-in method builtins.exec}
   #   1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


