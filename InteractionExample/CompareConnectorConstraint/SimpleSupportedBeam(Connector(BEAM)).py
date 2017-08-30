# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-


#the template of the original example:ExpAbq00.py
#link:http://www.020fea.com/a/5/152/11521.html

#explanation:
#structure:simple supported beam
#load:ConcentratedForce in the midSpan
#post:none

#set Connector(BEAM) in the midSpan

#comment by lindinan in 20170830

from abaqus import *
from abaqusConstants import *
from caeModules import *

from interaction import *
from optimization import *
from sketch import *
from visualization import *
from connectorBehavior import *

import regionToolset

#session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

span=4.0	#span unit:m


#-----------------------------------------------------

# Create a model.

myModel = mdb.Model(name='SimpleSupportedBeamModel1')
cLoad=10000	#only refers to scale

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.

mySketch1 = myModel.ConstrainedSketch(name='beamSketch1',sheetSize=10.0)

# Create the line.

mySketch1.Line(point1=(0.0, 0.0), point2=(span/2, 0.0))

# Create a three-dimensional, deformable part.

myBeamPart1 = myModel.Part(name='beamPart1', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create the part's base feature
myBeamPart1.BaseWire(sketch=mySketch1)

mySketch2 = myModel.ConstrainedSketch(name='beamSketch2',sheetSize=10.0)
mySketch2.Line(point1=(span/2, 0.0), point2=(span, 0.0))
myBeamPart2 = myModel.Part(name='beamPart2', dimensionality=THREE_D, type=DEFORMABLE_BODY)
myBeamPart2.BaseWire(sketch=mySketch2)

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


myModel.IProfile(name='beamProfile', b1=0.1, b2=0.1, h=0.2, l=0.1,
    t1=0.01, t2=0.01, t3=0.01)
    
myModel.BeamSection(name='beamSection', integration=BEFORE_ANALYSIS,
	poissonRatio=0.28, beamShape=CONSTANT, profile='beamProfile', thermalExpansion=OFF,
	temperatureDependency=OFF, dependencies=0, table=((210000000000.0, 82030000000.0), ),
	alphaDamping=0.0,betaDamping=0.0, compositeDamping=0.0, centroid=(0.0, 0.0), 
	shearCenter=(0.0, 0.0),	consistentMassMatrix=False)

###
beamRegion=regionToolset.Region(edges=myBeamPart1.edges)

myBeamPart1.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['beamPart1'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=myBeamPart1.edges.findAt(((0.0, 0.0, 0.0), 
    ), ((span/2, 0.0, 0.0), ), )))
    
###
beamRegion=regionToolset.Region(edges=myBeamPart2.edges)

myBeamPart2.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['beamPart2'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=myBeamPart2.edges.findAt(((span/2, 0.0, 0.0), 
    ), ((span, 0.0, 0.0), ), )))

#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

myBeamInstance1 = myAssembly.Instance(name='beamInstance1',
    part=myBeamPart1, dependent=ON)

myBeamInstance2 = myAssembly.Instance(name='beamInstance2',
    part=myBeamPart2, dependent=ON)

    
myModel.ConnectorSection(name='ConnSect-1', 
    assembledType=BEAM)
    
v1 = myAssembly.instances['beamInstance1'].vertices
v2 = myAssembly.instances['beamInstance2'].vertices

wire = myAssembly.WirePolyLine(points=((v1.findAt(coordinates=(span/2, 0.0, 0.0)), 
    v2.findAt(coordinates=(span/2, 0.0, 0.0))), ), mergeType=IMPRINT, 
    meshable=False)
    
oldName = wire.name
myAssembly.features.changeKey(fromName=oldName, 
    toName='Wire-1')

e1 = myAssembly.edges
edges1 = e1.findAt(((span/2+0.000025, 0.0, 0.0), ))    #??????????????
myAssembly.Set(edges=edges1, name='Wire-1-Set-1')
region = myAssembly.sets['Wire-1-Set-1']
csa = myAssembly.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.

#-------------------------------------------------------

from step import *

# Create a step. The time period of the static step is 1.0, 
# and the initial incrementation is 0.1; the step is created
# after the initial step. 

myModel.StaticStep(name='beamStep', previous='Initial',
    nlgeom=OFF, description='Initial load of the beam.')


#-------------------------------------------------------

from load import *

v=myAssembly.instances['beamInstance1'].vertices
verts=v.findAt(((0.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')

region=myAssembly.sets['Set-fix1']

myModel.DisplacementBC(name='BC-1', createStepName='beamStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

#
v=myAssembly.instances['beamInstance2'].vertices
verts=v.findAt(((span, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix2')

region=myAssembly.sets['Set-fix2']

myModel.DisplacementBC(name='BC-2', createStepName='beamStep',
    region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

v=myAssembly.instances['beamInstance1'].vertices
verts=v.findAt(((span/2, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts, name='Set-force')

region=myAssembly.sets['Set-force']

myModel.ConcentratedForce(name='CLoad', createStepName='beamStep',
    region=region, cf2=-1.0*cLoad, distributionType=UNIFORM, field='',
    localCsys=None)
    
#-------------------------------------------------------

from mesh import *
	
# Assign an element type to the part instance.
#region = (myInstance.cells,)
#elemType = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
#myAssembly.setElementType(regions=region, elemTypes=(elemType,))


# Seed the part instance.
myBeamPart1.seedPart(size=span/20,
    deviationFactor=0.1, minSizeFactor=0.1)

#need:
#from abaqus import *
#from abaqusConstants import *


# Mesh the part instance.
myBeamPart1.generateMesh()

myBeamPart2.seedPart(size=span/20,
    deviationFactor=0.1, minSizeFactor=0.1)



# Mesh the part instance.
myBeamPart2.generateMesh()

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='SimpleSupportedBeam'

myJob=mdb.Job(name=jobName, model='SimpleSupportedBeamModel1')
	
myJob.submit(consistencyChecking=OFF)


#-----------------------------------

from odbAccess import *

myJob.waitForCompletion()

#ms=myJob.messages[-1]

instanceName='beamInstance1'
stepName='beamStep'

frame=-1

x,y=[],[]

#if ms.type==JOB_COMPLETED:
odbPath=jobName+'.odb'
o=openOdb(path=odbPath,readOnly=True)
ns=o.rootAssembly.instances[instanceName.upper()].nodes
fop=o.steps[stepName].getFrame(frameValue=frame).fieldOutputs['U'].values

(u1, u2, u3) = fop[2].data

print str(u2)

with open("nu.txt","w") as f:
    f.write(str(u2))

o.close()
#for i in range(len(ns)):
#    (x1,y1,z1)=ns[i].coordinates
#    (u1,u2)=fop[i].data
#    x.append(x1)
#   y.append(u2)
#o.close()



# Save by ldn
