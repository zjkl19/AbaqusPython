# -*- coding: mbcs -*-

#explanation:
#structure:simple supported beam
#load:ConcentratedForce in the midSpan
#post:none

#comment by lindinan

from interaction import *
from optimization import *
from sketch import *
from visualization import *
from connectorBehavior import *

import regionToolset

session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

beamLength=2.0
cLoad=1.0e1	#only refers to scale

#-----------------------------------------------------

# Create a model.

modelName='SpringExample03'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.
	
mySketch = myModel.ConstrainedSketch(name='beamSketch',sheetSize=10.0)

# Create the line.

mySketch.Line(point1=(-beamLength, 0.0), point2=(-beamLength/2, 0.0))

mySketch.Line(point1=(-beamLength/2, 0.0), point2=(0.0, 0.0))

mySketch.Line(point1=(0.0, 0.0), point2=(beamLength, 0.0))
	
# Create a three-dimensional, deformable part.

myBeamPart = myModel.Part(name='beamPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	
# Create the part's base feature
myBeamPart.BaseWire(sketch=mySketch)

#-----------------------------------------------------

from material import *

# Create a material.
# no need for the "before analysis" in beam analysis
#-------------------------------------------------------

from section import *
# Create the beam section.

myModel.RectangularProfile(a=12, b=1, name='RecProfile')

mySection=myModel.BeamSection(name='beamSection', profile='RecProfile',
    poissonRatio=0.28, integration=BEFORE_ANALYSIS,
	table=((1.0, 1.0), ), alphaDamping=0.0, beamShape=CONSTANT,
    betaDamping=0.0, centroid=(0.0, 0.0), compositeDamping=0.0,
	consistentMassMatrix=False, dependencies=0, shearCenter=(0.0, 0.0),
	temperatureDependency=OFF, thermalExpansion=OFF)
	
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
    edges=myBeamPart.edges.findAt(((-beamLength, 0.0, 0.0), 
    ), ((beamLength, 0.0, 0.0), ), )))

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

#mdb.models['Model-1'].rootAssembly.Set(name='Set-1', vertices=
#    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
#    0.0, 0.0, 0.0), )))

#v=myAssembly.instances('beamInstance').vertices
#verts=v.findAt(((0.0, 0.0, 0.0), ),)

v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((-beamLength, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')	

region=myAssembly.sets['Set-fix1']

myModel.DisplacementBC(name='BC-1', createStepName='beamStep',
    region=region, u1=0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=UNSET,
	amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)

v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((beamLength, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix2')	

region=myAssembly.sets['Set-fix2']

myModel.DisplacementBC(name='BC-2', createStepName='beamStep',
    region=region, u1=UNSET, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=UNSET,
	amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)
	

#connect to ground

import connectorBehavior
#-----------------------------------------------------
v1 = myAssembly.instances['beamInstance'].vertices
myAssembly.WirePolyLine(points=((None, v1.findAt(coordinates=(0.0, 0.0, 0.0))), ), 
    mergeType=IMPRINT, meshable=OFF)

e1 = myAssembly.edges
edges1 = e1.findAt(((0.0001, -0.0001, 0.0), ))
myAssembly.Set(edges=edges1, name='Wire-1-Set-1')
#-----------------------------------------------------

myModel.ConnectorSection(name='ConnSect-1', 
    translationalType=CARTESIAN)    #ConnectorSection object
elastic_0 = connectorBehavior.ConnectorElasticity(components=(2, ), 
    behavior=NONLINEAR, table=((-100, -1), (0.0, 0.0), (
    0, 10.0)))    #connectorBehavior
elastic_0.ConnectorOptions()
myModel.sections['ConnSect-1'].setValues(behaviorOptions =(
    elastic_0, ) )


#-----------------------------------------------------
e1 = myAssembly.edges
#edges1 = e1.findAt(((beamLength+1.0e-4, -1.0e-4, 0.0), ))
edges1 = e1.findAt(((0.0001, -0.0001, 0.0), ))
myAssembly.Set(edges=edges1, name='Wire-1-Set-1')
region = myModel.rootAssembly.sets['Wire-1-Set-1']
csa = myAssembly.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.

	
v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((-beamLength/2, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts, name='Set-force')

region=myAssembly.sets['Set-force']

myModel.ConcentratedForce(name='beamLoad', createStepName='beamStep',
    region=region, cf2=1.0*cLoad, distributionType=UNIFORM, field='',
    localCsys=None)
#-------------------------------------------------------

from mesh import *
	
# Seed the part instance.
myAssembly.seedPartInstance(regions=(myInstance,), size=0.01,
    deviationFactor=0.01, minSizeFactor=0.01)
	
# Mesh the part instance.
myAssembly.generateMesh(regions=(myInstance,))

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

myJob=mdb.Job(name=modelName, model=modelName)
	
myJob.submit(consistencyChecking=OFF)

import unittest   
class myclass(unittest.TestCase):
 
    def setUp(self):  
        pass 
 
    def tearDown(self):  
        pass  
      
    def TestArea(self):  
        self.assertEqual(myModel.profiles['RecProfile'].a*myModel.profiles['RecProfile'].b, 13)  

import logging
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

suite = unittest.TestSuite()
suite.addTest(myclass("TestArea"))
runner = unittest.TextTestRunner()

logging.debug(runner.run(suite))


# Save by ldn
