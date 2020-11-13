#!/usr/bin/python3

"""
    Test Cases:
        - Length of 1
        - All equal elements
        - All diff elements
        - Some same some diff
        - Length 8
        - Avg. Length

TIL: If order doesn't matter, we need to sort outputs to make sure they match up for tests!

"""

import unittest
from permutationsII import Solution

# Have to sort test outputs since order doesn't matter

class test(unittest.TestCase):

    a = Solution()

    def test1(self):
        self.assertEqual(self.a.permuteUnique([1]), [[1]], "Fails length 1 case")

    def testAllEqual(self):
        self.assertEqual(self.a.permuteUnique([1,1,1,1,1,1,1]), [[1,1,1,1,1,1,1]], "Fails all equal case")

    def testAllDifferent(self):
        self.assertEqual(self.a.permuteUnique([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], "Fails all diff case")

    def testMix(self):
        self.assertEqual(self.a.permuteUnique([1,1,2]), [[1,1,2], [1,2,1], [2,1,1]], "Fails mix case")




