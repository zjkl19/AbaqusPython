# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:23:03 2017

@author: ldn
"""
def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l

def downDim(tup):
    for i in range(len(tup)):
        yield tup[i]


#stiffingGirder:
EndPointCoordinate=((-3.6,7.355,0.0),(123.6,7.355,0.0))    #west & east end point
rGirderRigidarmCoordinate=((10,8.13,0),(15,8.3675,0),(20,8.58,0),
    (30,8.93,0),(35,9.0675,0),(40,9.18,0),(45,9.2675,0),(50,9.33,0),(55,9.3675,0),
    (60,9.38,0),
    (65,9.3675,0),(70,9.33,0),(75,9.2675,0),(80,9.18,0),(85,9.0675,0),(90,8.93,0),
    (100,8.58,0),(105,8.3675,0),(110,8.13,0))
GirderB_BCoordinate=((9.735286,8.115441,0),	(10.249718,8.141862,0),	(14.74465,8.355371,0),
    (15.249775,8.378115,0),	(19.745716,8.569193,0),	(20.249824,8.589368,0),	(29.747493,8.921794,0),
    (30.249906,8.936872,0),	(34.748205,9.060576,0),	(35.249937,9.073124,0),	(39.748798,9.174348,0),
    (40.249962,9.184374,0),	(44.749273,9.263112,0),	(45.24998,9.270625,0),	(49.749629,9.32687,0),
    (50.249993,9.331875,0),	(54.749866,9.365624,0),	(55.249999,9.368125,0),	(59.749985,9.379375,0),
    (60.249999,9.379375,0),	(64.749985,9.368125,0),	(65.249993,9.365625,0),	(69.749866,9.331876,0),
    (70.24998,9.326875,0),	(74.749629,9.27063,0),	(75.249962,9.263126,0),	(79.749273,9.184388,0),
    (80.249937,9.174376,0),	(84.748798,9.073152,0),	(85.249906,9.060628,0),	(89.748205,8.936924,0),
    (90.249868,8.921879,0),	(99.746664,8.5895,0),	(100.249775,8.569385,0), (104.745716,8.378307,0),
    (105.249718,8.355638,0),	(109.74465,8.142129,0),	(110.249623,8.116271,0))
GirderD_DCoordinate=((24.247015,8.739263,0), (25.749604,8.791862,0),(94.247757,8.791948,0),(95.749473,8.739395,0))

GirderA_ACoordinate=GirderB_BCoordinate[1:5] \
     +(GirderB_BCoordinate[5],GirderD_DCoordinate[0],GirderD_DCoordinate[1],GirderB_BCoordinate[6])  \
     +GirderB_BCoordinate[7:len(GirderB_BCoordinate)-1-3*2]  \
     +(GirderB_BCoordinate[len(GirderB_BCoordinate)-1-3*2],GirderD_DCoordinate[2],GirderD_DCoordinate[3],GirderB_BCoordinate[len(GirderB_BCoordinate)-1-3*2+1])  \
     +GirderB_BCoordinate[len(GirderB_BCoordinate)-1-2*2:len(GirderB_BCoordinate)-1] 

GirderE_ECoordinate=((-1.454187,7.489113,0),(1.248114,7.648646,0),(118.736796,7.649476,0),(121.454187,7.489113,0)) 

GirderC_CCoordinate=((3.993964,7.799668,0),GirderB_BCoordinate[0],GirderB_BCoordinate[-1],(115.990946,7.800498,0))

GirderF_FCoordinate=(EndPointCoordinate[0],GirderE_ECoordinate[0],GirderE_ECoordinate[1],GirderC_CCoordinate[0],GirderC_CCoordinate[3],GirderE_ECoordinate[2],GirderE_ECoordinate[3],EndPointCoordinate[1])

rGirderCableSpringCoordinate=((-1.454187,7.489113,0),	(121.454187,7.489113,0))

GirderWeightsSupportCoordinate=((0,7.58,0),(120,7.58,0))

GirderTowerSupportCoordinate=((25.0,8.7675,0),(95.0,8.7675,0))

rRigidarmSuspenderCoordinate=(((10,7.73,-3.75),(15,7.9675,-3.75),(20,8.18,-3.75),
    (30,8.53,-3.75),(35,8.6675,-3.75),(40,8.78,-3.75),(45,8.8675,-3.75),(50,8.93,-3.75),(55,8.9675,-3.75),
    (60,8.98,-3.75),
    (65,8.9675,-3.75),(70,8.93,-3.75),(75,8.8675,-3.75),(80,8.78,-3.75),(85,8.6675,-3.75),(90,8.53,-3.75),
    (100,8.18,-3.75),(105,7.9675,-3.75),(110,7.73,-3.75)),

    ((10,7.73,3.75),(15,7.9675,3.75),(20,8.18,3.75),
    (30,8.53,3.75),(35,8.6675,3.75),(40,8.78,3.75),(45,8.8675,3.75),(50,8.93,3.75),(55,8.9675,3.75),
    (60,8.98,3.75),
    (65,8.9675,3.75),(70,8.93,3.75),(75,8.8675,3.75),(80,8.78,3.75),(85,8.6675,3.75),(90,8.53,3.75),
    (100,8.18,3.75),(105,7.9675,3.75),(110,7.73,3.75)))
"""
GirderList=(EndPointCoordinate,rGirderRigidarmCoordinate,GirderB_BCoordinate,GirderC_CCoordinate,
            GirderD_DCoordinate,GirderE_ECoordinate,GirderF_FCoordinate,
            rGirderCableSpringCoordinate,GirderWeightsSupportCoordinate,    #all nodes that forms girder
            GirderTowerSupportCoordinate)
"""
GirderTotal=EndPointCoordinate+rGirderRigidarmCoordinate+GirderA_ACoordinate    \
    +GirderB_BCoordinate+GirderC_CCoordinate+GirderD_DCoordinate    \
    +GirderE_ECoordinate+GirderF_FCoordinate+rGirderCableSpringCoordinate    \
    +GirderWeightsSupportCoordinate+GirderTowerSupportCoordinate    


SortedGirderTotal = list(set(list(GirderTotal)))

SortedGirderTotal.sort()

SortedGirderTotal=tuple(SortedGirderTotal)

print(SortedGirderTotal)

GirderTowerTraverseBeamCoordinate=((25,8.7675,0),	(95,8.7675,0),(25,8.7675,0),(95,8.7675,0))
GirderTowerSupportCoordinate=()
#GirderList1=list(map(lambda x:x[0],GirderList))

#GirderList.sort()
#GirderList = list(set(GirderList))

#tuple(map(lambda x:x[0],GirderB_BCoordinate[1:5]))

#print(GirderList)
#print(GirderB_BCoordinate[1:5])