#!/usr/bin/python3

"""
    Test Cases:
        - Basic divisible cases
        - Truncating zero
        - Negative number combos
        - Overflow cases
        - Random other cases

"""

import unittest
from divideTwoInts import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.divide(9, 3), 3)
        self.assertEqual(self.a.divide(9, -3), -3)
        self.assertEqual(self.a.divide(-9, 3), -3)
        self.assertEqual(self.a.divide(-9, -3), 3)
        self.assertEqual(self.a.divide(3, 9), 0)

    def testRandom(self):
        self.assertEqual(self.a.divide(18, 7), 2)
        self.assertEqual(self.a.divide(36, -1), -36)


