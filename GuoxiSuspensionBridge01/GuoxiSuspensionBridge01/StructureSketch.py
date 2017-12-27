class StructureSketch(object):
    """Create 'Sketch' of the structure"""
 
    def __init__(self,structureModel,structureGeometry):
        """init

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        self.structureGeometry=structureGeometry
        self.structureModel=structureModel

    def CreateSketch(self):
        """Create Sketch
        
        function summary

        Args:
            structureGeometry: structureGeometry instance

        Returns:

        Raises:
        """

        #design pattern: builder
        self.__CreateTowerSketch()
        self.__CreateStiffeningGirderSketch()
        self.__CreateGirderAddOn()
        self.__CreateGirderRigidarmSketch()
        self.__CreateCableSketch()
        self.__CreateSuspenderSketch()


    def __CreateTowerSketch(self):
        """CreateTowerSketch
        
        function summary

        Args:

        Returns:

        Raises:
        """

        #Tower:
        """obsoleted code
        dTB=self.structureGeometry.downTowerBottomCoordinate
        rUD=self.structureGeometry.rUpDownTowerCoordinate
        uTT=self.structureGeometry.upTowerTopCoordinate

        self.towerSketch=[]

        for i in range(0,2):
            mySketch = self.structureModel.ConstrainedSketch(name='towerSketch'+str(i+1),sheetSize=10.0)
            
            mySketch.Line(point1=(dTB[0][i][0],dTB[0][i][1]), point2=(rUD[0][i][0],rUD[0][i][1]))
            mySketch.Line(point1=(rUD[0][i][0],rUD[0][i][1]), point2=(uTT[0][i][0],uTT[0][i][1]))
            mySketch.Line(point1=(uTT[0][i][0],uTT[0][i][1]), point2=(uTT[1][i][0]+(uTT[1][i][2]-uTT[0][i][2]),uTT[1][i][1]))
            mySketch.Line(point1=(uTT[1][i][0]+(uTT[1][i][2]-uTT[0][i][2]),uTT[1][i][1]), point2=(rUD[1][i][0]+(rUD[1][i][2]-rUD[0][i][2]),rUD[1][i][1]))
            mySketch.Line(point1=(rUD[1][i][0]+(rUD[1][i][2]-rUD[0][i][2]),rUD[1][i][1]), point2=(dTB[1][i][0]+(dTB[1][i][2]-dTB[0][i][2]),dTB[1][i][1]))
            
            self.towerSketch.append(mySketch)

        self.towerSketch=tuple(self.towerSketch)
        """
   
        TT=self.structureGeometry.TowerTopCoordinate
        TB=self.structureGeometry.TowerBottomCoordinate
        TB01=self.structureGeometry.TowerBeam01Coordinate
        TB02=self.structureGeometry.TowerBeam02Coordinate
        TB03=self.structureGeometry.TowerBeam03Coordinate
        TB04=self.structureGeometry.TowerBeam04Coordinate

        TB01ColumnPointer=(0,3)
        for i in range(0,2):    #i belongs to {0,1}, west to east
            mySketch = self.structureModel.ConstrainedSketch(name='towerSketch'+str(i+1),sheetSize=10.0)
                  
            #column 01,02
            for j in range(0,2):
                mySketch.Line(point1=(TB[i][j][0]+TB[i][j][2],TB[i][j][1]), point2=(TB01[i][TB01ColumnPointer[j]][0]+TB01[i][TB01ColumnPointer[j]][2],TB01[i][TB01ColumnPointer[j]][1]))
                mySketch.Line(point1=(TB01[i][TB01ColumnPointer[j]][0]+TB01[i][TB01ColumnPointer[j]][2],TB01[i][TB01ColumnPointer[j]][1]), point2=(TB02[i][j][0]+TB02[i][j][2],TB02[i][0][1]))
                mySketch.Line(point1=(TB02[i][j][0]+TB02[i][j][2],TB02[i][j][1]), point2=(TB03[i][j][0]+TB03[i][j][2],TB03[i][j][1]))
                mySketch.Line(point1=(TB03[i][j][0]+TB03[i][j][2],TB03[i][j][1]), point2=(TB04[i][j][0]+TB04[i][j][2],TB04[i][j][1]))
                mySketch.Line(point1=(TB04[i][j][0]+TB04[i][j][2],TB04[i][j][1]), point2=(TT[i][j][0]+TT[i][j][2],TT[i][j][1]))

            #towerBeam01
            mySketch.Line(point1=(TB01[i][0][0]+TB01[i][0][2],TB01[i][0][1]), point2=(TB01[i][1][0]+TB01[i][1][2],TB01[i][1][1]))        
            mySketch.Line(point1=(TB01[i][1][0]+TB01[i][1][2],TB01[i][1][1]), point2=(TB01[i][2][0]+TB01[i][2][2],TB01[i][2][1])) 
            mySketch.Line(point1=(TB01[i][2][0]+TB01[i][2][2],TB01[i][2][1]), point2=(TB01[i][3][0]+TB01[i][3][2],TB01[i][3][1])) 

            #towerBeam02
            mySketch.Line(point1=(TB02[i][0][0]+TB02[i][0][2],TB02[i][0][1]), point2=(TB02[i][1][0]+TB02[i][1][2],TB02[i][1][1]))        

            #towerBeam03
            mySketch.Line(point1=(TB03[i][0][0]+TB03[i][0][2],TB03[i][0][1]), point2=(TB03[i][1][0]+TB03[i][1][2],TB03[i][1][1]))        

            #towerBeam04
            mySketch.Line(point1=(TB04[i][0][0]+TB04[i][0][2],TB04[i][0][1]), point2=(TB04[i][1][0]+TB04[i][1][2],TB04[i][1][1]))        

    def __CreateStiffeningGirderSketch(self):
        """Create Stiffening Girder Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """

        """obsoleted code    
        eP=self.structureGeometry.EndPointCoordinate
        rGR=self.structureGeometry.rGirderRigidarmCoordinate
        rRS=self.structureGeometry.rRigidarmSuspenderCoordinate

        #stiffeningGirderCoordinate=(eP[0],rGRC[0],eP[1])
        lst=[]
        lst.append(eP[0])
        for i in range(len(rGR)):
            lst.append(rGR[i])
        lst.append(eP[1])
        stiffeningGirderCoordinate=tuple(lst)
        
        sG=stiffeningGirderCoordinate
        
        mySketch = self.structureModel.ConstrainedSketch(name='stiffeningGirderSketch',sheetSize=10.0)

        for i in range(len(sG)-1):
            mySketch.Line(point1=(sG[i][0],sG[i][1]), point2=(sG[i+1][0],sG[i+1][1]))
        
        self.stiffeningGirderSketch=mySketch
        """
        mySketch = self.structureModel.ConstrainedSketch(name='stiffeningGirderSketch',sheetSize=10.0)

        sG=self.structureGeometry.stiffeningGirderCoordinate
        for i in range(len(sG)-1):
            mySketch.Line(point1=(sG[i][0],sG[i][1]), point2=(sG[i+1][0],sG[i+1][1]))

    def __CreateGirderAddOn(self):
        """Create Girder Add-On
        """
        self.__CreateGirderWeightsSupportBeam()
        self.__CreateGirderTowerBeamSketch()
        pass

    def __CreateGirderWeightsSupportBeam(self):
        """Create Girder Weights Support Beam Sketch
        """
        GWB=self.structureGeometry.GirderWeightsBeamCoordinate
        GWS=self.structureGeometry.GirderWeightsSupportCoordinate

        for i in range(0,2):    #i belongs to {0,1}, west to east
            mySketch = self.structureModel.ConstrainedSketch(name='girderWeightsBeamSketch'+str(i+1),sheetSize=10.0)
            mySketch.Line(point1=(GWB[i][0][0]+GWB[i][0][2],GWB[i][0][1]), point2=(GWS[i][0],GWS[i][1]))       
            mySketch.Line(point1=(GWS[i][0],GWS[i][1]), point2=(GWB[i][1][0]+GWB[i][1][2],GWB[i][1][1]))
  
    def __CreateGirderTowerBeamSketch(self):
        """Create Girder Tower Beam Sketch
        """

        GTB=self.structureGeometry.GirderTowerBeamCoordinate
        GTS=self.structureGeometry.GirderTowerSupportCoordinate

        for i in range(0,2):    #i belongs to {0,1}, west to east
            mySketch = self.structureModel.ConstrainedSketch(name='girderTowerBeamSketch'+str(i+1),sheetSize=10.0)
            mySketch.Line(point1=(GTB[i][0][0]+GTB[i][0][2],GTB[i][0][1]), point2=(GTS[i][0],GTS[i][1]))       
            mySketch.Line(point1=(GTS[i][0],GTS[i][1]), point2=(GTB[i][1][0]+GTB[i][1][2],GTB[i][1][1]))
         

    def __CreateGirderRigidarmSketch(self):
        """Create Girder Rigidarm Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """    
        rGR=self.structureGeometry.rGirderRigidarmCoordinate
        rRS=self.structureGeometry.rRigidarmSuspenderCoordinate

        #create GirderRigidarm Sketch
        girderRigidarmSketch=[]
        for i in range(len(rGR)):
            mySketch = self.structureModel.ConstrainedSketch(name='girderRigidarmSketch'+str(i+1),sheetSize=10.0)
            mySketch.Line(point1=(rRS[0][i][0]+rRS[0][i][2],rRS[0][i][1]), point2=(rGR[i][0],rGR[i][1]))
            mySketch.Line(point1=(rGR[i][0],rGR[i][1]), point2=(rRS[1][i][0]+rRS[1][i][2],rRS[1][i][1]))
            girderRigidarmSketch.append(mySketch)   #rRS[0][i][2] is negative

        self.girderRigidarmSketch=tuple(girderRigidarmSketch)        

    def __CreateCableSketch(self):
        """Create Cable Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """
         #cable   
        cableCoordinate=self.structureGeometry.cableCoordinate

        self.cableSketch=[]
        cableSketch=[]
        for i in range(len(cableCoordinate)):
            mySketch = self.structureModel.ConstrainedSketch(name='cableSketch'+str(i+1),sheetSize=10.0)
            for j in range(len(cableCoordinate[i])-1):
                mySketch.Line(point1=(cableCoordinate[i][j][0],cableCoordinate[i][j][1]), point2=(cableCoordinate[i][j+1][0],cableCoordinate[i][j+1][1]))
            cableSketch.append(mySketch)
        self.cableSketch=tuple(cableSketch)

    def __CreateSuspenderSketch(self):
        """Create Suspender Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """
        
        hP=self.structureGeometry.hangingPointCoordinate
        rRS=self.structureGeometry.rRigidarmSuspenderCoordinate             

        self.suspenderSketch=[]
        suspenderSketch=[]
        for i in range(len(rRS)):
            for j in range(len(rRS[0])):
                mySketch = self.structureModel.ConstrainedSketch(name='suspenderSketch'+str(i+1)+'-'+str(j+1),sheetSize=10.0)
                mySketch.Line(point1=(hP[i][j][0],hP[i][j][1]), point2=(rRS[i][j][0],rRS[i][j][1]))
                suspenderSketch.append(mySketch)   
            self.suspenderSketch.append(tuple(suspenderSketch))
        
        self.suspenderSketch=tuple(self.suspenderSketch)
     