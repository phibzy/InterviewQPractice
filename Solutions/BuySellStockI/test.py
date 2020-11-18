#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from buySell import Solution

class test(unittest.TestCase):

    a = Solution()

    def testDefault(self):
        self.assertEqual(self.a.maxProfit([7,1,5,3,6,4]), 5, "Fails default case")

    def testDescOnly(self):
        self.assertEqual(self.a.maxProfit([9,8,7,6,5,4,3,2,1]), 0, "Fails desc only case")

    def testFlatEarnings(self):
        self.assertEqual(self.a.maxProfit([10,10,10,10]), 0, "Fails flat case")

    def testDodgyMin(self):
        self.assertEqual(self.a.maxProfit([5,7,6,6,2]), 2, "Fails flat case")
