#!/usr/bin/python3

"""
   Test Cases:

    - Empty
    - 1 bracket
    - Balanced but wrong brackets
    - Normal case
    - One out

"""

import unittest
from validParentheses import Solution

class testIsValid(unittest.TestCase):

    a = Solution()

    def testEmpty(self):
        self.assertTrue(self.a.isValid(''), "Fails empty case")

    def testOne(self):
        self.assertFalse(self.a.isValid('('), "Fails single case")

    def testBalancedButWrongBrackets(self):
        self.assertFalse(self.a.isValid('((()})'), "Fails balanced but wrong case")

    def testNormalCase(self):
        self.assertTrue(self.a.isValid('((()))'), "Fails normal case")

    def testOneOut(self):
        self.assertFalse(self.a.isValid('((())))'), "Fails one out case")

    def testOneOutAlternate(self):
        self.assertFalse(self.a.isValid('(((()))'), "Fails one out alternate case")
