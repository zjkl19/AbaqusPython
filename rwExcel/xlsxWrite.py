# -*- coding: utf-8 -*-
"""


@author: ldn
"""

import sys, os.path

sys.path.append('D:\ProgramData\Anaconda3\Lib\site-packages')

import xlwt

path=sys.path[0]

w=xlwt.Workbook()

ws=w.add_sheet('test')

for i in range(10):
    ws.write(i,2,i)

localPath=os.path.join(path,'example.xls')

w.save(localPath)


