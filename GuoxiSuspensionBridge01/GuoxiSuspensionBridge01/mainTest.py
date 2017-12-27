# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan

from abaqus import *
from abaqusConstants import *
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()        
       
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
bridgePart=SP.StructurePart(myModel,bridgeGeometry,bridgeSketch,abaqusPart)
bridgePart.CreatePart()

mdb.saveAs(pathName='mainTest.cae')
#-----------------------------------------------------


