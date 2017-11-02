# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan

class BridgeGeometry(object):
    """store the bridge geometry information of the suspension bridge"""
    
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
        pass    

class BridgeSketch(object):
    """Create 'Sketch' of the suspension bridge"""

    
    def __init__(self):
        pass
    def CreateSketch(self,bridegeGeometry):
        """Create Sketch
        
        function summary

        Args:
            bridegeGeometry: BridgeGeometry instance

        Returns:

        Raises:
        """

        #design pattern: builder
        self.__CreateTowerSketch(bridegeGeometry)
        self.__CreateStiffeningGirderSketch(bridegeGeometry)
        self.__CreateGirderRigidarmSketch(bridegeGeometry)
        self.__CreateCableSketch()
        self.__CreateSuspenderSketch(bridegeGeometry);

    def __CreateTowerSketch(self,bridegeGeometry):
        """CreateTowerSketch
        
        function summary

        Args:

        Returns:

        Raises:
        """
        
        #global myModel

        #Tower:

        dTB=bridegeGeometry.downTowerBottomCoordinate
        rUD=bridegeGeometry.rUpDownTowerCoordinate
        uTT=bridegeGeometry.upTowerTopCoordinate

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

    def __CreateStiffeningGirderSketch(self,bridegeGeometry):
        """Create Stiffening Girder Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """    
        eP=bridegeGeometry.EndPointCoordinate
        rGR=bridegeGeometry.rGirderRigidarmCoordinate
        rRS=bridegeGeometry.rRigidarmSuspenderCoordinate

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
      

    
    def __CreateGirderRigidarmSketch(self,bridegeGeometry):
        """Create Girder Rigidarm Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """    
        rGR=bridegeGeometry.rGirderRigidarmCoordinate
        rRS=bridegeGeometry.rRigidarmSuspenderCoordinate

        #create GirderRigidarm Sketch
        girderRigidarmSketch=[]
        for i in range(len(rGR)):
            mySketch = myModel.ConstrainedSketch(name='girderRigidarmSketch'+str(i+1),sheetSize=10.0)
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
        
        #global myModel

        cableCoordinate=(((-1.45,6.473),(10,11.270569),(15,13.906819),(20,16.903937),(25,20.44),
            (30,17.92136),(35,15.940382),(40,14.319928),(45,13.059819),(50,12.159874),
            (55,11.619961),(60,11.44),(65,11.619961),(70,12.159874),(75,13.059819),
            (80,14.319928),(85,15.940382),(90,17.92136),(95,20.44),(100,16.903937),
            (105,13.906819),(110,11.270569),(121.45,6.473)),

            ((-1.45,6.473),(10,11.270569),(15,13.906819),(20,16.903937),(25,20.44),
            (30,17.92136),(35,15.940382),(40,14.319928),(45,13.059819),(50,12.159874),
            (55,11.619961),(60,11.44),(65,11.619961),(70,12.159874),(75,13.059819),
            (80,14.319928),(85,15.940382),(90,17.92136),(95,20.44),(100,16.903937),
            (105,13.906819),(110,11.270569),(121.45,6.473)))
        
        self.cableCoordinate=cableCoordinate

        mySketch = myModel.ConstrainedSketch(name='cableSketch1',sheetSize=10.0)

        for i in range(len(cableCoordinate[0])-1):
            mySketch.Line(point1=cableCoordinate[0][i], point2=cableCoordinate[0][i+1])

        cableSketch1=mySketch

        mySketch = myModel.ConstrainedSketch(name='cableSketch2',sheetSize=10.0)

        for i in range(len(cableCoordinate[1])-1):
            mySketch.Line(point1=cableCoordinate[1][i], point2=cableCoordinate[1][i+1])

        cableSketch2=mySketch

        self.cableSketch=(cableSketch1,cableSketch2)

    def __CreateSuspenderSketch(self,bridegeGeometry):
        """Create Suspender Sketch
        
        function summary

        Args:

        Returns:

        Raises:
        """
        
        hP=bridegeGeometry.hangingPointCoordinate
        rRS=bridegeGeometry.rRigidarmSuspenderCoordinate             

        self.suspenderSketch=[]
        suspenderSketch=[]
        for i in range(len(rRS)):
            for j in range(len(rRS[0])):
                mySketch = myModel.ConstrainedSketch(name='girderRigidarmSketch'+str(i+1)+'-'+str(j+1),sheetSize=10.0)
                mySketch.Line(point1=(hP[i][j][0],hP[i][j][1]), point2=(rRS[i][j][0],rRS[i][j][1]))
                suspenderSketch.append(mySketch)   
            self.suspenderSketch.append(tuple(suspenderSketch))
        
        self.suspenderSketch=tuple(self.suspenderSketch)
     

