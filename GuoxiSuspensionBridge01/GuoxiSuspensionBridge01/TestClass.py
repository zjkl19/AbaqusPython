# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#summary:
#structure: self-anchored suspension bridge
#post:displacement
#goal:verify the completed-state of the suspension bridge

#comment by lindinan


#-----------------------------------------------------

import unittest   

import StructureGeometry as SG    #import Geometry information

# Create geometry

class TestGeometry(unittest.TestCase):
 
    def setUp(self):  
        self.err=1e-5
        self.bridgeGeometry=SG.StructureGeometry()

 
    def tearDown(self):  
        pass  
      
    def TestTowerGeometry(self):
        #test downtower
        realMidSpan=self.bridgeGeometry.downTowerBottomCoordinate[0][1][0]-self.bridgeGeometry.downTowerBottomCoordinate[0][0][0]
        self.assertLessEqual(realMidSpan-70,self.err)

        towerHorizontalSpan=self.bridgeGeometry.downTowerBottomCoordinate[0][1][2]-self.bridgeGeometry.downTowerBottomCoordinate[0][0][2]
        self.assertLessEqual(towerHorizontalSpan-7.50,self.err)

    def TestEndPointSpan(self):
        realEndPointSpan=self.bridgeGeometry.EndPointCoordinate[1][0]-self.bridgeGeometry.EndPointCoordinate[0][0]  
        self.assertLessEqual(realEndPointSpan-127.2,self.err)  


import logging
#logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

suite = unittest.TestSuite()
suite.addTest(TestGeometry("TestTowerGeometry"))
suite.addTest(TestGeometry("TestEndPointSpan"))
runner = unittest.TextTestRunner()

logging.debug(runner.run(suite))
