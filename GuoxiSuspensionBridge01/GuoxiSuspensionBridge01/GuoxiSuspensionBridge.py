# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan

class CreateModel(object):
    """description of class"""

    def __init__(self):
        pass
    def CreatePart(self,myModel):
        import sketch
        import part
        # Create a sketch for the base feature.
        mySketch = myModel.ConstrainedSketch(name='trussSketch1',sheetSize=10.0)
        mySketch.Line(point1=(-1, 1), point2=(0, 0.0))
        # Create a three-dimensional, deformable part.

        trussPart1 = myModel.Part(name='trussPart1', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
	        # Create the part's base feature
        trussPart1.BaseWire(sketch=mySketch)

        #---
        mySketch = myModel.ConstrainedSketch(name='trussSketch2',sheetSize=10.0)
        mySketch.Line(point1=(1, 1), point2=(0, 0.0))
        trussPart2 = myModel.Part(name='trussPart2', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        trussPart2.BaseWire(sketch=mySketch)
        #---
        mySketch = myModel.ConstrainedSketch(name='beamSketch',sheetSize=10.0)
        mySketch.Line(point1=(-1, 0), point2=(1, 0))
        beamPart = myModel.Part(name='beamPart', dimensionality=part.THREE_D, type=part.DEFORMABLE_BODY)
        beamPart.BaseWire(sketch=mySketch)

#start the program
session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

#-----------------------------------------------------

# Create a model.

modelName='GuoxiSuspensionBridge'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------
cm=CreateModel()
cm.CreatePart(myModel)
#-----------------------------------------------------
