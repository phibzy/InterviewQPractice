#!/usr/bin/python3

"""
    Test Cases:

        - No houses
        - One house
        - Default
        - Simple

"""

import unittest
from minCost import minCost

class test(unittest.TestCase):

    def invalidHouseCase(self):
        self.assertEqual(minCost([[0, 0]]), 0)
        self.assertEqual(minCost([]), 0)

    def testDefault(self):
        self.assertEqual(minCost([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20)
        self.assertEqual(minCost([[0, 0], [0, 2], [4, 5]]), 9)

