#!/usr/bin/python3

"""
Test Cases:
    - Empty string
    - All whitespace
    - First char (after sign) is letter
    
    - Negative number
    - Number with positive sign
    - Normal number


"""

import unittest
from atoi import Solution

class testATOI(unittest.TestCase):

    a = Solution()

    def testEmpty(self):
        self.assertEqual(self.a.myAtoi(''), 0, "Fails empty string case")

    def testAllWhiteSpace(self):
        self.assertEqual(self.a.myAtoi('        '), 0, "Fails whitespace case")

    def testFirstCharLetter(self):
        self.assertEqual(self.a.myAtoi('     how ya doing cuz?'), 0, "Fails first char incorrect case")

    def testFirstCharLetterWithSign(self):
        self.assertEqual(self.a.myAtoi('     -how ya doing cuz?'), 0, "Fails first char incorrect with sign case")

    def testNormalNumber(self):
        self.assertEqual(self.a.myAtoi('1337'), 1337, "Fails normal number case")

    def testNormalNumberWithPositiveSign(self):
        self.assertEqual(self.a.myAtoi('+1337'), 1337, "Fails normal number case with pos sign")

    def testNormalNumberWithNegativeSign(self):
        self.assertEqual(self.a.myAtoi('-720'), -720, "Fails normal number case with neg sign")

    def testNormalNumberWithWhitespace(self):
        self.assertEqual(self.a.myAtoi('        1337  '), 1337, "Fails normal number with whitespace case")

    def testNormalNumberWithOtherChars(self):
        self.assertEqual(self.a.myAtoi(' -420 is a number! '), -420, "Fails normal number with other chars case")

    #TODO: Max/min int cases


