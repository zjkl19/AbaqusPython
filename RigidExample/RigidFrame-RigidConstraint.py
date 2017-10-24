# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-


#summary:
#structure:frame
#load:ConcentratedForce in the edge
#post:RF,RM,U

#set Connector(BEAM) in the interaction point

#comment by lindinan

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

h=1.0    #height unit:m
l=1.0    #length unit:m

#-----------------------------------------------------

# Create a model.

modelName='RigidFrame-RigidConstraint'

myModel = mdb.Model(name=modelName)
cLoad=2    #only refers to scale; unit:m

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.

mySketch1 = myModel.ConstrainedSketch(name='columnSketch',sheetSize=10.0)

# Create the line.

mySketch1.Line(point1=(0.0, 0.0), point2=(0.0, h))

# Create a three-dimensional, deformable part.

columnPart = myModel.Part(name='columnPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create the part's base feature
columnPart.BaseWire(sketch=mySketch1)

mySketch2 = myModel.ConstrainedSketch(name='beamSketch',sheetSize=10.0)
mySketch2.Line(point1=(0.0, h), point2=(h, l))
beamPart = myModel.Part(name='beamPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)
beamPart.BaseWire(sketch=mySketch2)

#-----------------------------------------------------

from material import *

# Create a material.

myC50 = myModel.Material(name='Material-C50', description='Concrete C50')

# Create the elastic properties

#elasticProperties = (209.E9, 0.28)
#mySteel.Elastic(table=(elasticProperties, ) )

#It(umat) seems to be no use in the situation in the "integration=BEFORE_ANALYSIS"

myC50.Density(table=((2500.0, ), ))
myC50.Elastic(table=((34500000000.0, 0.2), ))	#3.45e10N/m^2

#-------------------------------------------------------

from section import *
# Create the beam section.



myModel.RectangularProfile(a=0.3, b=0.4, name='RectProfile')
    
myModel.BeamSection(name='RectSection', integration=BEFORE_ANALYSIS,
	poissonRatio=0.28, beamShape=CONSTANT, profile='RectProfile', thermalExpansion=OFF,
	temperatureDependency=OFF, dependencies=0, table=((2.10e11, 8.203e11), ),
	alphaDamping=0.0,betaDamping=0.0, compositeDamping=0.0, centroid=(0.0, 0.0), 
	shearCenter=(0.0, 0.0),	consistentMassMatrix=False)

###
columnRegion=regionToolset.Region(edges=columnPart.edges)

columnPart.SectionAssignment(region=columnRegion, sectionName='RectSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['columnPart'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=columnPart.edges.findAt(((0.0, 0.0, 0.0), 
    ), ((0.0, h, 0.0), ), )))
    
#------------------------------------------------------------------

beamRegion=regionToolset.Region(edges=beamPart.edges)

beamPart.SectionAssignment(region=beamRegion, sectionName='RectSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['beamPart'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=beamPart.edges.findAt(((0.0, h, 0.0), 
    ), ((l, h, 0.0), ), )))

#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

myColumnInstance = myAssembly.Instance(name='columnInstance',
    part=columnPart, dependent=ON)

myBeamInstance = myAssembly.Instance(name='beamInstance',
    part=beamPart, dependent=ON)


v1 = myColumnInstance.vertices
myAssembly.ReferencePoint(point=v1.findAt(coordinates=(0.0, h, 0.0)))    
    

e1 = myAssembly.instances['beamInstance'].edges
edges1 = e1.findAt(((l/4, l, 0.0), ))
region2=myAssembly.Set(edges=edges1, name='b_Set-1')


#r1=myAssembly.referencePoints
#refPoints1=(r1[6], )    #?

#refPoints1=myAssembly.referencePoints.findAt((0,h,0),)
r1=myAssembly.referencePoints
refPoints1=(r1.findAt((0,h,0),), )

region1=regionToolset.Region(referencePoints=refPoints1)
myModel.RigidBody(name='Constraint-1', 
    refPointRegion=region1, bodyRegion=region2)

#-------------------------------------------------------------
    
myModel.ConnectorSection(name='ConnSect-1', 
    assembledType=BEAM)
    
v1 = myColumnInstance.vertices
v2 = myBeamInstance.vertices

wire = myAssembly.WirePolyLine(points=((v1.findAt(coordinates=(0.0, h, 0.0)), 
    v2.findAt(coordinates=(0.0, h, 0.0))), ), meshable=False)
    
oldName = wire.name
myAssembly.features.changeKey(fromName=oldName, 
    toName='Wire-1')

e1 = myAssembly.edges
edges1 = e1.findAt(((0.0, h, 0.0), ))
myAssembly.Set(edges=edges1, name='Wire-1-Set-1')
region = myAssembly.sets['Wire-1-Set-1']
csa = myAssembly.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.

#-------------------------------------------------------

from step import *

# Create a step. The time period of the static step is 1.0, 
# and the initial incrementation is 0.1; the step is created
# after the initial step. 

myModel.StaticStep(name='LoadStep', previous='Initial',
    nlgeom=OFF, description='Initial load of the structure.')


#-------------------------------------------------------

from load import *

v=myColumnInstance.vertices
verts=v.findAt(((0.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')

region=myAssembly.sets['Set-fix1']

myModel.DisplacementBC(name='BC-1', createStepName='LoadStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)


v=myBeamInstance.vertices
verts=v.findAt(((l, h, 0.0), ),)
myAssembly.Set(vertices=verts, name='Set-force')

region=myAssembly.sets['Set-force']

myModel.ConcentratedForce(name='CLoad', createStepName='LoadStep',
    region=region, cf2=-1.0*cLoad, distributionType=UNIFORM, field='',
    localCsys=None)
    
#-------------------------------------------------------

from mesh import *

# Assign an element type to the part instance.
#region = (myInstance.cells,)
#elemType = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
#myAssembly.setElementType(regions=region, elemTypes=(elemType,))


# Seed the part instance.
columnPart.seedPart(size=h/5,
    deviationFactor=0.1, minSizeFactor=0.1)

#need:
#from abaqus import *
#from abaqusConstants import *


# Mesh the part instance.
columnPart.generateMesh()

beamPart.seedPart(size=l/5,
    deviationFactor=0.1, minSizeFactor=0.1)



# Mesh the part instance.
beamPart.generateMesh()

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName=modelName

myJob=mdb.Job(name=jobName, model=modelName)

myJob.submit(consistencyChecking=OFF)

#-----------------------------------

