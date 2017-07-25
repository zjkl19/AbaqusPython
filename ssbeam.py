# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *
from viewerModules import *
import regionToolset
import mesh

mdb.saveAs(pathName='D:/SIMULIA/Temp/ExpAbq00.cae')
#: The model database has been saved to "D:\SIMULIA\Temp\ExpAbq00.cae".

s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=10.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints

s.setPrimaryObject(option=STANDALONE)

s.Line(point1=(0.0, 0.0), point2=(2.0, 0.0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(2.0, 0.0), point2=(4.0, 0.0))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.ParallelConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseWire(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']

del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].IProfile(name='Profile-1', l=0.1, h=0.2, b1=0.1, b2=0.1, 
    t1=0.01, t2=0.01, t3=0.01)

#p = mdb.models['Model-1'].parts['Part-1']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#3 ]', ), )
region=p.Set(edges=edges, name='Set-1')
#p = mdb.models['Model-1'].parts['Part-1']
p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
    1.0))
#: Beam orientations have been assigned to the selected regions.

mdb.models['Model-1'].BeamSection(name='Section-1', 
    integration=BEFORE_ANALYSIS, poissonRatio=0.28, beamShape=CONSTANT, 
    profile='Profile-1', thermalExpansion=OFF, temperatureDependency=OFF, 
    dependencies=0, table=((210000000000.0, 82030000000.0), ), 
    alphaDamping=0.0, betaDamping=0.0, compositeDamping=0.0, centroid=(0.0, 
    0.0), shearCenter=(0.0, 0.0), consistentMassMatrix=False)

p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
	
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
#p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=OFF)

mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')

#a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Part-1-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
region = a.Set(vertices=verts1, name='Set-1')
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', 
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)

#a = mdb.models['Model-1'].rootAssembly
#v1 = a.instances['Part-1-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#4 ]', ), )
region = a.Set(vertices=verts1, name='Set-2')
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)

a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Part-1-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
region = a.Set(vertices=verts1, name='Set-3')
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1', 
    region=region, cf2=-10000.0, distributionType=UNIFORM, field='', 
    localCsys=None)

a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.seedPartInstance(regions=partInstances, size=0.2, deviationFactor=0.1, 
    minSizeFactor=0.1)

a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.generateMesh(regions=partInstances)

mdb.Job(name='ExpAbq00', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)

mdb.jobs['ExpAbq00'].submit(consistencyChecking=OFF)
