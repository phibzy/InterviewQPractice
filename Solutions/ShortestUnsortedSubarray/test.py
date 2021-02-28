#!/usr/bin/python3

"""
    Test Cases:
        - No sorting needed
        - Reverse order list
        - Swap in middle
        - First and last swap
        - Vaguely increasing

"""

import unittest
from shortestSub import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.findUnsortedSubarray([1,2,3,4,5,6]), 0)
        self.assertEqual(self.a.findUnsortedSubarray([6]), 0)
        self.assertEqual(self.a.findUnsortedSubarray([]), 0)

    def testSwaps(self):
        self.assertEqual(self.a.findUnsortedSubarray([6,5,4,3,2,1]), 6)
        self.assertEqual(self.a.findUnsortedSubarray([6,2,3,4,5,1]), 6)
        self.assertEqual(self.a.findUnsortedSubarray([1,2,2,2,2,2,2,2,5,3,4,5,6]), 3)
        self.assertEqual(self.a.findUnsortedSubarray([1,2,2,5,2,2,2,2,2,3,4,5,6]), 8)
        self.assertEqual(self.a.findUnsortedSubarray([1,2,3,4,5,6,8,7,9,10,11,12]), 2)

    def testOther(self):
        self.assertEqual(self.a.findUnsortedSubarray([2,3,3,2,4]), 3)
