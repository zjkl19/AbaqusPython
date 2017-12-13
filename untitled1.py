# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 15:33:45 2017

@author: ldn
"""
"""create the mesh of the structrue"""
import os
import xlwt
m=[-1,-2,-3]

path=os.sys.path[0]
w=xlwt.Workbook()
ws=w.add_sheet('test')
for i in range(0,len(m)):
    ws.write(i,2,m[i])
localPath=os.path.join(path,'example.xls')
w.save(localPath)