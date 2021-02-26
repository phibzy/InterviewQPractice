#!/usr/bin/python3

"""
    Test Cases:
        - Basic 1 case
        - AB case
        - A + B case
        - AB + AB case
        - More mixes of above

"""

import unittest
from parentheses import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.scoreOfParentheses("()"), 1)
        self.assertEqual(self.a.scoreOfParentheses("()()"), 2)
        self.assertEqual(self.a.scoreOfParentheses("()()()"), 3)
        self.assertEqual(self.a.scoreOfParentheses("((()))"), 4)

    def testMixes(self):
        self.assertEqual(self.a.scoreOfParentheses("((()))()"), 5)
        self.assertEqual(self.a.scoreOfParentheses("(()())()((()()()))"), 17)

