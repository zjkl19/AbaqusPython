# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#explanation:
#summary:illustrate the usage of line load
#structure:simple supported beam
#load:line load along the span
#post:SM

#comment by lindinan

from interaction import *
from optimization import *
from sketch import *
from visualization import *
from connectorBehavior import *

import regionToolset

session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

beamLength=1.0

#-----------------------------------------------------

# Create a model.

modelName='UniformLoad_SSBeam'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.

mySketch = myModel.ConstrainedSketch(name='beamSketch',sheetSize=10.0)

# Create the line.

mySketch.Line(point1=(0.0, 0.0), point2=(beamLength, 0.0))

# Create a three-dimensional, deformable part.

myBeamPart = myModel.Part(name='beamPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create the part's base feature
myBeamPart.BaseWire(sketch=mySketch)

#-----------------------------------------------------

from material import *

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


# Assign the section to the region. The region refers 
# to the single cell in this model.

#beamRegion = (myBeamPart.cells,)
beamRegion=regionToolset.Region(edges=myBeamPart.edges)

myBeamPart.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)

myModel.parts['beamPart'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
    edges=myBeamPart.edges.findAt(((beamLength/4, 0.0, 0.0), 
    ), ((beamLength/2, 0.0, 0.0), ), )))

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
    

myModel.FieldOutputRequest(name='F-Output-2', 
    createStepName='beamStep', variables=('SF',))

#-------------------------------------------------------

from load import *


v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((0.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')

region=myAssembly.sets['Set-fix1']

myModel.DisplacementBC(name='BC-1', createStepName='beamStep',
    region=region, u1=0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=UNSET,
	amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)


v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((beamLength, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts, name='Set-fix2')

region=myAssembly.sets['Set-fix2']

myModel.DisplacementBC(name='BC-2', createStepName='beamStep',
    region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
	amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
	localCsys=None)



e1 = myInstance.edges
edges1 = e1.findAt(((beamLength/4, 0.0, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.LineLoad(name='Load-1', 
    createStepName='beamStep', region=region, comp2=-1.0)
#-------------------------------------------------------

from mesh import *
	
# Assign an element type to the part instance.
# Seed the part instance.
myAssembly.seedPartInstance(regions=(myInstance,), size=beamLength/100,
    deviationFactor=0.1, minSizeFactor=0.1)

# Mesh the part instance.
myAssembly.generateMesh(regions=(myInstance,))

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='currJob'

myJob=mdb.Job(name=jobName, model=modelName)

myJob.submit(consistencyChecking=OFF)


# Save by ldn
