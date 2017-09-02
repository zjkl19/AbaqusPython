# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#explanation:
#abstract:the usage of initial stress
#structure:truss with 3 bar
#load:initial Fn
#post:RF, u

#comment by lindinan in 20170902

from abaqus import *
from abaqusConstants import *
from caeModules import *

from interaction import *
from optimization import *
from sketch import *
from visualization import *
from connectorBehavior import *

import regionToolset

session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

l1=1.0	#the length of the truss in the bottom. unit:m

l2=1.0	#the length of the truss int the left. unit:m

l3= (l1**2+l2**2)**0.5	#the length of the slope truss. unit:m

modelName='TrussInitialStressModel'     #the name of the model

#-----------------------------------------------------

# Create a model.

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.

sketch1 = myModel.ConstrainedSketch(name='trussSketch1',sheetSize=10.0)

# Create the line.

sketch1.Line(point1=(0.0, 0.0), point2=(l1, 0.0))

# Create a three-dimensional, deformable part.

trussPart1 = myModel.Part(name='trussPart1', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create the part's base feature
trussPart1.BaseWire(sketch=sketch1)

sketch2 = myModel.ConstrainedSketch(name='trussSketch2',sheetSize=10.0)
sketch2.Line(point1=(0.0, 0.0), point2=(0.0, l2))
trussPart2 = myModel.Part(name='trussPart2', dimensionality=THREE_D, type=DEFORMABLE_BODY)
trussPart2.BaseWire(sketch=sketch2)

sketch3 = myModel.ConstrainedSketch(name='trussSketch3',sheetSize=10.0)
sketch3.Line(point1=(0.0, l2), point2=(l1, 0.0))
trussPart3 = myModel.Part(name='trussPart3', dimensionality=THREE_D, type=DEFORMABLE_BODY)
trussPart3.BaseWire(sketch=sketch3)
#-----------------------------------------------------

from material import *

# Create a material.


#It(umat) seems to be no use in the situation in the "integration=BEFORE_ANALYSIS"

#Ematerial=3.45e10   #Young's module
Ematerial=1.0   #Young's module
pmaterial=0.3   #possion ratio
myTrussMaterial=myModel.Material(name='trussMaterial')
myModel.materials['trussMaterial'].Elastic(table=((Ematerial, pmaterial), ))

#-------------------------------------------------------

from section import *
# Create the truss section.

trussArea=1.0

myTrussSection=myModel.TrussSection(name='trussSection', material='trussMaterial', 
    area=trussArea)
    

###
trussRegion=regionToolset.Region(edges=trussPart1.edges)

trussPart1.SectionAssignment(region=trussRegion, sectionName='trussSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
trussPart1.assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
    edges=trussPart1.edges.findAt(((0.0, 0.0, 0.0),
    ), ((l1, 0.0, 0.0), ), )))

###
trussRegion=regionToolset.Region(edges=trussPart2.edges)

trussPart2.SectionAssignment(region=trussRegion, sectionName='trussSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
trussPart2.assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
    edges=trussPart2.edges.findAt(((0.0, 0.0, 0.0),
    ), ((0.0, l2, 0.0), ), )))

###
trussRegion=regionToolset.Region(edges=trussPart3.edges)

trussPart3.SectionAssignment(region=trussRegion, sectionName='trussSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
trussPart3.assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
    edges=trussPart3.edges.findAt(((0.0, l1, 0.0),
    ), ((l2, 0.0, 0.0), ), )))
#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

trussInstance1 = myAssembly.Instance(name='trussInstance1',
    part=trussPart1, dependent=ON)

trussInstance2 = myAssembly.Instance(name='trussInstance2',
    part=trussPart2, dependent=ON)

trussInstance3 = myAssembly.Instance(name='trussInstance3',
    part=trussPart3, dependent=ON)

###    
myModel.ConnectorSection(name='ConnSect-1', 
    translationalType=JOIN)
    
v1 = myAssembly.instances['trussInstance1'].vertices
v2 = myAssembly.instances['trussInstance2'].vertices

wire = myAssembly.WirePolyLine(points=((v1.findAt(coordinates=(0.0, 0.0, 0.0)), 
    v2.findAt(coordinates=(0.0, 0.0, 0.0))), ), mergeType=IMPRINT, 
    meshable=False)
    
oldName = wire.name
myAssembly.features.changeKey(fromName=oldName, 
    toName='Wire-1')

e1 = myAssembly.edges
edges1 = e1.findAt(((0.0, 0.0, 0.0), ))
myAssembly.Set(edges=edges1, name='Wire-1-Set-1')
region = myAssembly.sets['Wire-1-Set-1']
csa = myAssembly.SectionAssignment(sectionName='ConnSect-1', region=region)

