# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:44:38 2017

@author: ldn
"""

import logging
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

a=1
b=2
r=a+b
logging.debug(r)
l1=[]
l1.append(18)
l1.append(20)
logging.debug(l1)
l1.append(23)