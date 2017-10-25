#!/usr/bin/env python  
#encoding: utf-8

import unittest   
class myclass(unittest.TestCase):
 
    def setUp(self):  
        pass 
 
    def tearDown(self):  
        pass  
      
    def testsum(self):  
        self.assertEqual(self.sum(1, 2), 4)  
         
    def sum(self, x, y):  
        return x+y  
      

suite = unittest.TestSuite()
suite.addTest(myclass("testsum"))
runner = unittest.TextTestRunner()
runner.run(suite)