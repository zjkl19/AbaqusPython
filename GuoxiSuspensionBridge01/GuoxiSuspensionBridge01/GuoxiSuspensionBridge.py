# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan

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

#-----------------------------------------------------
#Create interaction
import StructureInteraction
bridgeInteraction=StructureInteraction.StructureInteraction(myModel,bridgeGeometry,myAssembly,bridgeRegionSet)
bridgeInteraction.CreateInteraction()

#-----------------------------------------------------
#Create step
import StructureStep
bridgeStep=StructureStep.StructureStep(myModel)
bridgeStep.CreateStep()

#-----------------------------------------------------
#Create load
import StructureLoad
bridgeLoad=StructureLoad.StructureLoad(myModel,myAssembly,bridgeRegionSet)
bridgeLoad.CreateLoad()