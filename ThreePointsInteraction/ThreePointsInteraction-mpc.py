# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-


#explanation:
#summary:the illustration of 3 points interaction
#structure:frame
#load:line load
#post:SM

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

span=1.0	#span unit:m

#-----------------------------------------------------

# Create a model.

modelName='SteelFrame'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.

mySketch1 = myModel.ConstrainedSketch(name='beamSketch1',sheetSize=10.0)

# Create the line.

mySketch1.Line(point1=(-1.0*span, 0.0), point2=(0.0, 0.0))

# Create a three-dimensional, deformable part.

myBeamPart1 = myModel.Part(name='beamPart1', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create the part's base feature
myBeamPart1.BaseWire(sketch=mySketch1)

mySketch2 = myModel.ConstrainedSketch(name='beamSketch2',sheetSize=10.0)
mySketch2.Line(point1=(0.0, 0.0), point2=(span, 0.0))
myBeamPart2 = myModel.Part(name='beamPart2', dimensionality=THREE_D, type=DEFORMABLE_BODY)
myBeamPart2.BaseWire(sketch=mySketch2)

mySketch3 = myModel.ConstrainedSketch(name='columnSketch1',sheetSize=10.0)
mySketch3.Line(point1=(0.0, 0.0), point2=(0.0, -1.0*span))
myColumnPart1 = myModel.Part(name='columnPart1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
myColumnPart1.BaseWire(sketch=mySketch3)
#-----------------------------------------------------

from material import *

# Create a material.


#It(umat) seems to be no use in the situation in the "integration=BEFORE_ANALYSIS"

#-------------------------------------------------------

from section import *
# Create the beam section.

myModel.GeneralizedProfile(name='GProfile', area=1.0, i11=1.0, i12=0, i22=1.0, j=1.0, gammaO=0.0, gammaW=0.0) 

Emat=1.0
Gmat=1.0

mySection=myModel.BeamSection(name='beamSection', profile='GProfile',
    poissonRatio=0.28, integration=BEFORE_ANALYSIS,
	table=((Emat, Gmat), ), alphaDamping=0.0, beamShape=CONSTANT,
    betaDamping=0.0, centroid=(0.0, 0.0), compositeDamping=0.0,
	consistentMassMatrix=False, dependencies=0, shearCenter=(0.0, 0.0),
	temperatureDependency=OFF, thermalExpansion=OFF)

###
beamRegion=regionToolset.Region(edges=myBeamPart1.edges)

myBeamPart1.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)

myBeamPart1.assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
    edges=myBeamPart1.edges.findAt(((-1.0*span/2, 0.0, 0.0), 
    ), ((0.0, 0.0, 0.0), ), )))
###
beamRegion=regionToolset.Region(edges=myBeamPart2.edges)

myBeamPart2.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)

myBeamPart2.assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
    edges=myBeamPart2.edges.findAt(((0.0, 0.0, 0.0), 
    ), ((span/2, 0.0, 0.0), ), )))

columnRegion=regionToolset.Region(edges=myColumnPart1.edges)

myColumnPart1.SectionAssignment(region=columnRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)

myColumnPart1.assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
    edges=myColumnPart1.edges.findAt(((0.0, 0.0, 0.0), 
    ), ((0.0, -span/2, 0.0), ), )))
#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

myBeamInstance1 = myAssembly.Instance(name='beamInstance1',
    part=myBeamPart1, dependent=ON)

myBeamInstance2 = myAssembly.Instance(name='beamInstance2',
    part=myBeamPart2, dependent=ON)

myColumnInstance1 = myAssembly.Instance(name='columnInstance1',
    part=myColumnPart1, dependent=ON)

import regionToolset
    
# MPC constraint
v1 = myBeamInstance1.vertices
verts1 = v1.findAt(((0.0, 0.0, 0.0), ))
region1=regionToolset.Region(vertices=verts1)

