#!/usr/bin/python3

"""
    Test Cases:
        - 1
        - All the IV, IX type cases in one number - e.g. CMXCIV etc.
        - 3999
        - Some basic numbers

"""

import unittest
from intToRoman import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.intToRoman(1), "I")
        self.assertEqual(self.a.intToRoman(4), "IV")
        self.assertEqual(self.a.intToRoman(5), "V")
        self.assertEqual(self.a.intToRoman(9), "IX")

    def testCombos(self):
        self.assertEqual(self.a.intToRoman(3999), "MMMCMXCIX")
        self.assertEqual(self.a.intToRoman(1942), "MCMXLII")
        self.assertEqual(self.a.intToRoman(464), "CDLXIV")

