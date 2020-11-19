#!/usr/bin/python3

"""
    Test Cases:
        - Many intervals, part of one greater interval
        - No overlaps
        - Out of order cases
        - Length 1 case
        - Odd/Even lengths
        
"""

import unittest
from mergeIntervals import Solution

class test(unittest.TestCase):

    a = Solution()

    def testLength1(self):
        self.assertEqual(self.a.merge([[1,2]]), [[1,2]], "Fails length 1 case")

    def testManyOfOne(self):
        self.assertEqual(self.a.merge([[1,4],[2,9],[6,17],[9,10],[3,3]]), [[1,17]], "Fails many intervals of one case")
    
    def testNoOverlaps(self):
        self.assertEqual(self.a.merge([[1,4],[6,9],[10,17],[20,23],[30,32]]), [[1,4],[6,9],[10,17],[20,23],[30,32]], "Fails no overlap case")

    def testOneOverlapEvenLength(self):
        self.assertEqual(self.a.merge([[1,4],[6,9],[31,33],[10,17],[20,23],[30,32]]), [[1,4],[6,9],[10,17],[20,23],[30,33]], "Fails one overlap even length case")

