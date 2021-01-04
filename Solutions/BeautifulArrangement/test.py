#!/usr/bin/python3

"""
    Test Cases:
        - Base 1 and 2 cases
        - 15 case (max)

"""

import unittest
from arrange import Solution

class testArrange(unittest.TestCase):

    a = Solution()

    def testN(self):
        self.assertEqual(self.a.countArrangement(1), 1)
        self.assertEqual(self.a.countArrangement(2), 2)
        self.assertEqual(self.a.countArrangement(3), 3)
        self.assertEqual(self.a.countArrangement(4), 8)
        self.assertEqual(self.a.countArrangement(15), 24679)

