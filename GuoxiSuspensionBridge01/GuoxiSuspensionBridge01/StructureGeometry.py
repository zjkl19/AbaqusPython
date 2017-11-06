class StructureGeometry(object):
    """store the structure geometry information of the structure"""
    
    #Tower:
    downTowerBottomCoordinate=(((25,3.3,-3.75),(25,3.3,3.75)),
                                ((95,3.3,-3.75),(95,3.3,3.75)))     #west & east
    rUpDownTowerCoordinate=(((25,8.127,-3.75),(25,8.127,3.75)),
                                ((95,8.127,-3.75),(95,8.127,3.75)))
    upTowerTopCoordinate=(((25,20.44,-3.75),(25,20.44,3.75)),
                                ((95,20.44,-3.75),(95,20.44,3.75)))

    #stiffingGirder:
    EndPointCoordinate=((-3.6,7.355,0.0),(123.6,7.355,0.0))    #west & east end point
    rGirderRigidarmCoordinate=((10,8.13,0),(15,8.3675,0),(20,8.58,0),
        (30,8.93,0),(35,9.0675,0),(40,9.18,0),(45,9.2675,0),(50,9.33,0),(55,9.3675,0),
        (60,9.38,0),
        (65,9.3675,0),(70,9.33,0),(75,9.2675,0),(80,9.18,0),(85,9.0675,0),(90,8.93,0),
        (100,8.58,0),(105,8.3675,0),(110,8.13,0))
    
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

    
    #cable
    anchorPointCoordinate=(((1.45,6.473,-3.75),(121.45,6.473,-3.75)),   #northern 1#  
                            ((1.45,6.473,3.75),(121.45,6.473,3.75)))    #southern 2#
  
    hangingPointCoordinate=(((10,11.270569,-3.75),(15,13.906819,-3.75),(20,16.903937,-3.75),
        (30,17.92136,-3.75),(35,15.940382,-3.75),(40,14.319928,-3.75),(45,13.059819,-3.75),(50,12.159874,-3.75),(55,11.619961,-3.75),
        (60,11.44,-3.75),
        (65,11.619961,-3.75),(70,12.159874,-3.75),(75,13.059819,-3.75),(80,14.319928,-3.75),(85,15.940382,-3.75),(90,17.92136,-3.75),
        (100,16.903937,-3.75),(105,13.906819,-3.75),(110,11.270569,-3.75)), 
        
        ((10,11.270569,3.75),(15,13.906819,3.75),(20,16.903937,3.75),
        (30,17.92136,3.75),(35,15.940382,3.75),(40,14.319928,3.75),(45,13.059819,3.75),(50,12.159874,3.75),(55,11.619961,3.75),
        (60,11.44,3.75),
        (65,11.619961,3.75),(70,12.159874,3.75),(75,13.059819,3.75),(80,14.319928,3.75),(85,15.940382,3.75),(90,17.92136,3.75),
        (100,16.903937,3.75),(105,13.906819,3.75),(110,11.270569,3.75))) 


    #suspender

    def __init__(self):
        self.__SetCableCoordinate()    #calc the cable coordinate
        self.__SetStiffeningGirderCoordinate() 

    def __SetCableCoordinate(self):
        """set the cable coordinate

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        aP=self.anchorPointCoordinate
        hP=self.hangingPointCoordinate
        uTT=self.upTowerTopCoordinate
        
        cableCoordinate=[]
        for i in range(len(aP)):
            lst=[]
            lst.append(aP[i][0])
            for j in range(len(hP[i])):
                if j==3:
                    lst.append(uTT[0][i])
                elif j==16:
                    lst.append(uTT[1][i])
                lst.append(hP[i][j])
            lst.append(aP[i][1])
            cableCoordinate.append(tuple(lst))
        cableCoordinate=tuple(cableCoordinate)
        self.cableCoordinate=cableCoordinate
    
    def __SetStiffeningGirderCoordinate(self):
        """set the stiffening girder coordinate

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        eP=self.EndPointCoordinate
        rGR=self.rGirderRigidarmCoordinate
        rRS=self.rRigidarmSuspenderCoordinate

        lst=[]
        lst.append(eP[0])
        for i in range(len(rGR)):
            lst.append(rGR[i])
        lst.append(eP[1])
        self.stiffeningGirderCoordinate=tuple(lst)   