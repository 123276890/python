# -*- coding: utf-8 -*-

from class_func import func


p = 6.58

m = func.conversion_price(p)
print(m)

f = func.json_final(1, 2, 3)
print(func.json_schemes(1, 2, 3, 5, f))

print(func.json_schemes(1, 2, 3, 4))