# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=10.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    2.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(2.0, 0.0), point2=(
    4.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.0, 0.0), )
    , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    3.0, 0.0), ))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseWire(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].IProfile(b1=0.1, b2=0.1, h=0.2, l=0.1, name='Profile-1', 
    t1=0.01, t2=0.01, t3=0.01)
mdb.models['Model-1'].BeamSection(alphaDamping=0.0, beamShape=CONSTANT, 
    betaDamping=0.0, centroid=(0.0, 0.0), compositeDamping=0.0, 
    consistentMassMatrix=False, dependencies=0, integration=BEFORE_ANALYSIS, 
    name='Section-1', poissonRatio=0.28, profile='Profile-1', shearCenter=(0.0, 
    0.0), table=((210000000000.0, 82030000000.0), ), temperatureDependency=OFF, 
    thermalExpansion=OFF)
mdb.models['Model-1'].parts['Part-1'].Set(edges=
    mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.5, 0.0, 0.0), ), ((
    2.5, 0.0, 0.0), ), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
mdb.models['Model-1'].rootAssembly.Set(name='Set-1', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
    0.0, 0.0, 0.0), )))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=0.0, 
    u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-2', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
    4.0, 0.0, 0.0), )))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'BC-2', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'], u1=UNSET, 
    u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET)
mdb.models['Model-1'].rootAssembly.Set(name='Set-3', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
    2.0, 0.0, 0.0), )))
mdb.models['Model-1'].ConcentratedForce(cf2=-10000.0, createStepName='Step-1', 
    distributionType=UNIFORM, field='', localCsys=None, name='Load-1', region=
    mdb.models['Model-1'].rootAssembly.sets['Set-3'])
mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    minSizeFactor=0.1, regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], ), size=0.2)
mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], ))
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='ExpAbq00', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='', waitHours=0, waitMinutes=0)
mdb.models['Model-1'].parts['Part-1'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.5, 0.0, 0.0), 
    ), ((2.5, 0.0, 0.0), ), )))
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['ExpAbq00'].submit(consistencyChecking=OFF)
mdb.jobs['ExpAbq00']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'bdl-PC', 'handle': 0, 'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'D:\\SIMULIA\\Temp\\ExpAbq00.odb', 'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'bdl-PC', 'handle': 60784, 'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'ExpAbq00', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['ExpAbq00']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'ExpAbq00', 'memory': 23.6787071228027})
mdb.jobs['ExpAbq00']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
    'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1, 
    'jobName': 'ExpAbq00', 'severe': 0, 'iterations': 1, 
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['ExpAbq00']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'ExpAbq00'})
mdb.jobs['ExpAbq00']._Message(JOB_COMPLETED, {
    'time': 'Sat Aug 05 12:09:15 2017', 'jobName': 'ExpAbq00'})
# Save by bdl on 2017_08_05-12.10.39; build 6.13-1 2013_05_16-10.28.56 126354
