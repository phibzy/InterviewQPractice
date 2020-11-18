#!/usr/bin/python3

"""
    Test Cases:
        - Hitting receptors 0 and 1 on full
        - Default LC test case
        - Hitting southwest corner (and thus 1 corner)
        - Multiple reflections
        - Rebounding off all walls
        - p == 1 case


"""

import unittest
from mReflection import Solution

class test(unittest.TestCase):

    a = Solution()

    def testReceptor1Hit(self):
        self.assertEqual(self.a.mirrorReflection(4,4), 1, "Fails receptor 1 on full case")

    def testReceptor0Hit(self):
        self.assertEqual(self.a.mirrorReflection(4,0), 0, "Fails receptor 0 on full case")

    def testLCDefault(self):
        self.assertEqual(self.a.mirrorReflection(4,2), 2, "Fails receptor 2 on full case")

    def testP1Case(self):
        self.assertEqual(self.a.mirrorReflection(1,1), 1, "Fails P == 1 case")



