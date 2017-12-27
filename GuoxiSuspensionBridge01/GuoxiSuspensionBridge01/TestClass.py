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
        pass

    def TestEndPointSpan(self):
        realEndPointSpan=self.bridgeGeometry.EndPointCoordinate[1][0]-self.bridgeGeometry.EndPointCoordinate[0][0]  
        self.assertLessEqual(realEndPointSpan-127.2,self.err)

    def TestGirderA_ACoordinate():
        pass
    
    def TestGirderB_BCoordinate():
        pass     

    def TestGirderC_CCoordinate():
        pass

    def TestGirderD_DCoordinate():
        pass

    def TestGirderE_ECoordinate():
        pass

    def TestGirderF_FCoordinate():
        pass

    def TestGirderWeightsSupportSpan(self):
        realSpan=self.bridgeGeometry.GirderWeightsSupportCoordinate[1][0]-self.bridgeGeometry.GirderWeightsSupportCoordinate[0][0]
        theorySpan=120.0  
        self.assertLessEqual(realSpan-theorySpan,self.err)

    def TestGirderTowerSupportSpan(self):
        pass

    def TestStiffeningGirderCoordinatePointCounts(self):      
        self.assertEqual(len(self.bridgeGeometry.stiffeningGirderCoordinate),73)

    def TestGirderTowerBeamCoordinate(self):
       pass

    def TestGirderTowerBeamSupportCoordinate(self):
       pass

    def TestTowerCoordinate(self):
       pass

    def TestCablePointCounts(self):
        self.assertEqual(len(self.bridgeGeometry.cableCoordinate[0]),23)
        self.assertEqual(len(self.bridgeGeometry.cableCoordinate[1]),23)

    def TestSuspenderCounts(self):
        self.assertEqual(len(self.bridgeGeometry.hangingPointCoordinate[0]),19)
        self.assertEqual(len(self.bridgeGeometry.hangingPointCoordinate[1]),19)

import logging
#logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

suite = unittest.TestSuite()
suite.addTest(TestGeometry("TestTowerGeometry"))
suite.addTest(TestGeometry("TestEndPointSpan"))
suite.addTest(TestGeometry("TestGirderWeightsSupportSpan"))
suite.addTest(TestGeometry("TestStiffeningGirderCoordinatePointCounts"))
suite.addTest(TestGeometry("TestCablePointCounts"))
suite.addTest(TestGeometry("TestSuspenderCounts"))

runner = unittest.TextTestRunner()

logging.debug(runner.run(suite))