###
v1 = myAssembly.instances['trussInstance1'].vertices
v2 = myAssembly.instances['trussInstance3'].vertices

wire = myAssembly.WirePolyLine(points=((v1.findAt(coordinates=(l1, 0.0, 0.0)), 
    v2.findAt(coordinates=(l1, 0.0, 0.0))), ), mergeType=IMPRINT, 
    meshable=False)
    
oldName = wire.name
myAssembly.features.changeKey(fromName=oldName, 
    toName='Wire-2')

e1 = myAssembly.edges
edges1 = e1.findAt(((l1, 0.0, 0.0), ))
myAssembly.Set(edges=edges1, name='Wire-2-Set-1')
region = myAssembly.sets['Wire-2-Set-1']
csa = myAssembly.SectionAssignment(sectionName='ConnSect-1', region=region)

###
v1 = myAssembly.instances['trussInstance2'].vertices
v2 = myAssembly.instances['trussInstance3'].vertices

wire = myAssembly.WirePolyLine(points=((v1.findAt(coordinates=(0.0, l2, 0.0)), 
    v2.findAt(coordinates=(0.0, l2, 0.0))), ), mergeType=IMPRINT, 
    meshable=False)
    
oldName = wire.name
myAssembly.features.changeKey(fromName=oldName, 
    toName='Wire-3')

e1 = myAssembly.edges
edges1 = e1.findAt(((0.0, l2, 0.0), ))
myAssembly.Set(edges=edges1, name='Wire-3-Set-1')
region = myAssembly.sets['Wire-3-Set-1']
csa = myAssembly.SectionAssignment(sectionName='ConnSect-1', region=region)  


#-------------------------------------------------------

from step import *

# Create a step. The time period of the static step is 1.0, 
# and the initial incrementation is 0.1; the step is created
# after the initial step. 

myModel.StaticStep(name='InitialStep', previous='Initial',
    nlgeom=OFF, description='Load of the structure')

#-------------------------------------------------------

from load import *

v=trussInstance1.vertices
verts=v.findAt(((0.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')

region=myAssembly.sets['Set-fix1']

myModel.DisplacementBC(name='BC-1', createStepName='InitialStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

###
v=trussInstance1.vertices
verts=v.findAt(((l1, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix2')

region=myAssembly.sets['Set-fix2']

myModel.DisplacementBC(name='BC-2', createStepName='InitialStep',
    region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)



e1 = trussInstance2.edges
edges1 = e1.findAt(((0.0, l2/2, 0.0), ))
region = myAssembly.Set(edges=edges1, name='Set-2')
myModel.Stress(name='Predefined Field-1', 
    region=region, distributionType=UNIFORM, sigma11=1.0, sigma22=None, 
    sigma12=None, sigma33=None, sigma13=None, sigma23=None)
    
#-------------------------------------------------------

import mesh
	
# Assign an element type to the part instance.
#region = (myInstance.cells,)
#elemType = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
#myAssembly.setElementType(regions=region, elemTypes=(elemType,))


# Seed the part instance.
trussPart1.seedPart(size=l1/5,
    deviationFactor=0.1, minSizeFactor=0.1)
    
elemType=mesh.ElemType(elemCode=T3D2)

pR=(trussPart1.edges,)

trussPart1.setElementType(regions=pR, elemTypes=(elemType,))

#need:
#from abaqus import *
#from abaqusConstants import *

#elemType1=mesh.ElemType(elemCode=B31)

#pR=(trussPart1.edges,)

#trussPart1.setElementType(regions=pR, elemTypes=(elemType1,))

# Mesh the part instance.
trussPart1.generateMesh()

trussPart2.seedPart(size=l2/5,
    deviationFactor=0.1, minSizeFactor=0.1)
    
elemType=mesh.ElemType(elemCode=T3D2)

pR=(trussPart2.edges,)

trussPart2.setElementType(regions=pR, elemTypes=(elemType,))

# Mesh the part instance.
trussPart2.generateMesh()

trussPart3.seedPart(size=l3/5,
    deviationFactor=0.1, minSizeFactor=0.1)
    
elemType=mesh.ElemType(elemCode=T3D2)

pR=(trussPart3.edges,)

trussPart3.setElementType(regions=pR, elemTypes=(elemType,))

# Mesh the part instance.
trussPart3.generateMesh()

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='trussInitialStress'

myJob=mdb.Job(name=jobName, model=modelName)
	
myJob.submit(consistencyChecking=OFF)


#-----------------------------------

# Save by ldn
