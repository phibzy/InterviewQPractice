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
        self.assertFalse(binarySearch([], 4))

    def testLength1Pass(self):
        self.assertTrue(binarySearch([4], 4))

    def testLength1Fail(self):
        self.assertFalse(binarySearch([-200], 4))

    def testOddLengthList(self):
        self.assertTrue(binarySearch([2,7,10,12,18], 7))

    def testEvenLengthList(self):
        self.assertTrue(binarySearch([2,7,10,12,18,2000], 18))

    def testFirstPassSuccess(self):
        self.assertTrue(binarySearch([-2,-1,0,1,2], 0))

    def testLastPassSuccess(self):
        self.assertTrue(binarySearch([-2,-1,0,1,2,200,420,3700,9999,10000,12000],12000))

    def testItemNotInListLong(self):
        self.assertFalse(binarySearch([-30,-15,-5,-2,0,1,4,20,45,67,72,81,420,960],-3000))
