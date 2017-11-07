# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan

session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

#-----------------------------------------------------

# Create a model.

modelName='GuoxiSuspensionBridge'

myModel = mdb.Model(name=modelName)

#-----------------------------------------------------

import GuoxiPackage.CreatePart

cp=GuoxiPackage.CreatePart.CreatePart(myModel)
#-----------------------------------------------------
