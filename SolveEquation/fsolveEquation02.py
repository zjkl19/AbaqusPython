# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:07:43 2017

节线法
the knob-line method

目前程序中的限制：
1、吊杆间距一致
2、不计算y坐标
3、吊杆在横向也是竖直

参考文献：
1、自锚式悬索桥的力学特征和设计研究   刘涛
2、用midas civil做悬索桥分析-实例解析.pdf
文献2 P7(页码3) （地锚式悬索桥）将附属构件的荷载换算成集中荷载，加载吊杆下端节点上。

主缆和吊杆的自重需要通过反复迭代计算才能确定（因为只有确定了主缆坐标位置才能确定重量）

主缆荷载和加劲梁相比太小了，初步找形可以忽略不计。  ---林迪南

计算依据：莆田市绶溪公园一期过溪桥图纸（含变更内容）



1#、2#塔顶塔顶ip点坐标：

(25,-3.75,20.35),（95,3.75,20.35）

跨中坐标:

(60,-3.75,11.35),(60,3.75,11.35)

@author: ldn
"""


from scipy.optimize import fsolve

#函数名：平衡方程
#传入参数:
#solu:list,[Tx,z[0],z[1],z[2],...]
#其中,z[i],i=0,1,2,...,nKnobs(节点数)
#d:list,吊杆间距
#Wsi:
#Wci:
#_z:已知左端,中点,右端的z坐标
#返回参数:
#Tx:水平力
#z:吊杆z坐标
   
def balanceFunc(solu,d,Wsi,Wci,z_):
    nKnobs=len(d)+1
    Tx=solu[0]
    z=[0]*nKnobs
    for i in range(0,nKnobs):
        z[i]=solu[i+1]
    solveStr=""    #求解用字符串
    for i in range(0,nKnobs-2):
        solveStr=solveStr+'Tx*(-1*((z['+str(i)+']-z['+str(i+1)+'])/d['+str(i)+'])+(z['+str(i+1)+']-z['+str(i+2)+'])/d['+str(i+1)+'])-(Wsi['+str(i)+']+Wci['+str(i)+']),'
    solveStr=solveStr+'z[0]-'+str(z_[0])+','
    solveStr=solveStr+'z['+str(nKnobs-1)+']-'+str(z_[2])+','
    solveStr=solveStr+'z['+str(int(0.5*(0+nKnobs-1)))+']-'+str(z_[1])
        #Tx*(-1*((z(1)-z(2))/d(2))+(z(2)-z(3))/d(3))-(Wsi+Wci),...,
    print(solveStr)

    retStr='['+solveStr+']'
    return(eval(retStr))
    #return [i[0]+i[1]-1,i[1]+i[2]-1,i[2]-2]
    #return [i[0] + 2 * i[1] + 3 * i[2] - 6,5 * (i[0] ** 2) + 6 * (i[1] ** 2) + 7 * (i[2] ** 2) - 18,9 * (i[0] ** 3) + 10 * (i[1] ** 3) + 11 * (i[2] ** 3) - 30]             

#基本参数尽可能列在此处

#荷载作用下，悬索上每一点下垂的距离称为垂度（不严谨？）
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
#    Wsi.append((deadLoad*d[j]+deadLoad*d[j+1])/2)        #近似认为梁段之间的恒载由两根吊杆平分。 --林迪南理解
    Wsi.append((deadLoad*d[j]+deadLoad*d[j+1])/2/2)    #第2个除以2的原因是双索面
#Wci[i]:第(i+1)根主缆力                                              #参考数值：438.275 单位:kN
Wci=[]
for j in range(0,nKnobs-2):
    Wci.append(0)    #初步分析中，忽略主缆重量，3.75 单位:kN,主缆自重可忽略不计（林迪南理解）  

#initialValue=[0]*(nKnobs+1)
initialValue=[-5900,20.35,17,16,15,14,13,12,11.35,12,13,14,15,16,17,20.35]
#-5965.00 ?
              
z_=[20.35,11.35,20.35]
argTuple=(d,Wsi,Wci,z_,)

r = fsolve(balanceFunc,initialValue,argTuple)
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
