#!/usr/bin/python3

"""
    Min string length is 1, all lowercase chars


    Test Cases:
        - 1 char
        - String of unique chars
        - String of same char only
        - Equal substrings

"""

import unittest
from conChar import Solution

class test(unittest.TestCase):

   a = Solution()

   def test1(self):
       self.assertEqual(self.a.maxPower("a"), 1, "Fails 1 char case")

   def test2Same(self):
       self.assertEqual(self.a.maxPower("aa"), 2, "Fails 2 same char case")

   def testUnique(self):
       self.assertEqual(self.a.maxPower("abcdefghi"), 1, "Fails unique char case")

   def testSameChar(self):
       self.assertEqual(self.a.maxPower("aaaaaaaaa"), 9, "Fails same char case")

   def testEqualSubstrings(self):
       self.assertEqual(self.a.maxPower("aaaaabaaaaa"), 5, "Fails equal substring case")



