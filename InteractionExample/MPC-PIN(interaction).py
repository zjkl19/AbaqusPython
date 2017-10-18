# -*- coding: mbcs -*-


from abaqus import *
from abaqusConstants import *

from interaction import *
from optimization import *
from sketch import *
from visualization import *
from connectorBehavior import *

import regionToolset

#session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

trussLength=1.0
beamLength=1.0
cLoad=1	#only refers to scale

#-----------------------------------------------------

# Create a model.

myModel = mdb.Model(name='InteractionTestModel')

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.
	
mySketch = myModel.ConstrainedSketch(name='trussSketch',sheetSize=trussLength*2)

# Create the line.

mySketch.Line(point1=(0.0, 0.0), point2=(trussLength, 0.0))
	
# Create a three-dimensional, deformable part.

myTrussPart = myModel.Part(name='trussPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	
# Create the part's base feature
myTrussPart.BaseWire(sketch=mySketch)

# Create a sketch for the base feature.
	
mySketch = myModel.ConstrainedSketch(name='beamSketch',sheetSize=beamLength*2)

# Create the line.

mySketch.Line(point1=(trussLength, 0.0), point2=(trussLength+beamLength, 0.0))
	
# Create a three-dimensional, deformable part.

myBeamPart = myModel.Part(name='beamPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	
# Create the part's base feature
myBeamPart.BaseWire(sketch=mySketch)

#-----------------------------------------------------

from material import *

# Create a material.

#mySteel = myModel.Material(name='Steel')

myTrussMaterial=myModel.Material(name='trussMaterial')
myModel.materials['trussMaterial'].Elastic(table=((1.0, 0.3), ))

# Create the elastic properties

#elasticProperties = (209.E9, 0.28)
#mySteel.Elastic(table=(elasticProperties, ) )


#-------------------------------------------------------

from section import *

myTrussSection=myModel.TrussSection(name='trussSection', material='trussMaterial', 
    area=1.0)

#a:bottom;b:height	
myModel.RectangularProfile(name='beamProfile', a=12.0, b=1.0)

myBeamSection=myModel.BeamSection(name='beamSection', profile='beamProfile',
    poissonRatio=0.28, integration=BEFORE_ANALYSIS,
	table=((1.0, 1.0), ), alphaDamping=0.0, beamShape=CONSTANT,
    betaDamping=0.0, centroid=(0.0, 0.0), compositeDamping=0.0,
	consistentMassMatrix=False, dependencies=0, shearCenter=(0.0, 0.0),
	temperatureDependency=OFF, thermalExpansion=OFF)
	
# Assign the section to the region. The region refers 
# to the single cell in this model.

trussRegion=regionToolset.Region(edges=myTrussPart.edges)

myTrussPart.SectionAssignment(region=trussRegion, sectionName='trussSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['trussPart'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=myTrussPart.edges.findAt(((trussLength/4, 0.0, 0.0),
    ), ((trussLength/2, 0.0, 0.0), ), )))

#beamRegion = (myBeamPart.cells,)
beamRegion=regionToolset.Region(edges=myBeamPart.edges)

myBeamPart.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['beamPart'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=myBeamPart.edges.findAt(((trussLength+beamLength/4, 0.0, 0.0), 
    ), ((trussLength+beamLength/2, 0.0, 0.0), ), )))

#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

myTrussInstance = myAssembly.Instance(name='trussInstance',
    part=myTrussPart, dependent=ON)

myBeamInstance = myAssembly.Instance(name='beamInstance',
    part=myBeamPart, dependent=ON)

# MPC constraint
v1 = myAssembly.instances['trussInstance'].vertices
verts1 = v1.findAt(((trussLength, 0.0, 0.0), ))
region1=regionToolset.Region(vertices=verts1)

v1 = myAssembly.instances['beamInstance'].vertices
verts1 = v1.findAt(((trussLength, 0.0, 0.0), ))
region2=regionToolset.Region(vertices=verts1)
myModel.MultipointConstraint(name='Constraint-1',
    controlPoint=region1, surface=region2, mpcType=PIN_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)
#-------------------------------------------------------

from step import *

# Create a step. The time period of the static step is 1.0, 
# and the initial incrementation is 0.1; the step is created
# after the initial step. 

myModel.StaticStep(name='structStep', previous='Initial',
    nlgeom=OFF, description='Load of the struct.')

#-------------------------------------------------------

from load import *


v=myAssembly.instances['trussInstance'].vertices
verts=v.findAt(((0.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')
	

region=myAssembly.sets['Set-fix1']

myModel.DisplacementBC(name='BC-1', createStepName='structStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
	amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)
	

v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((trussLength+beamLength, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts, name='Set-fix2')

region=myAssembly.sets['Set-fix2']
	
myModel.DisplacementBC(name='BC-2', createStepName='structStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
	amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
	localCsys=None)
	
#mdb.models['Model-1'].rootAssembly.Set(name='Set-3', vertices=
#    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
#   2.0, 0.0, 0.0), )))
	
v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt((((trussLength+beamLength)/2, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts, name='Set-force')

region=myAssembly.sets['Set-force']

myModel.ConcentratedForce(name='centerLoad', createStepName='structStep',
    region=region, cf2=-1.0*cLoad, distributionType=UNIFORM, field='',
    localCsys=None)
#-------------------------------------------------------

#from mesh import *
import mesh
	
# Assign an element type to the part instance.
#region = (myInstance.cells,)
#elemType = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
#myAssembly.setElementType(regions=region, elemTypes=(elemType,))

# Seed the part instance.
myTrussPart.seedPart(size=0.2,
    deviationFactor=0.1, minSizeFactor=0.1)

#need:
#from abaqus import *
#from abaqusConstants import *

elemType1=mesh.ElemType(elemCode=T3D2)

pR=(myTrussPart.edges,)

myTrussPart.setElementType(regions=pR, elemTypes=(elemType1,))

# Mesh the part instance.
myTrussPart.generateMesh()

myBeamPart.seedPart(size=0.2,
    deviationFactor=0.1, minSizeFactor=0.1)
	
elemType2=mesh.ElemType(elemCode=B32)

pR=(myBeamPart.edges,)

myBeamPart.setElementType(regions=pR, elemTypes=(elemType2,))

# Mesh the part instance.
myBeamPart.generateMesh()	


#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='InteractionTest'

myJob=mdb.Job(name=jobName, model='InteractionTestModel')
	
myJob.submit(consistencyChecking=OFF)


# Save by ldn
