#!/usr/bin/python3

"""
    Test Cases:
        - Empty string
        - All letters
        - Perfectly balanced string
        - Starting with closed parentheses
        - Starting with open
        - Input of length N, output empty string
        - Length 1 string, invalid and valid

"""

import unittest
from minRemove import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.minRemoveToMakeValid(""), "")
        self.assertEqual(self.a.minRemoveToMakeValid("nicegary"), "nicegary")

    def testBalanced(self):
        self.assertEqual(self.a.minRemoveToMakeValid("aa(noice(d))n"), "aa(noice(d))n")
        self.assertEqual(self.a.minRemoveToMakeValid("(((((((())))))))"), "(((((((())))))))")

    def testInvalid(self):
        self.assertEqual(self.a.minRemoveToMakeValid(")aa(noice(d))n"), "aa(noice(d))n")
        self.assertEqual(self.a.minRemoveToMakeValid("(aa(noice(d))n"), "aa(noice(d))n")
        self.assertEqual(self.a.minRemoveToMakeValid("))))((("), "")
        self.assertEqual(self.a.minRemoveToMakeValid("aa(noice(d))n)"), "aa(noice(d))n")
        self.assertEqual(self.a.minRemoveToMakeValid("())()((("), "()()")


