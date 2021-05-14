"""
1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""
import hashlib

def func1(s):
    if len(s) < 2:
        return print(0)
    else:
        k = 0
        hash_help = []
        while k < len(s)-1:
            for i in range(len(s) - k):
                a = []
                for j in range(i,i+k+1):
                    a.append(s[j])
                b = [''.join(a)]

                hash_help.append(b)
            k += 1
        hash_del = []
        for x in hash_help:
            if x not in hash_del:
                hash_del.append(x)

        return print(hash_help), print(hash_del), print(len(hash_del))

# Прикрутил хэш функцию к тому же самому:
def func2(s):
    if len(s) < 2:
        return print(0)
    else:
        k = 0
        hash_help = []
        while k < len(s)-1:
            for i in range(len(s) - k):
                a = []
                for j in range(i,i+k+1):
                    a.append(s[j])
                b = [''.join(a)]

                hash_b = hash(tuple(b))
                hash_help.append(hash_b)
            k += 1
        hash_del = []
        for x in hash_help:
            if x not in hash_del:
                hash_del.append(x)

        return print(hash_help), print(hash_del), print(len(hash_del))

func1('adsds')
func2('adsds')


