# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 18:56:32 2017

@author: ldn
"""

f=9.00   #中跨吊点垂度

#-----
#使abaqus python可以使用anaconda3中的模块
import sys
extModulePath='D:\ProgramData\Anaconda3\Lib\site-packages'    #扩展模块路径
sys.path.append(extModulePath)
#-----

import xlrd

modelFileName='modelData.xlsx'
sheetName='steeveInterval'

sht_steeveInterval='steeveInterval'
sht_anchorCoordinate='anchorCoordinate'

#steeveInterval
#anchorCoordinate

data=xlrd.open_workbook(modelFileName)

sh=data.sheet_by_name(sht_steeveInterval)

nKnobs=sh.nrows-1+1   #number of knobs
#-1表示减掉表头行
#+1表示点数比距离数多1

#initial list
d=[]    #吊杆间距
for j in range(1,sh.nrows):
    d.append(sh.cell_value(j,1))

#xlrd example:
#print(sh.nrows)
#print(sh.cell_value(0,0))
#print(sh.cell_value(1,1))

#恒荷载
#可以根据过溪桥主要材料数量表计算
#其中：
#主梁自重：141.35KN/m
#二期恒载:18.47+7.68
#索鞍自重、吊杆锚具自重、索夹自重若干（初步分析中忽略不计）

deadLoad=175.31    #恒载,deadLoad:KN/m

#Wsi[i]:第(i+1)根吊杆力
Wsi=[]
for j in range(0,nKnobs-2):
    Wsi.append((deadLoad*d[j]+deadLoad*d[j+1])/2)        #近似认为梁段之间的恒载由两根吊杆平分。 --林迪南理解

#Wci[i]:第(i+1)根主缆力                                              #参考数值：438.275 单位:kN
Wci=[]
for j in range(0,nKnobs-2):
    Wci.append(0)    #初步分析中，忽略主缆重量，3.75 单位:kN,主缆自重可忽略不计（林迪南理解）  

initialValue=[0]*(nKnobs+1)
              
z_=[20.35,11.35,20.35]
argTuple=(d,Wsi,Wci,z_,)

nKnobs=len(d)+1
solu=[0]*(nKnobs+1)
Tx=solu[0]
z=[0]*nKnobs
for i in range(0,nKnobs):
    z[i]=solu[i+1]
solveStr=""    #求解用字符串
for i in range(0,nKnobs-2):
    solveStr=solveStr+'Tx*(-1*((z['+str(i)+']-z['+str(i+1)+'])/d['+str(i)+'])+(z['+str(i+1)+']-z['+str(i+2)+'])/d['+str(i+1)+'])-(Wsi['+str(i)+']+Wci['+str(i)+']),'
solveStr=solveStr+'z[0]-'+str(z_[0])+','
solveStr=solveStr+'z['+str(nKnobs-2)+']-'+str(z_[2])+','
solveStr=solveStr+'z['+str(int(0.5*(nKnobs+1)))+']-'+str(z_[1])
    #Tx*(-1*((z(1)-z(2))/d(2))+(z(2)-z(3))/d(3))-(Wsi+Wci),...,

retStr='['+solveStr+']'

