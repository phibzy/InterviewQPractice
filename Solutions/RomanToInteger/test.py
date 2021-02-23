#!/usr/bin/python3

"""
    Test Cases:
        - Basic numeral conversion
        - Look ahead versions by themselves
        - Standard combo
        - Combo featuring lookahead versions
"""

import unittest
from romanToInt import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.romanToInt("I"), 1)
        self.assertEqual(self.a.romanToInt("V"), 5)
        self.assertEqual(self.a.romanToInt("X"), 10)
        self.assertEqual(self.a.romanToInt("L"), 50)
        self.assertEqual(self.a.romanToInt("C"), 100)
        self.assertEqual(self.a.romanToInt("D"), 500)
        self.assertEqual(self.a.romanToInt("M"), 1000)

    def testEdgyValues(self):
        self.assertEqual(self.a.romanToInt("IV"), 4)
        self.assertEqual(self.a.romanToInt("IX"), 9)
        self.assertEqual(self.a.romanToInt("XL"), 40)
        self.assertEqual(self.a.romanToInt("XC"), 90)
        self.assertEqual(self.a.romanToInt("CD"), 400)
        self.assertEqual(self.a.romanToInt("CM"), 900)

    def testNormalCombo(self):
        self.assertEqual(self.a.romanToInt("MMMCCVI"), 3206)

    def testEdgyCombo(self):
        self.assertEqual(self.a.romanToInt("MMCMXCIX"), 2999)


