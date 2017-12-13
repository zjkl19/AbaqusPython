# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:47:05 2017

@author: ldn
"""
def ConnectPoints(*args):
    """Connect Points

    Required argument: points(tuple form) to connect

    Optional arguments:

    None.

    Return value: sorted connected points(tuple form)

    Exceptions:

    None.
    """
    lst=[]    #unsorted connected points
    for arg in args:
        for i in range(len(arg)):
            lst.append(arg[i])
            
    return lst

A_A=((0,0,0),(5,2,0),(115,2,0),(120,2,0))

B_B=((5,2,0),(10,8,0),(110,0,0),(115,2,0))
C_C=((10,8,0),(110,0,0))

ori=[(0,0,0),(5,2,0),(115,2,0),(120,2,0),(10,8,0),(110,0,0)]

sorted_ori=sorted(ori)

expected=((0,0,0),(5,2,0),(10,8,0),(110,0,0),(115,2,0),(120,2,0))

print(ConnectPoints(A_A,B_B,C_C))
