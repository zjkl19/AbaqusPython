# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by Administrator on Mon Dec 18 20:06:43 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=50.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(-5.0, 0.0), point2=(0.0, 0.0))
s.HorizontalConstraint(entity=g.findAt((-2.5, 0.0)), addUndoState=False)
s.Line(point1=(0.0, 0.0), point2=(5.0, 0.0))
s.HorizontalConstraint(entity=g.findAt((2.5, 0.0)), addUndoState=False)
s.ParallelConstraint(entity1=g.findAt((-2.5, 0.0)), entity2=g.findAt((2.5, 
    0.0)), addUndoState=False)

p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseWire(sketch=s)
s.unsetPrimaryObject()


p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p.ReferencePoint(point=(-5.0, -5.0, 0.0))


p = mdb.models['Model-1'].Part(name='Part-3', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p.ReferencePoint(point=(5.0, -5.0, 0.0))

p = mdb.models['Model-1'].parts['Part-3']

mdb.models['Model-1'].RectangularProfile(name='Profile-1', a=1.0, b=1.0)
mdb.models['Model-1'].BeamSection(name='Section-1', 
    integration=BEFORE_ANALYSIS, poissonRatio=0.3, beamShape=CONSTANT, 
    profile='Profile-1', thermalExpansion=OFF, temperatureDependency=OFF, 
    dependencies=0, table=((100.0, 100.0), ), alphaDamping=0.0, 
    betaDamping=0.0, compositeDamping=0.0, centroid=(0.0, 0.0), shearCenter=(
    0.0, 0.0), consistentMassMatrix=False)

p = mdb.models['Model-1'].parts['Part-1']
e = p.edges
edges = e.findAt(((-3.75, 0.0, 0.0), ), ((1.25, 0.0, 0.0), ))
region = p.Set(edges=edges, name='Set-1')
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Part-1']
e = p.edges
edges = e.findAt(((-3.75, 0.0, 0.0), ), ((1.25, 0.0, 0.0), ))
region=p.Set(edges=edges, name='Set-2')
p = mdb.models['Model-1'].parts['Part-1']
p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
    -1.0))
#: Beam orientations have been assigned to the selected regions.

a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
I1=a.Instance(name='Part-1-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['Part-3']
a.Instance(name='Part-3-1', part=p, dependent=OFF)



mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')

a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['Part-1-1'].vertices
r1 = a.instances['Part-2-1'].referencePoints
r2 = a.instances['Part-3-1'].referencePoints
a.WirePolyLine(points=((v11.findAt(coordinates=(0.0, 0.0, 0.0)), r1[1]), (
    v11.findAt(coordinates=(0.0, 0.0, 0.0)), r2[1])), mergeType=IMPRINT, 
    meshable=OFF)
a = mdb.models['Model-1'].rootAssembly
e1 = a.edges
edges1 = e1.findAt(((1.25, -1.25, 0.0), ), ((-1.25, -1.25, 0.0), ))
a.Set(edges=edges1, name='Wire-1-Set-1')
mdb.models['Model-1'].ConnectorSection(name='ConnSect-1', 
    translationalType=CARTESIAN)
elastic_0 = connectorBehavior.ConnectorElasticity(components=(1, 2, 3), table=(
    (1e1, 1e1, 1e1), ))
elastic_0.ConnectorOptions()
mdb.models['Model-1'].sections['ConnSect-1'].setValues(behaviorOptions =(
    elastic_0, ) )

a = mdb.models['Model-1'].rootAssembly
e1 = a.edges
edges1 = e1.findAt(((1.25, -1.25, 0.0), ), ((-1.25, -1.25, 0.0), ))
region=a.Set(edges=edges1, name='Set-2')
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 2 wires or attachment lines.


a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Part-1-1'].vertices
verts1 = v1.findAt(((0.0, 0.0, 0.0), ))
region = a.Set(vertices=verts1, name='Set-3')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf2=-1000.0, distributionType=UNIFORM, field='', 
    localCsys=None)


a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Part-3-1'].referencePoints
refPoints1=(r1[1], )
r2 = a.instances['Part-2-1'].referencePoints
refPoints2=(r2[1], )
v3 = a.instances['Part-1-1'].vertices
verts3 = v3.findAt(((-5.0, 0.0, 0.0), ), ((5.0, 0.0, 0.0), ))
region = a.Set(vertices=verts3, referencePoints=(refPoints1, refPoints2, ), 
    name='Set-4')


mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', 
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)

from mesh import *
	
# Seed the part instance.
a.seedPartInstance(regions=(I1,), size=0.01,
    deviationFactor=0.01, minSizeFactor=0.01)
	
# Mesh the part instance.
a.generateMesh(regions=(I1,))

#-------------------------------------------------------

a.regenerate()

mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)