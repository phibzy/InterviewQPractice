#!/usr/bin/python3

"""
    Test Cases:
        - Multiple digits
        - Lots of spaces
        - Order of Ops (i.e. 2+2*2)
        - Only a number

"""

import unittest
from basicCalcII import Solution

class test(unittest.TestCase):

    a = Solution()

    def testNumberOnly(self):
        self.assertEqual(self.a.calculate("300"), 300)

    def testMultipyDivideOnly(self):
        self.assertEqual(self.a.calculate("  20 * 2 * 3       /         1"), 120)

    def testMultipyDivideOnly2(self):
        self.assertEqual(self.a.calculate("  20 / 9 * 3       /         2"), 3)

    def testAddSubtract1(self):
        self.assertEqual(self.a.calculate("  20 - 4     + 2 + 8 - 9 - 3"), 14)

    def testAddSubtract2(self):
        self.assertEqual(self.a.calculate("  20 + 9 * 2 - 4 /3"), 37)

    def testSimpleMix(self):
        self.assertEqual(self.a.calculate("2 + 3 * 2  "), 8)


