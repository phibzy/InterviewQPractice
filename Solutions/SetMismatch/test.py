#!/usr/bin/python3

"""
    Test Cases:
        - Len 2 case
        - All other cases

"""

import unittest
from setMismatch import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(sorted(self.a.findErrorNums([1,1])), [1,2])

    def testDefault(self):
        self.assertEqual(sorted(self.a.findErrorNums([1,2,2,4])), [2,3])


