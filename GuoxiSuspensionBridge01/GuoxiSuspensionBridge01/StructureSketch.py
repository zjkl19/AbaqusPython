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
        self.__CreateGirderRigidarmSketch()
        self.__CreateCableSketch()
        self.__CreateSuspenderSketch();

    def __CreateTowerSketch(self):
        """CreateTowerSketch
        
        function summary

        Args:

        Returns:

        Raises:
        """

        #Tower:

        dTB=self.structureGeometry.downTowerBottomCoordinate
        rUD=self.structureGeometry.rUpDownTowerCoordinate
        uTT=self.structureGeometry.upTowerTopCoordinate

        self.towerSketch=[]

        for i in range(0,2):
            mySketch = self.structureModel.ConstrainedSketch(name='towerSketch'+str(i+1),sheetSize=10.0)
            #dTB[0][0][0]: 1# tower, 1# tower column, x coordinate
            mySketch.Line(point1=(dTB[i][0][0],dTB[i][0][1]), point2=(rUD[i][0][0],rUD[i][0][1]))
            mySketch.Line(point1=(rUD[i][0][0],rUD[i][0][1]), point2=(uTT[i][0][0],uTT[i][0][1]))
            mySketch.Line(point1=(uTT[i][0][0],uTT[i][0][1]), point2=(uTT[i][1][0]+(uTT[i][1][2]-uTT[i][0][2]),uTT[i][1][1]))
            mySketch.Line(point1=(uTT[i][1][0]+(uTT[i][1][2]-uTT[i][0][2]),uTT[i][1][1]), point2=(rUD[i][1][0]+(rUD[i][1][2]-rUD[i][0][2]),rUD[i][1][1]))
            mySketch.Line(point1=(rUD[i][1][0]+(rUD[i][1][2]-rUD[i][0][2]),rUD[i][1][1]), point2=(dTB[i][1][0]+(dTB[i][1][2]-dTB[i][0][2]),dTB[i][1][1]))
            self.towerSketch.append(mySketch)


        self.towerSketch=tuple(self.towerSketch)

    def __CreateStiffeningGirderSketch(self):
        """Create Stiffening Girder Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """    
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
                mySketch = self.structureModel.ConstrainedSketch(name='girderRigidarmSketch'+str(i+1)+'-'+str(j+1),sheetSize=10.0)
                mySketch.Line(point1=(hP[i][j][0],hP[i][j][1]), point2=(rRS[i][j][0],rRS[i][j][1]))
                suspenderSketch.append(mySketch)   
            self.suspenderSketch.append(tuple(suspenderSketch))
        
        self.suspenderSketch=tuple(self.suspenderSketch)
     