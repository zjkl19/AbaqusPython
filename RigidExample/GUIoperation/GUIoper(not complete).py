# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-


#explanation:
#structure:frame
#load:ConcentratedForce in the edge
#post:RF,RM,U

#set Connector(BEAM) in the interaction point

#comment by lindinan in 20170831

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

h=1.0    #height unit:m
l=1.0    #length unit:m


#-----------------------------------------------------

# Create a model.

myModel = mdb.Model(name='RigidFrameExample')
CLoad=2    #only refers to scale; unit:m

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



myModel.RectangularProfile(a=0.3, b=0.4, name='columnProfile')
    
myModel.BeamSection(name='columnSection', integration=BEFORE_ANALYSIS,
	poissonRatio=0.28, beamShape=CONSTANT, profile='columnProfile', thermalExpansion=OFF,
	temperatureDependency=OFF, dependencies=0, table=((2.10e11, 8.203e11), ),
	alphaDamping=0.0,betaDamping=0.0, compositeDamping=0.0, centroid=(0.0, 0.0), 
	shearCenter=(0.0, 0.0),	consistentMassMatrix=False)

###
columnRegion=regionToolset.Region(edges=columnPart.edges)

columnPart.SectionAssignment(region=columnRegion, sectionName='columnSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['columnPart'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(-1.0, 0.0, 0.0), region=Region(
    edges=columnPart.edges.findAt(((0.0, 0.0, 0.0), 
    ), ((0.0, h, 0.0), ), )))
    

#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)

myColumnInstance = myAssembly.Instance(name='columnInstance',
    part=columnPart, dependent=ON)

myBeamInstance = myAssembly.Instance(name='beamInstance',
    part=beamPart, dependent=ON)
