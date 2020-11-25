#!/usr/bin/python3

"""
    Test Cases:
        - Test even K
        - Test K divisible by 5
        - Test 1
        - Test 111
        - Test assorted cases


"""

import unittest
from smallestInt import Solution

class testSmallestIntDivK(unittest.TestCase):

    a = Solution()

    def test1(self):
        self.assertEqual(self.a.smallestRepunitDivByK(1), 1)

    def test111(self):
        self.assertEqual(self.a.smallestRepunitDivByK(111), 3)

    def testEven(self):
        self.assertEqual(self.a.smallestRepunitDivByK(4), -1)

    def testDiv5(self):
        self.assertEqual(self.a.smallestRepunitDivByK(105), -1)

    def testAssorted1(self):
        self.assertEqual(self.a.smallestRepunitDivByK(7), 6)

    def testAssorted2(self):
        self.assertEqual(self.a.smallestRepunitDivByK(9), 9)

    def testAssorted3(self):
        self.assertEqual(self.a.smallestRepunitDivByK(13), 6)

    def testMaxValidK(self):
        self.assertEqual(self.a.smallestRepunitDivByK(99999), 45)

    def testMaxInvalidK(self):
        self.assertEqual(self.a.smallestRepunitDivByK(100000), -1)

    def testBigN(self):
        self.assertEqual(self.a.smallestRepunitDivByK(99997), 7866)
