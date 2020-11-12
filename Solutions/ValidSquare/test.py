#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from validSquare import Solution

class test(unittest.TestCase):

    a = Solution()

    def testDefault(self):
        self.assertTrue(self.a.validSquare([0,0], [1,1], [1,0], [0,1]), "Fails default case")

    def testDefaultDiffOrder(self):
        self.assertTrue(self.a.validSquare([0,0], [1,0], [1,1], [0,1]), "Fails default case in diff order")

    def testSimpleIncorrect(self):
        self.assertFalse(self.a.validSquare([0,0], [1,0], [1,2], [0,1]), "Fails simple incorrect case")

    def testSimpleNeg(self):
        self.assertTrue(self.a.validSquare([0,0], [-1,0], [-1,-1], [0,-1]), "Fails simple neg case")

    def testHalfNeg(self):
        self.assertTrue(self.a.validSquare([0,0], [-1,0], [-1,1], [0,1]), "Fails half neg case")

    def testIncorrectHalfNeg(self):
        self.assertFalse(self.a.validSquare([0,0], [-1,0], [-1,1], [0,-1]), "Fails incorrect half neg case")

    def test4QuarterSquare(self):
        self.assertTrue(self.a.validSquare([-500,500], [-500,-500], [500,-500], [500,500]), "Fails 4 quarter case")

    def testDiagSquare(self):
        self.assertTrue(self.a.validSquare([-1,0], [0,-1], [1,0], [0,1]), "Fails diag square case")

    def testEqualPoints(self):
        self.assertFalse(self.a.validSquare([0,0], [0,0], [0,0], [0,0]), "Fails equal points case")


