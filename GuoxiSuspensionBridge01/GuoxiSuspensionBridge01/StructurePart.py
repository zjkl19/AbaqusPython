class StructurePart(object):
    """Create 'Part' of the structure"""

    def __init__(self,structureModel,structureSketch,abaqusPart):
        self.structureModel=structureModel
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
        self.__CreateStiffeningGirderPart();
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

        towerPart1 = self.structureModel.Part(name='towerPart1', dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
        towerPart1.BaseWire(sketch=self.structureSketch.towerSketch[0])

        towerPart2 = self.structureModel.Part(name='towerPart2', dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
        towerPart2.BaseWire(sketch=self.structureSketch.towerSketch[1])

        self.towerPart=(towerPart1,towerPart2)

    def __CreateStiffeningGirderPart(self):
        """Create Tower Part
        
        function summary

        Args:


        Returns:

        Raises:
        """ 
        stiffeningGirderPart = self.structureModel.Part(name='beamPart', dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
        stiffeningGirderPart.BaseWire(sketch=self.structureSketch.stiffeningGirderSketch)
        self.stiffeningGirderPart=stiffeningGirderPart

        self.girderRigidarmPart=[]
        for i in range(len(self.structureSketch.girderRigidarmSketch)):
            girderRigidarmPart = self.structureModel.Part(name='girderRigidarmPart'+str(i+1), dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
            girderRigidarmPart.BaseWire(sketch=self.structureSketch.girderRigidarmSketch[i])
            self.girderRigidarmPart.append(girderRigidarmPart)
        
        self.girderRigidarmPart=tuple(self.girderRigidarmPart)
 
        
    def __CreateCablePart(self):
        """Create Cable Part
        
        function summary

        Args:


        Returns:

        Raises:
        """

        cablePart1 = self.structureModel.Part(name='cablePart1', dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
        cablePart1.BaseWire(sketch=self.structureSketch.cableSketch[0])

        cablePart2 = self.structureModel.Part(name='cablePart2', dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
        cablePart2.BaseWire(sketch=self.structureSketch.cableSketch[1])

        self.cablePart=(cablePart1,cablePart2)

    def __CreateSuspenderPart(self):
        """Create Suspender Part
        
        function summary

        Args:


        Returns:

        Raises:
        """
        self.suspenderPart=[]
        for i in range(len(self.structureSketch.suspenderSketch)):
            suspenderPart=[]
            for j in range(len(self.structureSketch.suspenderSketch[0])):
                sP = self.structureModel.Part(name='suspenderPart'+str(i+1)+'-'+str(j+1), dimensionality=self.abaqusPart.THREE_D, type=self.abaqusPart.DEFORMABLE_BODY)
                sP.BaseWire(sketch=self.structureSketch.suspenderSketch[i][j])
                suspenderPart.append(sP)
            self.suspenderPart.append(tuple(suspenderPart))
        
        self.suspenderPart=tuple(self.suspenderPart)

