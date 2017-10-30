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
    EndPointCoordinate=((-3.6,0.0,7.355),(123.6,0.0,7.355))    #west & east end point
    rGirderDiaphragmCoordinate=((10,8.13,0),(15,8.3675,0),(20,8.58,0),
        (25,8.7675,0),(30,8.93,0),(35,9.0675,0),(40,9.18,0),(45,9.2675,0),(50,9.33,0),(55,9.3675,0),
        (60,9.38,0),
        (65,9.3675,0),(70,9.33,0),(75,9.2675,0),(80,9.18,0),(85,9.0675,0),(90,8.93,0),(95,8.7675,0),
        (100,8.58,0),(105,8.3675,0),(110,8.13,0))
    
    rGirderSuspenderCoordinate=(((10,7.73,-3.75),(15,7.9675,-3.75),(20,8.18,-3.75),
        (30,8.53,-3.75),(35,8.6675,-3.75),(40,8.78,-3.75),(45,8.8675,-3.75),(50,8.93,-3.75),(55,8.9675,-3.75),
        (60,8.98,-3.75),
        (65,8.9675,-3.75),(70,8.93,-3.75),(75,8.8675,-3.75),(80,8.78,-3.75),(85,8.6675,-3.75),(90,8.53,-3.75),
        (100,8.18,-3.75),(105,7.9675,-3.75),(110,7.73,-3.75)),

        ((10,7.73,3.75),(15,7.9675,3.75),(20,8.18,3.75),
        (30,8.53,3.75),(35,8.6675,3.75),(40,8.78,3.75),(45,8.8675,3.75),(50,8.93,3.75),(55,8.9675,3.75),
        (60,8.98,3.75),
        (65,8.9675,3.75),(70,8.93,3.75),(75,8.8675,3.75),(80,8.78,3.75),(85,8.6675,3.75),(90,8.53,3.75),
        (100,8.18,3.75),(105,7.9675,3.75),(110,7.73,3.75)))

    rGirderCableCoordinate
    rGirderSuspenderCoordinate
    
    #cable
    anchorPointCoordinate=(((1.45,6.473,-3.75),(121.45,6.473,-3.75)),   #northern 1#  
                            ((1.45,6.473,3.75),(121.45,6.473,3.75)))    #southern 2#
  
    hangedPointCoordinate=(((10,11.270569,-3.75),(15,13.906819,-3.75),(20,16.903937,-3.75),
        (30,17.92136,-3.75),(35,15.940382,-3.75),(40,14.319928,-3.75),(45,13.059819,-3.75),(50,12.159874,-3.75),(55,11.619961,-3.75),
        (60,11.44,-3.75),
        (80,14.319928,-3.75),(85,15.940382,-3.75),(90,17.92136,-3.75),(65,11.619961,-3.75),(70,12.159874,-3.75),(75,13.059819,-3.75),
        (100,16.903937,-3.75),(105,13.906819,-3.75),(110,11.270569,-3.75)), 
        
        ((10,11.270569,3.75),(15,13.906819,3.75),(20,16.903937,3.75),
        (30,17.92136,3.75),(35,15.940382,3.75),(40,14.319928,3.75),(45,13.059819,3.75),(50,12.159874,3.75),(55,11.619961,3.75),
        (60,11.44,3.75),
        (80,14.319928,3.75),(85,15.940382,3.75),(90,17.92136,3.75),(65,11.619961,3.75),(70,12.159874,3.75),(75,13.059819,3.75),
        (100,16.903937,3.75),(105,13.906819,3.75),(110,11.270569,3.75))) 


    #suspender

    def __init__(self):
        pass    

