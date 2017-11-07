# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan

class CreateModel(object):
    """Create 'Part' of the suspension bridge"""

    def __init__(self):
        pass
    def CreatePart(self,myModel,part):
        # Create a sketch for the base feature.
        mySketch = myModel.ConstrainedSketch(name='trussSketch1',sheetSize=10.0)
        mySketch.Line(point1=(-1, 1), point2=(0, 0.0))
        # Create a three-dimensional, deformable part.

        self.trussPart1 = myModel.Part(name='trussPart1', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
	    # Create the part's base feature
        self.trussPart1.BaseWire(sketch=mySketch)

        #---
        mySketch = myModel.ConstrainedSketch(name='trussSketch2',sheetSize=10.0)
        mySketch.Line(point1=(1, 1), point2=(0, 0.0))
        self.trussPart2 = myModel.Part(name='trussPart2', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        self.trussPart2.BaseWire(sketch=mySketch)
        #---
        mySketch = myModel.ConstrainedSketch(name='beamSketch',sheetSize=10.0)
        mySketch.Line(point1=(-1, 0), point2=(1, 0))
        self.beamPart = myModel.Part(name='beamPart', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        self.beamPart.BaseWire(sketch=mySketch)

#start the program
session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

#-----------------------------------------------------

# Create a model.

modelName='GuoxiSuspensionBridge'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------
import part

cm=CreateModel()
cm.CreatePart(myModel,part)
#-----------------------------------------------------
