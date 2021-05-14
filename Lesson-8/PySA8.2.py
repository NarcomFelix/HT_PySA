"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter

array = input('Введите строку: ')

#for i in array:

c = dict(Counter(array))
c_keys = c.keys()
c_values = c.values()

print(c_keys)
print(c_values)
print(c)
# d ={}
# d_keys = []
# d_values = []
# k = len(c)
# while k > 0:
#     d_keys.append(c_keys[k])
#     d_values.append(c_values[k])
#     k -= 1

# c_keys = reversed(c.keys())
# c_values = reversed(c.values())
# c_rev = dict(zip(c_keys, c_values))

# print(c)
# print(c_rev)
# print(d_keys)
# print(d_keys)
# print(len(c))