v1 = myBeamInstance2.vertices
verts1 = v1.findAt(((0.0, 0.0, 0.0), ))
region2=regionToolset.Region(vertices=verts1)
myModel.MultipointConstraint(name='Constraint-1',
    controlPoint=region1, surface=region2, mpcType=BEAM_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)

# MPC constraint
v1 = myBeamInstance1.vertices
verts1 = v1.findAt(((0.0, 0.0, 0.0), ))
region1=regionToolset.Region(vertices=verts1)

v1 = myColumnInstance1.vertices
verts1 = v1.findAt(((0.0, 0.0, 0.0), ))
region2=regionToolset.Region(vertices=verts1)
myModel.MultipointConstraint(name='Constraint-2',
    controlPoint=region1, surface=region2, mpcType=BEAM_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)
#-------------------------------------------------------

from step import *

# Create a step. The time period of the static step is 1.0, 
# and the initial incrementation is 0.1; the step is created
# after the initial step. 

myModel.StaticStep(name='beamStep', previous='Initial',
    nlgeom=OFF, description='Load of the beam.')

myModel.FieldOutputRequest(name='F-Output-2', 
    createStepName='beamStep', variables=('SF',))

#-------------------------------------------------------

from load import *

v=myBeamInstance1.vertices
verts=v.findAt(((-1.0*span, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')

region=myAssembly.sets['Set-fix1']

myModel.DisplacementBC(name='BC-1', createStepName='beamStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)


v=myBeamInstance2.vertices
verts=v.findAt(((span, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix2')

region=myAssembly.sets['Set-fix2']

myModel.DisplacementBC(name='BC-2', createStepName='beamStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

v=myColumnInstance1.vertices
verts=v.findAt(((0.0, -1.0*span, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix3')

region=myAssembly.sets['Set-fix3']

myModel.DisplacementBC(name='BC-3', createStepName='beamStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)
#---------------------
e1 = myBeamInstance1.edges
edges1 = e1.findAt(((-span/2, 0.0, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.LineLoad(name='Load-1', 
    createStepName='beamStep', region=region, comp2=-1.0)

e1 = myBeamInstance2.edges
edges1 = e1.findAt(((span/2, 0.0, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.LineLoad(name='Load-2', 
    createStepName='beamStep', region=region, comp2=-1.0)
#-------------------------------------------------------

from mesh import *

Ediv=100   #the number of the Element division

# Seed the part instance.
myBeamPart1.seedPart(size=span/Ediv,
    deviationFactor=0.1, minSizeFactor=0.1)

#need:
#from abaqus import *
#from abaqusConstants import *

elemType1=mesh.ElemType(elemCode=B31)

pR=(myBeamPart1.edges,)

myBeamPart1.setElementType(regions=pR, elemTypes=(elemType1,))

# Mesh the part instance.
myBeamPart1.generateMesh()

myBeamPart2.seedPart(size=span/Ediv,
    deviationFactor=0.1, minSizeFactor=0.1)
	
elemType2=mesh.ElemType(elemCode=B31)

pR=(myBeamPart2.edges,)

myBeamPart2.setElementType(regions=pR, elemTypes=(elemType2,))

# Mesh the part instance.
myBeamPart2.generateMesh()

myColumnPart1.seedPart(size=span/Ediv,
    deviationFactor=0.1, minSizeFactor=0.1)
	
elemType3=mesh.ElemType(elemCode=B31)

pR=(myColumnPart1.edges,)

myColumnPart1.setElementType(regions=pR, elemTypes=(elemType3,))

# Mesh the part instance.
myColumnPart1.generateMesh()

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='currJob'

myJob=mdb.Job(name=jobName, model=modelName)
	
myJob.submit(consistencyChecking=OFF)

#for i in range(len(ns)):
#    (x1,y1,z1)=ns[i].coordinates
#    (u1,u2)=fop[i].data
#    x.append(x1)
#   y.append(u2)
#o.close()



# Save by ldn
