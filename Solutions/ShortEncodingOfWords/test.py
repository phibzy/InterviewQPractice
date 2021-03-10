#!/usr/bin/python3

"""
    Test Cases:
        - All contained in one word
        - Single letters -> Both equal and unequal
        - Single word
        - No suffixes in common
        - Mixed cases

"""

import unittest
from encode import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasic(self):
        self.assertEqual(self.a.minimumLengthEncoding(["t"]), 2)
        self.assertEqual(self.a.minimumLengthEncoding(["t", "t", "t", "t", "t", "t"]), 2)
        self.assertEqual(self.a.minimumLengthEncoding(["t", "y", "e", "c", "z", "a"]), 12)
        self.assertEqual(self.a.minimumLengthEncoding(["tomothy", "y", "cheese", "c", "eese", "a"]), 19)

