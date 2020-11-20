#!/usr/bin/python3

"""
    Test Cases:
        - Length 1
        - No repeats
        - As many nested repeats as possible
        - Separate repeats joined together
        - Repeat number with more than 1 digit

    Important notes:
        - Only dealing with lowercase letters, digits
          and square brackets
        - Guaranteed length of 1

"""

import unittest
from decodeString import Solution

class testDecode(unittest.TestCase):

    a = Solution()

    def test1(self):
        self.assertEqual(self.a.decodeString("a"), "a", "Fails one char case")

    def testNoRepeats(self):
        self.assertEqual(self.a.decodeString("youaresmelly"), "youaresmelly", "Fails no repeats case")

    def testNested(self):
        self.assertEqual(self.a.decodeString("2[3[4[a]]]"), "aaaaaaaaaaaaaaaaaaaaaaaa", "Fails nested repeats case")

    def testSeparateRepeats(self):
        self.assertEqual(self.a.decodeString("2[b]3[c]4[a]"), "bbcccaaaa", "Fails separate repeats case")

    def testMoreDigitRepeat(self):
        self.assertEqual(self.a.decodeString("10[b]10[c]2[a]"), "bbbbbbbbbbccccccccccaa", "Fails >1 digit repeat case")
