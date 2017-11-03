# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan

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
        self.__SetCableCoordinate()     #calc the cable coordinate

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

class StructureSketch(object):
    """Create 'Sketch' of the structure"""

    
    def __init__(self):
        pass
    def CreateSketch(self,structureGeometry):
        """Create Sketch
        
        function summary

        Args:
            structureGeometry: structureGeometry instance

        Returns:

        Raises:
        """

        #design pattern: builder
        self.__CreateTowerSketch(structureGeometry)
        self.__CreateStiffeningGirderSketch(structureGeometry)
        self.__CreateGirderRigidarmSketch(structureGeometry)
        self.__CreateCableSketch(structureGeometry)
        self.__CreateSuspenderSketch(structureGeometry);

    def __CreateTowerSketch(self,structureGeometry):
        """CreateTowerSketch
        
        function summary

        Args:

        Returns:

        Raises:
        """
        
        #global myModel

        #Tower:

        dTB=structureGeometry.downTowerBottomCoordinate
        rUD=structureGeometry.rUpDownTowerCoordinate
        uTT=structureGeometry.upTowerTopCoordinate

        self.towerSketch=[]

        for i in range(0,2):
            mySketch = myModel.ConstrainedSketch(name='towerSketch'+str(i+1),sheetSize=10.0)
            #dTB[0][0][0]: 1# tower, 1# tower column, x coordinate
            mySketch.Line(point1=(dTB[i][0][0],dTB[i][0][1]), point2=(rUD[i][0][0],rUD[i][0][1]))
            mySketch.Line(point1=(rUD[i][0][0],rUD[i][0][1]), point2=(uTT[i][0][0],uTT[i][0][1]))
            mySketch.Line(point1=(uTT[i][0][0],uTT[i][0][1]), point2=(uTT[i][1][0]+(uTT[i][1][2]-uTT[i][0][2]),uTT[i][1][1]))
            mySketch.Line(point1=(uTT[i][1][0]+(uTT[i][1][2]-uTT[i][0][2]),uTT[i][1][1]), point2=(rUD[i][1][0]+(rUD[i][1][2]-rUD[i][0][2]),rUD[i][1][1]))
            mySketch.Line(point1=(rUD[i][1][0]+(rUD[i][1][2]-rUD[i][0][2]),rUD[i][1][1]), point2=(dTB[i][1][0]+(dTB[i][1][2]-dTB[i][0][2]),dTB[i][1][1]))
            self.towerSketch.append(mySketch)


        self.towerSketch=tuple(self.towerSketch)

    def __CreateStiffeningGirderSketch(self,structureGeometry):
        """Create Stiffening Girder Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """    
        eP=structureGeometry.EndPointCoordinate
        rGR=structureGeometry.rGirderRigidarmCoordinate
        rRS=structureGeometry.rRigidarmSuspenderCoordinate

        #stiffeningGirderCoordinate=(eP[0],rGRC[0],eP[1])
        lst=[]
        lst.append(eP[0])
        for i in range(len(rGR)):
            lst.append(rGR[i])
        lst.append(eP[1])
        stiffeningGirderCoordinate=tuple(lst)
        
        sG=stiffeningGirderCoordinate
        
        mySketch = myModel.ConstrainedSketch(name='stiffeningGirderSketch',sheetSize=10.0)

        for i in range(len(sG)-1):
            mySketch.Line(point1=(sG[i][0],sG[i][1]), point2=(sG[i+1][0],sG[i+1][1]))
        
        self.stiffeningGirderSketch=mySketch
      

    
    def __CreateGirderRigidarmSketch(self,structureGeometry):
        """Create Girder Rigidarm Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """    
        rGR=structureGeometry.rGirderRigidarmCoordinate
        rRS=structureGeometry.rRigidarmSuspenderCoordinate

        #create GirderRigidarm Sketch
        girderRigidarmSketch=[]
        for i in range(len(rGR)):
            mySketch = myModel.ConstrainedSketch(name='girderRigidarmSketch'+str(i+1),sheetSize=10.0)
            mySketch.Line(point1=(rRS[0][i][0]+rRS[0][i][2],rRS[0][i][1]), point2=(rGR[i][0],rGR[i][1]))
            mySketch.Line(point1=(rGR[i][0],rGR[i][1]), point2=(rRS[1][i][0]+rRS[1][i][2],rRS[1][i][1]))
            girderRigidarmSketch.append(mySketch)   #rRS[0][i][2] is negative

        self.girderRigidarmSketch=tuple(girderRigidarmSketch)        

    def __CreateCableSketch(self,structureGeometry):
        """Create Cable Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """
         #cable   
        cableCoordinate=structureGeometry.cableCoordinate

        #global myModel

        self.cableSketch=[]
        cableSketch=[]
        for i in range(len(cableCoordinate)):
            mySketch = myModel.ConstrainedSketch(name='cableSketch'+str(i+1),sheetSize=10.0)
            for j in range(len(cableCoordinate[i])-1):
                mySketch.Line(point1=(cableCoordinate[i][j][0],cableCoordinate[i][j][1]), point2=(cableCoordinate[i][j+1][0],cableCoordinate[i][j+1][1]))
            cableSketch.append(mySketch)
        self.cableSketch=tuple(cableSketch)

    def __CreateSuspenderSketch(self,structureGeometry):
        """Create Suspender Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """
        
        hP=structureGeometry.hangingPointCoordinate
        rRS=structureGeometry.rRigidarmSuspenderCoordinate             

        self.suspenderSketch=[]
        suspenderSketch=[]
        for i in range(len(rRS)):
            for j in range(len(rRS[0])):
                mySketch = myModel.ConstrainedSketch(name='girderRigidarmSketch'+str(i+1)+'-'+str(j+1),sheetSize=10.0)
                mySketch.Line(point1=(hP[i][j][0],hP[i][j][1]), point2=(rRS[i][j][0],rRS[i][j][1]))
                suspenderSketch.append(mySketch)   
            self.suspenderSketch.append(tuple(suspenderSketch))
        
        self.suspenderSketch=tuple(self.suspenderSketch)
     

