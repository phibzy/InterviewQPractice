#!/usr/bin/python3

"""
    Test Cases:
        - 1 cases
        - Simple greedy-esque cases
        - Ambiguous cases
        - Coins not in order

"""

import unittest
from coinChange import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.coinChange([1,2,3,4], 1), 1)
        self.assertEqual(self.a.coinChange([3,5], 1), -1)
        self.assertEqual(self.a.coinChange([3,500], 0), 0)

    def testGreedy(self):
        self.assertEqual(self.a.coinChange([1,3,5], 13), 3)
        self.assertEqual(self.a.coinChange([1,3,5,8], 19), 3)


