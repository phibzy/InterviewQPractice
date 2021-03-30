#!/usr/bin/python3

"""
    Test Cases:
        - Length 1 list
        - Length 2 list
        - Fee large enough to destroy any hope of profit
        - Obvious, only 1 buy required case
        - Multiple buy cases:
            - 0 fee
            - >0 fee, where greedy approach wouldn't work

"""

import unittest
from buySell import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.maxProfit([1], 300), 0)
        self.assertEqual(self.a.maxProfit([9,8,7,6,5,4,3,2,1], 0), 0)
        self.assertEqual(self.a.maxProfit([1,9], 3), 5)
        self.assertEqual(self.a.maxProfit([1, 9, 13, 90, 32, 5, 16, 88, 153], 152), 0)
        self.assertEqual(self.a.maxProfit([1, 3, 2, 9, 1, 4, 4, 1, 6], 3), 7)

    def testMulti(self):
        self.assertEqual(self.a.maxProfit([2,9,5,8,16,5,17], 2), 24)
        self.assertEqual(self.a.maxProfit([1,5,2,6,5,10], 3), 6)

        # Troubleshoot this later
        self.assertEqual(self.a.maxProfit([4,5,2,4,3,3,1,2,5,4], 1), 4)
    
    def testDefault(self):
        self.assertEqual(self.a.maxProfit([1,3,7,5,10,3], 3), 6)
        self.assertEqual(self.a.maxProfit([1,3,2,8,4,9], 2), 8)
        

