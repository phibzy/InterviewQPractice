#!/usr/bin/python3

"""
    Test Cases:
        - Length 1
        - Length 2
        - Basic average case
        - Decent length with no factors

"""

import unittest
from btreeFactors import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.numFactoredBinaryTrees([2]), 1)
        self.assertEqual(self.a.numFactoredBinaryTrees([2,6]), 2)
        self.assertEqual(self.a.numFactoredBinaryTrees([2,4]), 3)
        self.assertEqual(self.a.numFactoredBinaryTrees([2,4,5,10]), 7)
        self.assertEqual(self.a.numFactoredBinaryTrees([2,3,5,11,17,13,31]), 7)

    def testOther(self):
        self.assertEqual(self.a.numFactoredBinaryTrees([18,3,6,2]), 12)