class StructurePart(object):
    """Create 'Part' of the structure"""

    def __init__(self,modelSketch):
        self.modelSketch=modelSketch

    def CreatePart(self,part):
        """Create Part
        
        function summary

        Args:


        Returns:

        Raises:
        """

        #design pattern: builder
        self.__CreateTowerPart(part);
        self.__CreateStiffeningGirderPart();
        self.__CreateCablePart();
        self.__CreateSuspenderPart();

    def __CreateTowerPart(self,part):
        """Create Tower Part
        
        function summary

        Args:


        Returns:

        Raises:
        """

        towerPart1 = myModel.Part(name='towerPart1', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        towerPart1.BaseWire(sketch=self.modelSketch.towerSketch[0])

        towerPart2 = myModel.Part(name='towerPart2', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        towerPart2.BaseWire(sketch=self.modelSketch.towerSketch[1])

        self.towerPart=(towerPart1,towerPart2)

    def __CreateStiffeningGirderPart(self):
        """Create Tower Part
        
        function summary

        Args:


        Returns:

        Raises:
        """ 
        stiffeningGirderPart = myModel.Part(name='beamPart', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        stiffeningGirderPart.BaseWire(sketch=self.modelSketch.stiffeningGirderSketch)
        self.stiffeningGirderPart=stiffeningGirderPart

        self.girderRigidarmPart=[]
        for i in range(len(self.modelSketch.girderRigidarmSketch)):
            girderRigidarmPart = myModel.Part(name='girderRigidarmPart'+str(i+1), dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
            girderRigidarmPart.BaseWire(sketch=self.modelSketch.girderRigidarmSketch[i])
            self.girderRigidarmPart.append(girderRigidarmPart)
        
        self.girderRigidarmPart=tuple(self.girderRigidarmPart)
 
        
    def __CreateCablePart(self):
        """Create Cable Part
        
        function summary

        Args:


        Returns:

        Raises:
        """

        cablePart1 = myModel.Part(name='cablePart1', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        cablePart1.BaseWire(sketch=self.modelSketch.cableSketch[0])

        cablePart2 = myModel.Part(name='cablePart2', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        cablePart2.BaseWire(sketch=self.modelSketch.cableSketch[1])

        self.cablePart=(cablePart1,cablePart2)

    def __CreateSuspenderPart(self):
        """Create Suspender Part
        
        function summary

        Args:


        Returns:

        Raises:
        """
        self.suspenderPart=[]
        for i in range(len(self.modelSketch.suspenderSketch)):
            suspenderPart=[]
            for j in range(len(self.modelSketch.suspenderSketch[0])):
                sP = myModel.Part(name='suspenderPart'+str(i+1)+'-'+str(j+1), dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
                sP.BaseWire(sketch=self.modelSketch.suspenderSketch[i][j])
                suspenderPart.append(sP)
            self.suspenderPart.append(tuple(suspenderPart))
        
        self.suspenderPart=tuple(self.suspenderPart)



class StructureAssembly(object):
    """Create 'Assembly' of the structure"""

    def __init__(self,modelPart):
        self.modelPart=modelPart

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

        p = myModel.parts['towerPart1']  
        myAssembly.Instance(name='towerInstance1', part=p, dependent=ON)
        p = myModel.parts['towerPart2']
        myAssembly.Instance(name='towerInstance2', part=p, dependent=ON)

        p = myModel.parts['beamPart']
        myAssembly.Instance(name='beamInstance', part=p, dependent=ON)

        for i in range(len(self.modelPart.girderRigidarmPart)):       
            p = myModel.parts['girderRigidarmPart'+str(i+1)]
            myAssembly.Instance(name='girderRigidarmInstance'+str(i+1), part=p, dependent=ON)

        p = myModel.parts['cablePart1']
        myAssembly.Instance(name='cableInstance1', part=p, dependent=ON)
        p = myModel.parts['cablePart2']
        myAssembly.Instance(name='cableInstance2', part=p, dependent=ON)


        for i in range(len(self.modelPart.suspenderPart)):
            for j in range(len(self.modelPart.suspenderPart[0])):
                p = myModel.parts['suspenderPart'+str(i+1)+'-'+str(j+1)]
                myAssembly.Instance(name='suspenderInstance'+str(i+1)+'-'+str(j+1), part=p, dependent=ON)

    def __MoveInstance(self,structureGeometry):
        """Move Instance: Translate and rotate Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        self.__moveTowerInstance()
        self.__moveStiffeningGirderInstance()
        self.__moveGirderRigidarmInstance(structureGeometry)
        self.__moveCableInstance()
        self.__moveSuspenderInstance(structureGeometry)

    def __MergeInstance(self):
        """Merge Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        pass

    def __moveTowerInstance(self):
        myAssembly.translate(instanceList=('towerInstance1', ), vector=(0.0, 0.0, -3.75))
        myAssembly.rotate(instanceList=('towerInstance1', ), axisPoint=(25.0, (3.3+20.44)/2, -3.75), 
            axisDirection=(0.0, 8.57, 0.0), angle=-90.0)

        myAssembly.translate(instanceList=('towerInstance2', ), vector=(0.0, 0.0, -3.75))
        myAssembly.rotate(instanceList=('towerInstance2', ), axisPoint=(95.0, (3.3+20.44)/2, -3.75), 
            axisDirection=(0.0, 8.57, 0.0), angle=-90.0)
    
    def __moveStiffeningGirderInstance(self):
        pass

    def __moveGirderRigidarmInstance(self,structureGeometry):
        rGR=structureGeometry.rGirderRigidarmCoordinate

        for i in range(len(self.modelPart.girderRigidarmPart)): 
            myAssembly.rotate(instanceList=('girderRigidarmInstance'+str(i+1), ), axisPoint=rGR[i],
                axisDirection=(0, 1, 0), angle=90.0)

    def __moveCableInstance(self):
        myAssembly.translate(instanceList=('cableInstance1', ), vector=(0.0, 0.0, -3.75))
        myAssembly.translate(instanceList=('cableInstance2', ), vector=(0.0, 0.0, 3.75))

    def __moveSuspenderInstance(self,structureGeometry):
        """move Suspender Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        for i in range(len(self.modelPart.suspenderPart)):
            for j in range(len(self.modelPart.suspenderPart[0])):
                myAssembly.translate(instanceList=('suspenderInstance'+str(i+1)+'-'+str(j+1), ), vector=(0.0, 0.0, structureGeometry.rRigidarmSuspenderCoordinate[i][0][2]))

class StructureRegion(object):
    """store abaqus region of the structure"""

    def __init__(self):
        pass

    def CreateRegion(self):
        pass

class StructureInteraction(object):
    """Create 'Interaction' of the structure"""

    def __init__(self):
        pass


class StructureProperty(object):
    """Properties of the structure, including material, profile, section"""

    def __init__(self):
        pass

    def CreateProperty(self):
        """set the material, profile and section property

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        self.__CreateMaterial()
        self.__CreateProfile()
        self.__CreateSection()
    
    def __CreateMaterial(self):
        """create the material

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        #global myModel

        #must operate manual at the time being

        #cable Material
        cableMaterial=myModel.Material(name='cableMaterial')
        cableMaterial.Density(table=((8518.367347, ), ))    #density     
        cableMaterial.Elastic(table=((2.00E+11, 0.3), ))    #Young's module, possion ratio
        self.cableMaterial=cableMaterial

        #suspender Material
        suspenderMaterial=myModel.Material(name='suspenderMaterial')
        suspenderMaterial.Density(table=((9050, ), ))    #density     
        suspenderMaterial.Elastic(table=((2.00E+11, 0.3), ))    #Young's module, possion ratio
        self.suspenderMaterial=suspenderMaterial

        #C50 Material
        C50Material=myModel.Material(name='C50Material')
        C50Material.Density(table=((2549, ), ))    #density     
        C50Material.Elastic(table=((3.45E+10, 0.2), ))    #Young's module, possion ratio
        self.C50Material=C50Material


    def __CreateProfile(self):
        """create the profile

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        #Tower profile
        downTowerProfile=myModel.RectangularProfile(name='downTowerProfile', a=1.3, b=1.6)  #bottom:a height:b

        upTowerProfile=myModel.RectangularProfile(name='upTowerProfile', a=0.9, b=1.4)



        #girder profile
        A_AProfile=myModel.GeneralizedProfile(name='A-AProfile', area=3.24, i11=1.54E-01, i12=0, i22=2.17E+01, j=2.64E-01, gammaO=0.0, gammaW=0.0) 

        C_CProfile=myModel.GeneralizedProfile(name='C-CProfile', area=5.74, i11=3.11E-01, i12=0, i22=2.55E+01, j=1.07834, gammaO=0.0, gammaW=0.0)

        E_EProfile=myModel.GeneralizedProfile(name='E-EProfile', area=1.82E+01, i11=6.07E+00, i12=0, i22=1.26E+02, j=2.14E+01, gammaO=0.0, gammaW=0.0)


        F_FProfile=myModel.GeneralizedProfile(name='F-FProfile', area=1.24E+01, i11=1.94E+00, i12=0, i22=8.58E+01, j=7.24E+00, gammaO=0.0, gammaW=0.0)


        
        #cable profile
        #The CircularProfile object is derived from the Profile object
        cableProfile=myModel.CircularProfile(name='cableProfile', r=0.10695)

        #suspender profile
        suspenderProfile=myModel.CircularProfile(name='suspenderProfile', r=0.031022)	

    def __CreateSection(self):
        """create the section

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """ 

        #tower section
        downTowerSection=myModel.BeamSection(name='downTowerSection', 
              integration=BEFORE_ANALYSIS, profile='downTowerProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        upTowerSection=myModel.BeamSection(name='upTowerSection', 
              integration=BEFORE_ANALYSIS, profile='upTowerProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        #girder section
        A_ASection=myModel.BeamSection(name='A-ASection', 
              integration=BEFORE_ANALYSIS, profile='A-AProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        C_CSection=myModel.BeamSection(name='C-CSection', 
              integration=BEFORE_ANALYSIS, profile='A-AProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        E_ESection=myModel.BeamSection(name='E-ESection', 
              integration=BEFORE_ANALYSIS, profile='A-AProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        F_FSection=myModel.BeamSection(name='F-FSection', 
              integration=BEFORE_ANALYSIS, profile='A-AProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False) 
 
        #cable section
        A=3.14159*myModel.profiles['cableProfile'].r**2
        cableSection=myModel.TrussSection(name='cableSection', material='cableMaterial', 
            area=A)

        #suspender section
        A=3.14159*myModel.profiles['suspenderProfile'].r**2
        suspenderProfile=myModel.CircularProfile(name='suspenderSection', r=0.031022)
        suspenderSection=myModel.TrussSection(name='suspenderSection', material='suspenderMaterial', 
            area=A)	
       
    def SectionAssignment(self):
        """assign the truss and beam section

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """     
        pass   

    def AssignBeamSectionOrientation(self):
        """assign the truss and beam section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """     
        pass

class StructureStep(object):
    """define the step"""

     

    def __init__(self):
        pass

    def CreateStep(self):
        """abaqus:
            Create a step. The time period of the static step is 1.0, 
            and the initial incrementation is 0.1; the step is created
            after the initial step. 
        """ 
        myModel.StaticStep(name='beamStep', previous='Initial',
            nlgeom=OFF)
    
        myModel.FieldOutputRequest(name='F-Output-2', 
            createStepName='beamStep', variables=('SF',))       
    

class StructureLoad(object):
    """define the load of the structure"""

    def __init__(self):
        pass

    def CreateDisplacementBC():
        """create the displacement of the structure

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

class StructureMesh(object):
    """mesh the structrue"""

    def __init__(self):
        pass

    def CreateMesh(self):
        self.__MeshTower()
        self.__MeshGirder()
        self.__MeshCable()
        self.__MeshSuspender()

    def __MeshTower(self):
        pass

    def __MeshGirder(self):
        pass

    def __MeshCable(self):
        pass

    def __MeshSuspender(self):
        pass    
         
       
#start the program
session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

#-----------------------------------------------------

# Create a model

modelName='GuoxiSuspensionBridge'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------

# Create geometry
bg=StructureGeometry()

#-----------------------------------------------------

# Create a sketch
bs=StructureSketch()
bs.CreateSketch(bg)

#-----------------------------------------------------

#Create parts
import part
bp=StructurePart(bs)
bp.CreatePart(part)

#-----------------------------------------------------

#Create assembly
import assembly
from abaqusConstants import *
myAssembly=myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

ba=StructureAssembly(bp)
ba.CreateAssembly(bg)

bPro=StructureProperty()
bPro.CreateProperty()