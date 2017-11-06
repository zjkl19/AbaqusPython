class StructureAssembly(object):
    """Create 'Assembly' of the structure"""


    def __init__(self,structureModel,structurePart,structureAssembly):
        
        self.structureModel=structureModel
        self.structurePart=structurePart
        self.structureAssembly=structureAssembly


    def CreateAssembly(self,structureGeometry):
        """Create Assembly
        
        function summary

        Args:


        Returns:

        Raises:
        """
        self.__CreateInstance()
        self.__MoveInstance(structureGeometry)
        self.__MergeInstance()

    def __CreateInstance(self):
        """Create Instance
        
        function summary

        Args:


        Returns:

        Raises:
        """
        from abaqusConstants import *
        p = self.structureModel.parts['towerPart1']  
        self.structureAssembly.Instance(name='towerInstance1', part=p, dependent=ON)
        p = self.structureModel.parts['towerPart2']
        self.structureAssembly.Instance(name='towerInstance2', part=p, dependent=ON)

        p = self.structureModel.parts['beamPart']
        self.structureAssembly.Instance(name='beamInstance', part=p, dependent=ON)

        for i in range(len(self.structurePart.girderRigidarmPart)):       
            p = self.structureModel.parts['girderRigidarmPart'+str(i+1)]
            self.structureAssembly.Instance(name='girderRigidarmInstance'+str(i+1), part=p, dependent=ON)

        p = self.structureModel.parts['cablePart1']
        self.structureAssembly.Instance(name='cableInstance1', part=p, dependent=ON)
        p = self.structureModel.parts['cablePart2']
        self.structureAssembly.Instance(name='cableInstance2', part=p, dependent=ON)


        for i in range(len(self.structurePart.suspenderPart)):
            for j in range(len(self.structurePart.suspenderPart[0])):
                p = self.structureModel.parts['suspenderPart'+str(i+1)+'-'+str(j+1)]
                self.structureAssembly.Instance(name='suspenderInstance'+str(i+1)+'-'+str(j+1), part=p, dependent=ON)

    def __MoveInstance(self,structureGeometry):
        """Move Instance: Translate and rotate Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        self.__MoveTowerInstance()
        self.__MoveStiffeningGirderInstance()
        self.__MoveGirderRigidarmInstance(structureGeometry)
        self.__MoveCableInstance()
        self.__MoveSuspenderInstance(structureGeometry)

    def __MergeInstance(self):
        """Merge Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        from abaqusConstants import *
        a1 = self.structureModel.rootAssembly
        a1.InstanceFromBooleanMerge(name='PartAll', instances=(
            a1.instances['towerInstance1'], a1.instances['towerInstance2'], 
            a1.instances['beamInstance'], a1.instances['girderRigidarmInstance1'], 
            a1.instances['girderRigidarmInstance2'], 
            a1.instances['girderRigidarmInstance3'], 
            a1.instances['girderRigidarmInstance4'], 
            a1.instances['girderRigidarmInstance5'], 
            a1.instances['girderRigidarmInstance6'], 
            a1.instances['girderRigidarmInstance7'], 
            a1.instances['girderRigidarmInstance8'], 
            a1.instances['girderRigidarmInstance9'], 
            a1.instances['girderRigidarmInstance10'], 
            a1.instances['girderRigidarmInstance11'], 
            a1.instances['girderRigidarmInstance12'], 
            a1.instances['girderRigidarmInstance13'], 
            a1.instances['girderRigidarmInstance14'], 
            a1.instances['girderRigidarmInstance15'], 
            a1.instances['girderRigidarmInstance16'], 
            a1.instances['girderRigidarmInstance17'], 
            a1.instances['girderRigidarmInstance18'], 
            a1.instances['girderRigidarmInstance19'], a1.instances['cableInstance1'], 
            a1.instances['cableInstance2'], a1.instances['suspenderInstance1-1'], 
            a1.instances['suspenderInstance1-2'], a1.instances['suspenderInstance1-3'], 
            a1.instances['suspenderInstance1-4'], a1.instances['suspenderInstance1-5'], 
            a1.instances['suspenderInstance1-6'], a1.instances['suspenderInstance1-7'], 
            a1.instances['suspenderInstance1-8'], a1.instances['suspenderInstance1-9'], 
            a1.instances['suspenderInstance1-10'], 
            a1.instances['suspenderInstance1-11'], 
            a1.instances['suspenderInstance1-12'], 
            a1.instances['suspenderInstance1-13'], 
            a1.instances['suspenderInstance1-14'], 
            a1.instances['suspenderInstance1-15'], 
            a1.instances['suspenderInstance1-16'], 
            a1.instances['suspenderInstance1-17'], 
            a1.instances['suspenderInstance1-18'], 
            a1.instances['suspenderInstance1-19'], 
            a1.instances['suspenderInstance2-1'], a1.instances['suspenderInstance2-2'], 
            a1.instances['suspenderInstance2-3'], a1.instances['suspenderInstance2-4'], 
            a1.instances['suspenderInstance2-5'], a1.instances['suspenderInstance2-6'], 
            a1.instances['suspenderInstance2-7'], a1.instances['suspenderInstance2-8'], 
            a1.instances['suspenderInstance2-9'], 
            a1.instances['suspenderInstance2-10'], 
            a1.instances['suspenderInstance2-11'], 
            a1.instances['suspenderInstance2-12'], 
            a1.instances['suspenderInstance2-13'], 
            a1.instances['suspenderInstance2-14'], 
            a1.instances['suspenderInstance2-15'], 
            a1.instances['suspenderInstance2-16'], 
            a1.instances['suspenderInstance2-17'], 
            a1.instances['suspenderInstance2-18'], 
            a1.instances['suspenderInstance2-19'], ), originalInstances=SUPPRESS, 
            domain=GEOMETRY)

    def __MoveTowerInstance(self):
        self.structureAssembly.translate(instanceList=('towerInstance1', ), vector=(0.0, 0.0, -3.75))
        self.structureAssembly.rotate(instanceList=('towerInstance1', ), axisPoint=(25.0, (3.3+20.44)/2, -3.75), 
            axisDirection=(0.0, 8.57, 0.0), angle=-90.0)

        self.structureAssembly.translate(instanceList=('towerInstance2', ), vector=(0.0, 0.0, -3.75))
        self.structureAssembly.rotate(instanceList=('towerInstance2', ), axisPoint=(95.0, (3.3+20.44)/2, -3.75), 
            axisDirection=(0.0, 8.57, 0.0), angle=-90.0)
    
    def __MoveStiffeningGirderInstance(self):
        pass

    def __MoveGirderRigidarmInstance(self,structureGeometry):
        rGR=structureGeometry.rGirderRigidarmCoordinate

        for i in range(len(self.structurePart.girderRigidarmPart)): 
            self.structureAssembly.rotate(instanceList=('girderRigidarmInstance'+str(i+1), ), axisPoint=rGR[i],
                axisDirection=(0, 1, 0), angle=90.0)

    def __MoveCableInstance(self):
        self.structureAssembly.translate(instanceList=('cableInstance1', ), vector=(0.0, 0.0, -3.75))
        self.structureAssembly.translate(instanceList=('cableInstance2', ), vector=(0.0, 0.0, 3.75))

    def __MoveSuspenderInstance(self,structureGeometry):
        """move Suspender Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        for i in range(len(self.structurePart.suspenderPart)):
            for j in range(len(self.structurePart.suspenderPart[0])):
                self.structureAssembly.translate(instanceList=('suspenderInstance'+str(i+1)+'-'+str(j+1), ), vector=(0.0, 0.0, structureGeometry.rRigidarmSuspenderCoordinate[i][0][2]))