class BridgePart(object):
    """Create 'Part' of the suspension bridge"""

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



class BridgeAssembly(object):
    """Create 'Assembly' of the suspension bridge"""

    def __init__(self,modelPart):
        self.modelPart=modelPart

    def CreateAssembly(self,bridegeGeometry):
        """Create Assembly
        
        function summary

        Args:


        Returns:

        Raises:
        """
        self.__CreateInstance()
        self.__MoveInstance(bridegeGeometry)
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

    def __MoveInstance(self,bridegeGeometry):
        """Move Instance: Translate and rotate Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        self.__moveTowerInstance()
        self.__moveStiffeningGirderInstance()
        self.__moveGirderRigidarmInstance(bridegeGeometry)
        self.__moveCableInstance()
        self.__moveSuspenderInstance(bridegeGeometry)

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

    def __moveGirderRigidarmInstance(self,bridegeGeometry):
        rGR=bridegeGeometry.rGirderRigidarmCoordinate

        for i in range(len(self.modelPart.girderRigidarmPart)): 
            myAssembly.rotate(instanceList=('girderRigidarmInstance'+str(i+1), ), axisPoint=rGR[i],
                axisDirection=(0, 1, 0), angle=90.0)

    def __moveCableInstance(self):
        myAssembly.translate(instanceList=('cableInstance1', ), vector=(0.0, 0.0, -3.75))
        myAssembly.translate(instanceList=('cableInstance2', ), vector=(0.0, 0.0, 3.75))

    def __moveSuspenderInstance(self,bridegeGeometry):
        """move Suspender Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        for i in range(len(self.modelPart.suspenderPart)):
            for j in range(len(self.modelPart.suspenderPart[0])):
                myAssembly.translate(instanceList=('suspenderInstance'+str(i+1)+'-'+str(j+1), ), vector=(0.0, 0.0, bridegeGeometry.rRigidarmSuspenderCoordinate[i][0][2]))

class Property(object):
    """Properties of the suspension bridge, including material, profile, section"""

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
        pass
    
    def CreateMaterial(self):
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
        myModel.Material(name='Material-2')
        myModel.materials['Material-2'].Density(table=((7800.0, ), ))
        myModel.materials['Material-2'].Elastic(table=((2500.0, 0.3), ))

    def CreateProfile(self):
        """create the profile

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        myModel.GeneralizedProfile(name='GProfile', area=1000000.0, i11=1.0, i12=0, i22=1.0, j=1.0, gammaO=0.0, gammaW=0.0) 

    def CreateSection(self):
        """create the section

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        trussArea=1.0

        myModel.TrussSection(name='trussSection', material='trussMaterial', 
            area=trussArea)

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

class BridgeStep(object):
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
    

class BridgeLoad(object):
    """define the load of the structure"""

    def __init__(self):
        pass

    def CreateDisplacementBC():
        """create the bridge displacement

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

class BridgeMesh(object):
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
bg=BridgeGeometry()

#-----------------------------------------------------

# Create a sketch
bs=BridgeSketch()
bs.CreateSketch(bg)

#-----------------------------------------------------

#Create parts
import part
bp=BridgePart(bs)
bp.CreatePart(part)

#-----------------------------------------------------

#Create assembly
import assembly
from abaqusConstants import *
myAssembly=myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

ba=BridgeAssembly(bp)
ba.CreateAssembly(bg)