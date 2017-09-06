# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

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

span=5.0	#span unit:m

nSpan=2		#number of span

Gravity = 9.8	#acceleration of gravity 

#-----------------------------------------------------

# Create a model.

myModel = mdb.Model(name='cBeamModel')

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.

mySketch1 = myModel.ConstrainedSketch(name='beamSketch1',sheetSize=10.0)

# Create the line.

mySketch1.Line(point1=(0.0, 0.0), point2=(nSpan*span, 0.0))

# Create a three-dimensional, deformable part.

myBeamPart1 = myModel.Part(name='beamPart1', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create the part's base feature
myBeamPart1.BaseWire(sketch=mySketch1)

myBeamPart1.PartitionEdgeByPoint(edge=
    myBeamPart1.edges.findAt((2.5, 0.0, 0.0), ), 
    point=myBeamPart1.InterestingPoint(
    myBeamPart1.edges.findAt((2.5, 0.0, 0.0), ), 
    MIDDLE))

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
        
#myModel.GeneralizedProfile(name='beamProfile', area=3.24, i11=0.153819, i12=0.264036, i22=21.7272, j=0.0060, gammaO=0.0, gammaW=0.0) 
myModel.RectangularProfile(name='beamProfile', a=0.3, b=0.4)

myModel.BeamSection(name='beamSection', integration=BEFORE_ANALYSIS,density=2549.0,
	poissonRatio=0.20, beamShape=CONSTANT, profile='beamProfile', thermalExpansion=OFF,
	temperatureDependency=OFF, dependencies=0, table=((34500000000.0, 13800000000.0), ),
	alphaDamping=0.0,betaDamping=0.0, compositeDamping=0.0, centroid=(0.0, 0.0), 
	shearCenter=(0.0, 0.0),	consistentMassMatrix=False)

###
beamRegion=regionToolset.Region(edges=myBeamPart1.edges)

myBeamPart1.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['beamPart1'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=myBeamPart1.edges.findAt(((0.5, 0.0, 0.0), 
    ), ((2.5, 0.0, 0.0), ), )))
    

#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

myBeamInstance1 = myAssembly.Instance(name='beamInstance1',
    part=myBeamPart1, dependent=ON)
#-------------------------------------------------------

from step import *

# Create a step. The time period of the static step is 1.0, 
# and the initial incrementation is 0.1; the step is created
# after the initial step. 

myModel.StaticStep(name='beamStep', previous='Initial',
    nlgeom=OFF, description='Load of the beam.')

myModel.StaticStep(name='Step-Gravity', previous='beamStep',
    minInc=0.001, initialInc=0.2, description='Load of the Gravity.')
    
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


for i in range(2,nSpan+1):
    v=myAssembly.instances['beamInstance'+str(i-1)].vertices
    verts=v.findAt((((i-1)*span, 0.0, 0.0), ),)

    myAssembly.Set(vertices=verts,name='Set-fix'+str(i))

    region=myAssembly.sets['Set-fix'+str(i)]

    myModel.DisplacementBC(name='BC-' + str(i), createStepName='beamStep',
        region=region, u1=UNSET, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=UNSET,
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
        localCsys=None)
#---------------------

#the end of the cBeam
v=myAssembly.instances['beamInstance1'].vertices
verts=v.findAt(((nSpan*span, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix'+str(nSpan+1))

region=myAssembly.sets['Set-fix'+str(nSpan+1)]

myModel.DisplacementBC(name='BC-'+str(nSpan+1), createStepName='beamStep',
    region=region, u1=UNSET, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)


e = myBeamInstance1.edges
setGravity = myAssembly.Set(edges=e, name='Set4Gravity1')
Load1 = myModel.Gravity(name='Load-Gravity1', 
    createStepName='Step-Gravity', comp2=-1.0*Gravity, field='', 
    distributionType=UNIFORM, region=setGravity)
    
#-------------------------------------------------------

from mesh import *
	
# Assign an element type to the part instance.
#region = (myInstance.cells,)
#elemType = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
#myAssembly.setElementType(regions=region, elemTypes=(elemType,))


# Seed the part instance.
myBeamPart1.seedPart(size=span/5,
    deviationFactor=0.1, minSizeFactor=0.1)

#need:
#from abaqus import *
#from abaqusConstants import *

elemType1=mesh.ElemType(elemCode=B31)

pR=(myBeamPart1.edges,)

myBeamPart1.setElementType(regions=pR, elemTypes=(elemType1,))

# Mesh the part instance.
myBeamPart1.generateMesh()

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='cBeam'

myJob=mdb.Job(name=jobName, model='cBeamModel')
	
myJob.submit(consistencyChecking=OFF)


#-----------------------------------

from odbAccess import *

myJob.waitForCompletion()

#ms=myJob.messages[-1]

instanceName='beamInstance1'
stepName='Step-Gravity'

frame=1

x,y=[],[]

#if ms.type==JOB_COMPLETED:
odbPath=jobName+'.odb'
o=openOdb(path=odbPath,readOnly=True)
ns=o.rootAssembly.instances[instanceName.upper()].nodes
fop=o.steps[stepName].getFrame(frameValue=frame).fieldOutputs['U'].values

(u1, u2, u3) = fop[i].data

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
