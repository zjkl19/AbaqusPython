# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan


class StructureInteraction(object):
    """Create 'Interaction' of the structure"""

    def __init__(self):
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

    def CreatePredefinedField():
        """create the predefined field of the structure

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
import StructureGeometry as SG
bridgeGeometry=SG.StructureGeometry()

#-----------------------------------------------------

# Create a sketch
import StructureSketch as SS
bridgeSketch=SS.StructureSketch(myModel,bridgeGeometry)
bridgeSketch.CreateSketch()

#-----------------------------------------------------

#Create parts
import part as abaqusPart
import StructurePart as SP
bridgePart=SP.StructurePart(myModel,bridgeSketch,abaqusPart)
bridgePart.CreatePart()

#-----------------------------------------------------

#Create assembly
import assembly
from abaqusConstants import *

import StructureAssembly as SA
myAssembly=myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)    #CARTESIAN: from abaqusConstants import *


bridgeAssembly=SA.StructureAssembly(myModel,bridgePart,myAssembly)
bridgeAssembly.CreateAssembly(bridgeGeometry)

#-----------------------------------------------------
#Create region set
import StructureRegionSet as SRS
bridgeRegionSet=SRS.StructureRegionSet(myModel,bridgeGeometry)
bridgeRegionSet.CreateRegionSet()

#-----------------------------------------------------
#Create property
import StructureProperty
bridgeProperty=StructureProperty.StructureProperty(myModel,bridgeRegionSet)
bridgeProperty.CreateProperty()

