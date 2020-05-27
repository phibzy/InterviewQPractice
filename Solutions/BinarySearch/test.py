#!/usr/bin/python3

"""
Tests for Binary Search:

    - Odd length list
    - Even length list
    - Item not in list
    - List of length 1
    - Empty list
    - First pass success
    - Last pass success

"""

import unittest
from binarySearch import binarySearch

class testBinarySearch(unittest.TestCase):

    def testEmptyList(self):
        self.assertTrue(binarySearch([], 4) == -1)

    def testLength1Pass(self):
        self.assertTrue(binarySearch([4], 4) == 0)

    def testLength1Fail(self):
        self.assertTrue(binarySearch([-200], 4) == -1)

    def testOddLengthList(self):
        self.assertTrue(binarySearch([2,7,10,12,18], 7) == 1)

    def testEvenLengthList(self):
        self.assertTrue(binarySearch([2,7,10,12,18,2000], 18) == 4)

    def testFirstPassSuccess(self):
        self.assertTrue(binarySearch([-2,-1,0,1,2], 0) == 2)

    def testLastPassSuccess(self):
        self.assertTrue(binarySearch([-2,-1,0,1,2,200,420,3700,9999,10000,12000],12000) == 10)

    def testItemNotInListLong(self):
        self.assertTrue(binarySearch([-30,-15,-5,-2,0,1,4,20,45,67,72,81,420,960],-3000) == -1)
