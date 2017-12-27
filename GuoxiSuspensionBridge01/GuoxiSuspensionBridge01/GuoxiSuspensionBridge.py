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

'''
reference code:
import regionToolset
a = mdb.models['GuoxiSuspensionBridge'].rootAssembly
e1 = a.instances['PartAll-1'].edges
edges1 = e1.findAt(((113.4, 7.93625, 0.0), ), ((106.25, 8.308125, 0.0), ), ((
    101.25, 8.526875, 0.0), ), ((92.5, 8.8425, 0.0), ), ((86.25, 9.033125, 
    0.0), ), ((81.25, 9.151875, 0.0), ), ((76.25, 9.245625, 0.0), ), ((71.25, 
    9.314375, 0.0), ), ((66.25, 9.358125, 0.0), ), ((61.25, 9.376875, 0.0), ), 
    ((56.25, 9.370625, 0.0), ), ((51.25, 9.339375, 0.0), ), ((46.25, 9.283125, 
    0.0), ), ((41.25, 9.201875, 0.0), ), ((36.25, 9.095625, 0.0), ), ((31.25, 
    8.964375, 0.0), ), ((22.5, 8.6675, 0.0), ), ((16.25, 8.420625, 0.0), ), ((
    11.25, 8.189375, 0.0), ), ((-0.2, 7.54875, 0.0), ))
region = regionToolset.Region(edges=edges1)
mdb.models['GuoxiSuspensionBridge'].Gravity(name='Load-3', 
    createStepName='beamStep', comp2=-9.8, distributionType=UNIFORM, field='', 
    region=region)
'''
#-----------------------------------------------------
#Create mesh
import StructureMesh
bridgeMesh=StructureMesh.StructureMesh(structureModel=myModel,structureRegionSet=bridgeRegionSet,
    structureAssembly=myAssembly)
bridgeMesh.CreateMesh()

#-----------------------------------------------------
#job:

bridgeJob=mdb.Job(name='guoxiJob', model=modelName, description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)

bridgeJob.submit(consistencyChecking=OFF)

