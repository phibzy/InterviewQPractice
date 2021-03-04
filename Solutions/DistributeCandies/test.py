#!/usr/bin/python3

"""
    Test Cases:
        - Length two of candies
        - All unique
        - All the same
        
"""

import unittest
from candies import Solution

class test(unittest.TestCase):

    a = Solution()

    def testTwo(self):
        self.assertEqual(self.a.distributeCandies([1,2]), 1)
        self.assertEqual(self.a.distributeCandies([2,2]), 1)

    def testUnique(self):
        self.assertEqual(self.a.distributeCandies([1,2,-3,7,28,10000,-3000,90]), 4)

    def testSame(self):
        self.assertEqual(self.a.distributeCandies([6,6,6,6,6,6,6,6,6,6,6,6]),1)


