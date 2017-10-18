# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:07:43 2017

@author: ldn
"""


from scipy.optimize import fsolve

def func(i):
    #x, y, z = i[0], i[1], i[2]
    return [
            i[0] + 2 * i[1] + 3 * i[2] - 6,
            5 * (i[0] ** 2) + 6 * (i[1] ** 2) + 7 * (i[2] ** 2) - 18,
            9 * (i[0] ** 3) + 10 * (i[1] ** 3) + 11 * (i[2] ** 3) - 30
           ]
    
r = fsolve(func,[0, 0, 0])
print(r)
