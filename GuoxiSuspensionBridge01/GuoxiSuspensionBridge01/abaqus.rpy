# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by ldn on Wed Nov 08 23:55:24 2017
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.14844, 1.14583), width=169.05, 
    height=113.667)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('GuoxiSuspensionBridge.py', __main__.__dict__)
#: The model "GuoxiSuspensionBridge" has been created.
print 'RT script done'
#: RT script done
