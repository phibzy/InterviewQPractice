#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from arithmeticSlices import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasicSequences(self):
        self.assertEqual(self.a.numberOfArithmeticSlices([1,2,3]), 1)
        self.assertEqual(self.a.numberOfArithmeticSlices([1,9,3]), 0)
        self.assertEqual(self.a.numberOfArithmeticSlices([1,2,3,4]), 3)
        self.assertEqual(self.a.numberOfArithmeticSlices([2,4,6,8]), 3)
        self.assertEqual(self.a.numberOfArithmeticSlices([2,-4,-10,-16]), 3)
        self.assertEqual(self.a.numberOfArithmeticSlices([1,2,3,4,5,6,7]), 15)
        self.assertEqual(self.a.numberOfArithmeticSlices([1,2,3,4,5,6,7,8]), 21)
        self.assertEqual(self.a.numberOfArithmeticSlices([-3,-3,-3,-3,-3]), 6)

    def testNoSequences(self):
        self.assertEqual(self.a.numberOfArithmeticSlices([]), 0)
        self.assertEqual(self.a.numberOfArithmeticSlices([1,2]), 0)
        self.assertEqual(self.a.numberOfArithmeticSlices([180]), 0)
        self.assertEqual(self.a.numberOfArithmeticSlices([0,3,7,99,21,-4,-1000]), 0)
        self.assertEqual(self.a.numberOfArithmeticSlices([0,1,4,5,12,8]), 0)
        self.assertEqual(self.a.numberOfArithmeticSlices([5, -5, 5, -5]), 0)

    def testRandomSeq(self):
        self.assertEqual(self.a.numberOfArithmeticSlices([0,3,7,11,15,19,23,27,-1000,-1001,-1002,-1003,42,420,360,22,21,20,4]), 19)








