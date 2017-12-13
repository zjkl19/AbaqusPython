# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:23:46 2017

@author: ldn
"""

import numpy as np

a1=np.array([0.025,0.025,-0.019,-0.019])
a3=np.array([0.022,0.022,-0.011,-0.011])
a4=np.array([0.865,0.865,-0.667,-0.667])

print(1.368*a4)

b1=np.array([1.18,1.18,-0.91,-0.91])
b2=np.array([1.62,1.62,-1.25,-1.25])
b3=np.array([-1.5,-1.5,+1.14,+1.14])
b4=np.array([-0.88,-0.88,+0.44,+0.44])
print(b2+b3+b4)

P=10
l=2
E=1
I=1
k=100
r=(P*l**3/(16*E*I)-P/k)*l/(4/k+2*l**3/(3*E*I))
print(r)