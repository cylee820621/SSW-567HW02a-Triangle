# -*- coding: utf-8 -*-
"""
@author: chih-yu lee
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(1000,1000,1000),'Equilateral')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(10, 15, 12),'Scalene')

    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 3, 2),'Isoceles')

    def testIsocelesTriangleB(self):     
        self.assertEqual(classifyTriangle(4, 6, 6),'Isoceles')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1, -1, -1),'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle("200", "0", "0"),'InvalidInput')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(5, 2, 2),'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 5, 1),'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(2, 2, 5),'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

