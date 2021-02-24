#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from brokenCalc import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.brokenCalc(1, 1), 0)
        self.assertEqual(self.a.brokenCalc(1, 2), 1)
        self.assertEqual(self.a.brokenCalc(1, 8), 3)
        self.assertEqual(self.a.brokenCalc(5, 8), 2)
        self.assertEqual(self.a.brokenCalc(6, 20), 3)
        self.assertEqual(self.a.brokenCalc(3, 10), 3)
        self.assertEqual(self.a.brokenCalc(3, 10), 3)
        self.assertEqual(self.a.brokenCalc(6, 41), 6)
