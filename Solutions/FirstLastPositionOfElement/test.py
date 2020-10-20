#!/usr/bin/python3

"""
   Test Cases:
        
        - Empty array
        - Integer not in array
        - Single target integer in array
        - Array consisting of only target integer
        - Array with target int at start
        - Array with target int at end
        - Array of all negative ints
        - Odd and even lengths
        - Array of only target, len 1
        - Len 1, no target

"""

import unittest
from flElement import Solution

class testFLElement(unittest.TestCase):

    a = Solution()

    def testEmpty(self):
        self.assertEqual(self.a.searchRange([], 9), [-1,-1], "Fails empty list case")

    def testNoTarget(self):
        self.assertEqual(self.a.searchRange([1,2,3,4], 9), [-1,-1], "Fails no target case")

    def testSingleTarget(self):
        self.assertEqual(self.a.searchRange([-5,-2,3,9,12,13,14], 9), [3,3], "Fails single target case")

    def testAllTarget(self):
        self.assertEqual(self.a.searchRange([9,9,9,9,9,9,9,9,9,9,9,9,9,9], 9), [0,13], "Fails all target case")

    def testTargetAtStart(self):
        self.assertEqual(self.a.searchRange([1,2,3,4,5,6], 1), [0,0], "Fails target at start case")

    def testTargetAtStartMulti(self):
        self.assertEqual(self.a.searchRange([1,1,1,1,2,3,4,5,6], 1), [0,3], "Fails target at start multi case")

    def testTargetAtEnd(self):
        self.assertEqual(self.a.searchRange([1,2,3,4], 4), [3,3], "Fails target at end case")

    def testTargetAtEndMulti(self):
        self.assertEqual(self.a.searchRange([1,2,3,4,4,4], 4), [3,5], "Fails target at end case multi")

    def testLen1Target(self):
        self.assertEqual(self.a.searchRange([4], 4), [0,0], "Fails len 1 with target case")

    def testLen1NoTarget(self):
        self.assertEqual(self.a.searchRange([-7], 4), [-1,-1], "Fails len 1 with no target case")

    def testAllNeg(self):
        self.assertEqual(self.a.searchRange([-17,-14,-11,-7,-5,-3,-2], -7), [3,3], "Fails all neg case")

