#!/usr/bin/python3

"""
   Test Cases:

    - 0
    - 1
    - Random numbers

"""

import unittest
from numberOf1Bits import Solution

class test1Bits(unittest.TestCase):

    a = Solution()

    def test0(self):
        self.assertEqual(self.a.hammingWeight(0), 0)

    def test1(self):
        self.assertEqual(self.a.hammingWeight(1), 1)

    def test8(self):
        self.assertEqual(self.a.hammingWeight(8), 1)

    def test58(self):
        self.assertEqual(self.a.hammingWeight(58), 4)

    def test432(self):
        self.assertEqual(self.a.hammingWeight(432), 4)

    def test65893(self):
        self.assertEqual(self.a.hammingWeight(65893), 6)

    def test6589343(self):
        self.assertEqual(self.a.hammingWeight(6589343), 13)
