# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:07:43 2017

@author: ldn
"""


from scipy.optimize import fsolve

def func(i,coff):
    x=[0]*3
    x[0],x[1],x[2] = i[0], i[1], i[2]
    coff=1
    return[
            x[0]+x[1]-1,
            x[1]+x[2]-1,
            x[2]-2
          ]
    #return [i[0]+i[1]-1,i[1]+i[2]-1,i[2]-2]
    #return [i[0] + 2 * i[1] + 3 * i[2] - 6,5 * (i[0] ** 2) + 6 * (i[1] ** 2) + 7 * (i[2] ** 2) - 18,9 * (i[0] ** 3) + 10 * (i[1] ** 3) + 11 * (i[2] ** 3) - 30]             
c=1
coff=(1,)
r = fsolve(func,[0, 0, 0],coff)
print(r)

#            i[0] + 2 * i[1] + 3 * i[2] - 6,
#            5 * (i[0] ** 2) + 6 * (i[1] ** 2) + 7 * (i[2] ** 2) - 18,
#            9 * (i[0] ** 3) + 10 * (i[1] ** 3) + 11 * (i[2] ** 3) - 30

#            for j in range(0,3):
#                ast.literal_val('i[j]+i[j+1]-1,')      
#            i[2]=2

#%    z(1)-20.35,z(15)-z(1),z(8)-((1/2)*(z(1)+z(15))-9.00),...,
#%    Tx*(-1*((z(1)-z(2))/d(2))+(z(2)-z(3))/d(3))-(Wsi+Wci),...,
#%    Tx*(-1*((z(2)-z(3))/d(3))+(z(3)-z(4))/d(4))-(Wsi+Wci), ...,
