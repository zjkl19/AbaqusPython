# -*- coding:utf-8 -*-
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

nSpan=8		#number of span

Gravity = 9.8	#acceleration of gravity 

#-----------------------------------------------------

# Create a model.

myModel = mdb.Model(name='cBeamModel')

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.

mySketch = myModel.ConstrainedSketch(name='beamSketch',sheetSize=10.0)

# Create the line.

mySketch.Line(point1=(0.0, 0.0), point2=(nSpan*span, 0.0))

# Create a three-dimensional, deformable part.

myBeamPart = myModel.Part(name='beamPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create the part's base feature
myBeamPart.BaseWire(sketch=mySketch)

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
        
myModel.GeneralizedProfile(name='beamProfile', area=3.24, i11=0.153819, i12=0.264036, i22=21.7272, j=0.60, gammaO=0.0, gammaW=0.0) 

myModel.BeamSection(name='beamSection', integration=BEFORE_ANALYSIS,
	poissonRatio=0.20, beamShape=CONSTANT, profile='beamProfile', thermalExpansion=OFF,
	temperatureDependency=OFF, dependencies=0, table=((34500000000.0, 13800000000.0), ),
	alphaDamping=0.0,betaDamping=0.0, compositeDamping=0.0, centroid=(0.0, 0.0), 
	shearCenter=(0.0, 0.0),	consistentMassMatrix=False)
	
# Assign the section to the region. The region refers 
# to the single cell in this model.

#mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
#    offsetField='', offsetType=MIDDLE_SURFACE, region=
#    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
#    'Section-1', thicknessAssignment=FROM_SECTION)

#beamRegion = (myBeamPart.cells,)
beamRegion=regionToolset.Region(edges=myBeamPart.edges)

myBeamPart.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['beamPart'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=myBeamPart.edges.findAt(((0.5, 0.0, 0.0), 
    ), ((2.5, 0.0, 0.0), ), )))

#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)
myInstance = myAssembly.Instance(name='beamInstance',
    part=myBeamPart, dependent=OFF)

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

#mdb.models['Model-1'].rootAssembly.Set(name='Set-1', vertices=
#    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
#    0.0, 0.0, 0.0), )))

#v=myAssembly.instances('beamInstance').vertices
#verts=v.findAt(((0.0, 0.0, 0.0), ),)

v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((0.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')
	
#mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
#    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
#    'BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=0.0, 
#    u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET)

region=myAssembly.sets['Set-fix1']

myModel.DisplacementBC(name='BC-1', createStepName='beamStep',
    region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

#---------------------
#es=myBeamPart.edges
#e1=es.findAt((1.,0.,0.),)

#for i in range(2,nSpan+2):
for i in range(2,nSpan+2):
    #v=myAssembly.instances['beamInstance'].vertices
    #verts=v.findAt((((i-1)*span, 0.0, 0.0), ),)
    
    #pt=myBeamPart.DatumPointByEdgeParam(edge=e1,parameter=(i-1)*span/(nSpan*span))
    #d=myBeamPart.datums
    
    verts=v.findAt((((i-1)*span, 0.0, 0.0), ),)
    #verts=v.findAt(((40.0, 0.0, 0.0), ),)
    
    #verts=v.findAt(d[pt.id],)
    #myAssembly.Set(vertices=verts,name='Set-fix'+str(i))
    myAssembly.Set(vertices=verts,name='Set-fix'+str(i))

    region=myAssembly.sets['Set-fix'+str(i)]

    myModel.DisplacementBC(name='BC-' + str(i), createStepName='beamStep',
        region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
        localCsys=None)
#---------------------
    
#mdb.models['Model-1'].rootAssembly.Set(name='Set-3', vertices=
#    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
#   2.0, 0.0, 0.0), )))
	

e = myInstance.edges
setGravity = myAssembly.Set(edges=e, name='Set4Gravity')
Load = myModel.Gravity(name='Load-Gravity', 
    createStepName='Step-Gravity', comp2=-1.0*Gravity, field='', 
    distributionType=UNIFORM, region=setGravity)
	
#-------------------------------------------------------

from mesh import *
	
# Assign an element type to the part instance.
#region = (myInstance.cells,)
#elemType = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
#myAssembly.setElementType(regions=region, elemTypes=(elemType,))

# Seed the part instance.
myAssembly.seedPartInstance(regions=(myInstance,), size=span/5,
    deviationFactor=0.1, minSizeFactor=0.1)
	
# Mesh the part instance.
myAssembly.generateMesh(regions=(myInstance,))

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='cBeam'

myJob=mdb.Job(name=jobName, model='cBeamModel')
	
myJob.submit(consistencyChecking=OFF)


# Save by ldn
