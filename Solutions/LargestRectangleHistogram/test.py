#!/usr/bin/python3

"""
    Test Cases:
        - Largest rectangle is horizontal
        - Largest rectangle is vertical
        - Largest rectangle is just one column

"""

import unittest
from histogram import Solution

class test(unittest.TestCase):

    a = Solution()

    def testDefault(self):
        self.assertEqual(self.a.largestRectangleArea([2,1,5,6,2,3]), 10)

    def testHori(self):
        self.assertEqual(self.a.largestRectangleArea([2,3,2,2,5,6,4]), 14)

    def testVert(self):
        self.assertEqual(self.a.largestRectangleArea([1,4,2,9,0,1,2]), 9)

    def testZero(self):
        self.assertEqual(self.a.largestRectangleArea([4,2,0,3,2,5]), 6)

    def testFailingCase(self):
        self.assertEqual(self.a.largestRectangleArea([3,6,5,7,4,8,1,0]), 20)

