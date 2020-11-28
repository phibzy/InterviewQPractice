#!/usr/bin/python3

"""
    Test Cases:
        - Length 1 list
        - Obvious impossible case
        - Even split
        - Uneven split

"""

import unittest
from partition import Solution

class testPartition(unittest.TestCase):

    a = Solution()

    def testLength1(self):
        self.assertFalse(self.a.canPartition([20]))

    def testObviousImpossible(self):
        self.assertFalse(self.a.canPartition([1,20,7,8]))

    def testLessObviousImpossible(self):
        self.assertFalse(self.a.canPartition([1,2,4,6,9,11]))

    def testEvenSplit(self):
        self.assertTrue(self.a.canPartition([4,6,5,5]))

    def testUnevenSplit(self):
        self.assertTrue(self.a.canPartition([7,3,2,4,2]))

    def testRandomTrue1(self):
        self.assertTrue(self.a.canPartition([2,2,6,9,11,14]))

    def testRandomTrue2(self):
        self.assertTrue(self.a.canPartition([1,2,3,4,5,6,7]))
