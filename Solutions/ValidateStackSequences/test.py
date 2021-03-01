#!/usr/bin/python3

"""
    Test Cases:
        - Simple valid/invalid cases
        - Default cases
        - Empty lists
        - Lists of length 1 (to test loop conditions)

"""

import unittest
from valStack import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertTrue(self.a.validateStackSequences([1,2,3,4,5], [1,2,3,4,5]))
        self.assertTrue(self.a.validateStackSequences([], []))
        self.assertTrue(self.a.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
        self.assertTrue(self.a.validateStackSequences([1], [1]))

        self.assertFalse(self.a.validateStackSequences([1,2,3,4,5], [1,4,2,3,5]))
        self.assertFalse(self.a.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))

