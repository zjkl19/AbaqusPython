# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan


from interaction import *
from optimization import *
from sketch import *
from visualization import *
from connectorBehavior import *

import regionToolset

session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

#-----------------------------------------------------

# Create a model.

modelName='GuoxiSuspensionBridge'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.
	
mySketch = myModel.ConstrainedSketch(name='trussSketch1',sheetSize=10.0)

mySketch.Line(point1=(-1, 1), point2=(0, 0.0))
	
# Create a three-dimensional, deformable part.

trussPart1 = myModel.Part(name='trussPart1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	
# Create the part's base feature
trussPart1.BaseWire(sketch=mySketch)

#---
mySketch = myModel.ConstrainedSketch(name='trussSketch2',sheetSize=10.0)
mySketch.Line(point1=(1, 1), point2=(0, 0.0))
trussPart2 = myModel.Part(name='trussPart2', dimensionality=THREE_D, type=DEFORMABLE_BODY)
trussPart2.BaseWire(sketch=mySketch)
#---
mySketch = myModel.ConstrainedSketch(name='beamSketch',sheetSize=10.0)
mySketch.Line(point1=(-1, 0), point2=(1, 0))
beamPart = myModel.Part(name='beamPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)
beamPart.BaseWire(sketch=mySketch)
#-----------------------------------------------------

from material import *

Ematerial=1.0  #Young's module
pmaterial=0.3   #possion ratio
trussMaterial=myModel.Material(name='trussMaterial')
trussMaterial.Elastic(table=((Ematerial, pmaterial), ))

#-------------------------------------------------------

from section import *

# Create the truss section.

trussArea=1.0

myTrussSection=myModel.TrussSection(name='trussSection', material='trussMaterial', 
    area=trussArea)

#-----------

# Create the beam section.
myModel.GeneralizedProfile(name='GProfile', area=1000000.0, i11=1.0, i12=0, i22=1.0, j=1.0, gammaO=0.0, gammaW=0.0) 

Emat=1.0
Gmat=1.0

mySection=myModel.BeamSection(name='beamSection', profile='GProfile',
    poissonRatio=0.28, integration=BEFORE_ANALYSIS,
	table=((Emat, Gmat), ), alphaDamping=0.0, beamShape=CONSTANT,
    betaDamping=0.0, centroid=(0.0, 0.0), compositeDamping=0.0,
	consistentMassMatrix=False, dependencies=0, shearCenter=(0.0, 0.0),
	temperatureDependency=OFF, thermalExpansion=OFF)


#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

trussInstance1 = myAssembly.Instance(name='trussInstance1',
    part=trussPart1, dependent=ON)

trussInstance2 = myAssembly.Instance(name='trussInstance2',
    part=trussPart2, dependent=ON)

beamInstance1 = myAssembly.Instance(name='beamInstance1',
    part=beamPart, dependent=ON)

#combination
myAssembly.InstanceFromBooleanMerge(name='Part', instances=(
    trussInstance1, trussInstance2, 
    beamInstance1, ), originalInstances=SUPPRESS, 
    domain=GEOMETRY)

#-------------------------------------------------------

###
myPart = myModel.parts['Part']

edges = myPart.edges.findAt(((-0.75, 0.75, 0.0), ))
region = myPart.Set(edges=edges,name='set-1')
myPart.SectionAssignment(region=region, sectionName='trussSection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

myPart.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
    -1.0))
###

###
edges = myPart.edges.findAt(((0.75, 0.75, 0.0), ))
region = myPart.Set(edges=edges,name='set-2')
myPart.SectionAssignment(region=region, sectionName='trussSection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

myPart.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
    -1.0))
###

###
edges = myPart.edges.findAt(((-0.75, 0.0, 0.0), ), ((0.25, 0.0, 0.0), ))    #add two edges
region=myPart.Set(edges=edges,name='set-3')
myPart.SectionAssignment(region=region, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)

myPart.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
    -1.0))
###

from step import *

# Create a step. The time period of the static step is 1.0, 
# and the initial incrementation is 0.1; the step is created
# after the initial step. 

myModel.StaticStep(name='beamStep', previous='Initial',
    nlgeom=OFF)
    
myModel.FieldOutputRequest(name='F-Output-2', 
    createStepName='beamStep', variables=('SF',))

#-------------------------------------------------------

from load import *

PartInstance=myAssembly.instances['Part-1']

v=PartInstance.vertices
verts=v.findAt(((-1.0, 1.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')
region=myAssembly.sets['Set-fix1']
myModel.DisplacementBC(name='BC-1', createStepName='Initial',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)


verts=v.findAt(((1.0, 1.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix2')
region=myAssembly.sets['Set-fix2']
myModel.DisplacementBC(name='BC-2', createStepName='Initial',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

verts=v.findAt(((-1.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix3')
region=myAssembly.sets['Set-fix3']
myModel.DisplacementBC(name='BC-3', createStepName='Initial',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

verts=v.findAt(((1.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix4')
region=myAssembly.sets['Set-fix4']
myModel.DisplacementBC(name='BC-4', createStepName='Initial',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

###
e1 = PartInstance.edges
edges1 = e1.findAt(((-0.75, 0.0, 0.0), ), ((0.25, 0.0, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.LineLoad(name='Load-1', 
    createStepName='beamStep', region=region, comp2=-1.0)
###
#-------------------------------------------------------

from mesh import *

import mesh
	
Ediv=100   #the number of the Element division

# Seed the part instance.
myPart.seedPart(size=1/Ediv,
    deviationFactor=0.01, minSizeFactor=0.01)

#need:
#from abaqus import *
#from abaqusConstants import *

elemType1=mesh.ElemType(elemCode=T3D2)
elemType2=mesh.ElemType(elemCode=B32)

pR=(myPart.edges.findAt(((-0.75, 0.75, 0.0), )),)
myPart.setElementType(regions=pR, elemTypes=(elemType1,))

pR=(myPart.edges.findAt(((0.75, 0.75, 0.0), )),)
myPart.setElementType(regions=pR, elemTypes=(elemType1,))

pR=(myPart.edges.findAt(((-0.75, 0.0, 0.0), ), ((0.25, 0.0, 0.0), )),)
myPart.setElementType(regions=pR, elemTypes=(elemType2,))

myPart.generateMesh()

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='currJob'

myJob=mdb.Job(name=jobName, model=modelName)
	
myJob.submit(consistencyChecking=OFF)


# Save by ldn
