# -*- coding: utf-8 -*-
"""


@author: ldn
"""

import sys

sys.path.append('D:\ProgramData\Anaconda3\Lib\site-packages')

import xlrd

data=xlrd.open_workbook('modelData.xlsx')
sh=data.sheet_by_name('Sheet1')

print(sh.cell_value(1,1))

print(sh.cell_value(0,0))