class BridgeSketch(object):
    """Create 'Sketch' of the suspension bridge"""


    def __init__(self):
        pass
    def CreateSketch(self):
        """Create Sketch
        
        function summary

        Args:
            myModel: mdb model
            part: import part

        Returns:

        Raises:
        """

        #design pattern: builder
        self.__CreateTowerSketch();
        self.__CreateStiffeningGirderSketch();
        self.__CreateCableSketch();
        self.__CreateSuspenderSketch();

    def __CreateTowerSketch(self):
        """CreateTowerSketch
        
        function summary

        Args:

        Returns:

        Raises:
        """
        
        #global myModel

        towerCoordinate=(((25,3.3),(25,20.44),(25+7.5,20.44),(25+7.5,3.3)),
                        ((95,3.3),(95,20.44),(95+7.5,20.44),(95+7.5,3.3)))

        mySketch = myModel.ConstrainedSketch(name='towerSketch1',sheetSize=10.0)
        mySketch.Line(point1=towerCoordinate[0][0], point2=towerCoordinate[0][1])
        mySketch.Line(point1=towerCoordinate[0][1], point2=towerCoordinate[0][2])
        mySketch.Line(point1=towerCoordinate[0][2], point2=towerCoordinate[0][3])
        towerSketch1=mySketch


        mySketch = myModel.ConstrainedSketch(name='towerSketch2',sheetSize=10.0)
        mySketch.Line(point1=towerCoordinate[1][0], point2=towerCoordinate[1][1])
        mySketch.Line(point1=towerCoordinate[1][1], point2=towerCoordinate[1][2])
        mySketch.Line(point1=towerCoordinate[1][2], point2=towerCoordinate[1][3])
        towerSketch2=mySketch

        self.towerSketch=(towerSketch1,towerSketch2)

    def __CreateStiffeningGirderSketch(self):
  
        stiffeningGirderCoordinate=((-3.6,7.355),(-1.454187,7.489113),(0,7.58),(10,8.13),(15,8.3675),
            (20,8.58),(25,8.7675),(30,8.93),(35,9.0675),(40,9.18),(45,9.2675),(50,9.33),(55,9.3675),(60,9.38),
            (65,9.3675),(70,9.33),(75,9.2675),(80,9.18),(85,9.0675),(90,8.93),(95,8.7675),(100,8.58),(105,8.3675),
            (110,8.13),(120,7.58),(121.454187,7.489113),(123.6,7.355))
        
        mySketch = myModel.ConstrainedSketch(name='stiffeningGirderSketch',sheetSize=10.0)

        for i in range(len(stiffeningGirderCoordinate)-1):
            mySketch.Line(point1=stiffeningGirderCoordinate[i], point2=stiffeningGirderCoordinate[i+1])
        
        self.stiffeningGirderSketch=mySketch

    def __CreateCableSketch(self):
        """CreateTowerSketch
        
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

    def __CreateSuspenderSketch(self):
        """CreateTowerSketch
        
        function summary

        Args:

        Returns:

        Raises:
        """


        pass    

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
        pass

class BridgeAssembly(object):
    """Create 'Assembly' of the suspension bridge"""

    def __init__(self):
        pass

    def CreateAssembly(self):
        """Create Assembly
        
        function summary

        Args:


        Returns:

        Raises:
        """
        self.__CreateInstance()
        self.__MoveInstance()
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

        p = myModel.parts['cablePart1']
        myAssembly.Instance(name='cableInstance1', part=p, dependent=ON)
        p = myModel.parts['cablePart2']
        myAssembly.Instance(name='cableInstance2', part=p, dependent=ON)

    def __MoveInstance(self):
        """Move Instance: Translate and rotate Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        self.__moveTowerInstance()
        self.__moveStiffeningGirderInstance()
        self.__moveCableInstance()
        self.__moveSuspenderInstance()

    def __MergeInstance(self):
        """Merge Instance
        
        function summary

        Args:

        Returns:

        Raises:
        """
        pass

    def __moveTowerInstance(self):
        myAssembly.translate(instanceList=('towerInstance1', ), vector=(0.0, 0.0, -3.5))
        myAssembly.rotate(instanceList=('towerInstance1', ), axisPoint=(25.0, (3.3+20.44)/2, -3.5), 
            axisDirection=(0.0, 8.57, 0.0), angle=-90.0)

        myAssembly.translate(instanceList=('towerInstance2', ), vector=(0.0, 0.0, 3.5))
        myAssembly.rotate(instanceList=('towerInstance2', ), axisPoint=(95.0, (3.3+20.44)/2, -3.5), 
            axisDirection=(0.0, 8.57, 0.0), angle=-90.0)
    
    def __moveStiffeningGirderInstance(self):
        pass
    def __moveCableInstance(self):
        myAssembly.translate(instanceList=('cableInstance1', ), vector=(0.0, 0.0, -3.5))
        myAssembly.translate(instanceList=('cableInstance2', ), vector=(0.0, 0.0, 3.5))
    def __moveSuspenderInstance(self):
        pass

#start the program
session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

#-----------------------------------------------------

# Create a model

modelName='GuoxiSuspensionBridge'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------


# Create a sketch
bs=BridgeSketch()
bs.CreateSketch()

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

ba=BridgeAssembly()
ba.CreateAssembly()