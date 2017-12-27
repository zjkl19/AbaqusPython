class StructurePart(object):
    """Create 'Part' of the structure"""

    def __init__(self,structureModel,structureGeometry,structureSketch,abaqusPart):
        self.structureModel=structureModel
        self.structureGeometry=structureGeometry
        self.structureSketch=structureSketch
        self.abaqusPart=abaqusPart
    
    def CreatePart(self):
        """Create Part
        
        function summary

        Args:


        Returns:

        Raises:
        """

        #design pattern: builder
        self.__CreateTowerPart();
        self.__CreateStiffeningGirderPart()
        self.__CreateGirderAddOnPart()
        self.__CreateGirderRigidArmPart()       
        self.__CreateCablePart();
        self.__CreateSuspenderPart();

    def __CreateTowerPart(self):
        """Create Tower Part
        
        function summary

        Args:


        Returns:

        Raises:
        """
        #global part
        for i in range(0,2):
            towerPart = self.structureModel.Part(name='towerPart'+str(i+1), dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
            towerPart.BaseWire(sketch=self.structureModel.sketches['towerSketch'+str(i+1)])
        
        #obsoleted code:
        #self.towerPart=(towerPart1,towerPart2)

    def __CreateStiffeningGirderPart(self):
        """Create Tower Part
        
        function summary

        Args:


        Returns:

        Raises:
        """ 
        stiffeningGirderPart = self.structureModel.Part(name='stiffeningGirderPart', dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
        stiffeningGirderPart.BaseWire(sketch=self.structureModel.sketches['stiffeningGirderSketch'])

        #stiffeningGirderPart.BaseWire(sketch=self.structureSketch.stiffeningGirderSketch)
        #self.stiffeningGirderPart=stiffeningGirderPart
 
    def __CreateGirderRigidArmPart(self):
        """Create Girder RigidArm Part
        
        function summary

        Args:


        Returns:

        Raises:
        """ 
        rGR=self.structureGeometry.rGirderRigidarmCoordinate

        self.girderRigidarmPart=[]
        #for i in range(len(self.structureSketch.girderRigidarmSketch)):
        for i in range(len(rGR)):
            girderRigidarmPart = self.structureModel.Part(name='girderRigidarmPart'+str(i+1), dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
            girderRigidarmPart.BaseWire(sketch=self.structureModel.sketches['girderRigidarmSketch'+str(i+1)])
            #self.girderRigidarmPart.append(girderRigidarmPart)
        
        #self.girderRigidarmPart=tuple(self.girderRigidarmPart)

    def __CreateGirderAddOnPart(self):
        """Create Girder AddOn Part
        """
        self.__CreateGirderWeightsSupportBeamPart()
        self.__CreateGirderTowerBeamPart()

    def __CreateGirderWeightsSupportBeamPart(self):
        """Create Girder Weights Support Beam Part
        """
        for i in range(0,2):    
            girderWeightsSupportBeamPart = self.structureModel.Part(name='girderWeightsSupportBeamPart'+str(i+1), dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
            girderWeightsSupportBeamPart.BaseWire(sketch=self.structureModel.sketches['girderWeightsSupportBeamSketch'+str(i+1)])

    def __CreateGirderTowerBeamPart(self):
        """Create Girder Tower Beam Part
        """
        for i in range(0,2):    #i belongs to {0,1}, west to east
            girderTowerBeamPart = self.structureModel.Part(name='girderTowerBeamPart'+str(i+1), dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
            girderTowerBeamPart.BaseWire(sketch=self.structureModel.sketches['girderTowerBeamSketch'+str(i+1)])
       
    def __CreateCablePart(self):
        """Create Cable Part
        
        function summary

        Args:


        Returns:

        Raises:
        """
        for i in range(0,2):
            cablePart = self.structureModel.Part(name='cablePart'+str(i+1), dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
            cablePart.BaseWire(sketch=self.structureModel.sketches['cableSketch'+str(i+1)])

        #self.cablePart=(cablePart1,cablePart2)

    def __CreateSuspenderPart(self):
        """Create Suspender Part
        
        function summary

        Args:


        Returns:

        Raises:
        """

        hP=self.structureGeometry.hangingPointCoordinate

#        self.suspenderPart=[]
        for i in range(len(hP)):
#            suspenderPart=[]
            for j in range(len(hP[i])):
                sP = self.structureModel.Part(name='suspenderPart'+str(i+1)+'-'+str(j+1), dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
                sP.BaseWire(sketch=self.structureModel.sketches['suspenderSketch'+str(i+1)+'-'+str(j+1)])
#                suspenderPart.append(sP)
#            self.suspenderPart.append(tuple(suspenderPart))
        
#        self.suspenderPart=tuple(self.suspenderPart)

