#!/usr/bin/python3

"""
Test cases:
    Two single elements

    Even/odd element number cases:
        One odd length, one even
        Both odd
        Both even

    One median significantly higher than another

    Median in array of size 1, other array way bigger

    Two arrays with same median (one odd, one even)

"""

from medianTwoSortedArrays import findMedianSortedArrays
import unittest

class testCases(unittest.TestCase):

    def testTwoSingleElements(self):
        self.assertEqual(findMedianSortedArrays([1],[4]), 2.5, "Fails two single element case")

    def testOneOddOneEven(self):
        self.assertEqual(findMedianSortedArrays([1,5,12,40,92], [8,16,100,150]), 16, "Fails odd/even case")

    def testSignificantlyHigherMedian(self):
        self.assertEqual(findMedianSortedArrays([3,4,1000,1001,8000],[8,12,20, 5000]), 20, "Fails significantly higher median") 

    def testSignificantlyHigherMedianEven(self):
        self.assertEqual(findMedianSortedArrays([3,4,1000,1001,8000],[8,12,5000]), 506, "Fails significantly higher median (Even variant)") 

    def testBothOdd(self):
        self.assertEqual(findMedianSortedArrays([10,45,70,121,158], [32,67,84,100,137]), 77, "Fails bothOdd lengths")

    def testMedianSizeOneArray(self):
        self.assertEqual(findMedianSortedArrays([51], [4,13,22,71,92,158]), 51, "Fails element in length 1 array")






