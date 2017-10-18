# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:07:43 2017

@author: ldn
"""


from scipy.optimize import fsolve

def func(i):
    x, y, z = i[0], i[1], i[2]
    return [
            x + 2 * y + 3 * z - 6,
            5 * (x ** 2) + 6 * (y ** 2) + 7 * (z ** 2) - 18,
            9 * (x ** 3) + 10 * (y ** 3) + 11 * (z ** 3) - 30
           ]
    
r = fsolve(func,[0, 0, 0])
print(r)
