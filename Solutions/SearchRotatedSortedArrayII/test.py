#!/usr/bin/python3

"""
    Test Cases:
        - Non-rotated array - both cases
        - Array of duplicates - both with/without target
        - One index out of place - both cases
        - Default case
        - Randomly rotated case
        - Length 1 and 2
        - Negative numbers

Cases with lots of equal elements break this algo


"""

import unittest
from searchRotateII import Solution

class test(unittest.TestCase):

    a = Solution()

    def testDefault1(self):
        self.assertTrue(self.a.search([2,5,6,0,0,1,2], 0), "Fails default case 1")

    def testDefault2(self):
        self.assertFalse(self.a.search([2,5,6,0,0,1,2], 3), "Fails default case 2")

    def testNonRotated1(self):
        self.assertTrue(self.a.search([2,3,4,5,8,9,11,11,11], 3), "Fails NonRotated case 1")

    def testNonRotated2(self):
        self.assertFalse(self.a.search([2,3,4,5,8,9,11,11,11], 7), "Fails NonRotated case 2")

    def testDuplicates1(self):
        self.assertTrue(self.a.search([11,11,11,11,11], 11), "Fails Duplicates case 1")

    def testDuplicates2(self):
        self.assertFalse(self.a.search([11,11,11,11,11], 10), "Fails Duplicates case 2")

    def testOneRotated1(self):
        self.assertTrue(self.a.search([30,2,5,6,8,21], 8), "Fails OneRotated case 1")

    def testOneRotated2(self):
        self.assertFalse(self.a.search([30,2,5,6,8,21], 10), "Fails OneRotated case 2")

    def testRandomRotated1(self):
        self.assertTrue(self.a.search([30,31,31,42,2,2,2,5,5,6,8,21], 21), "Fails RandomRotated case 1")

    def testRandomRotated2(self):
        self.assertFalse(self.a.search([30,31,31,42,2,2,2,5,5,6,8,21], 1), "Fails RandomRotated case 2")

    def testLengthOne1(self):
        self.assertTrue(self.a.search([21], 21), "Fails LengthOne case 1")

    def testLengthOne2(self):
        self.assertFalse(self.a.search([500], 1), "Fails LengthOne case 2")

    def testNegNumbers1(self):
        self.assertTrue(self.a.search([0,4,7,9,9,12,21,-12,-4,-4,-1], 21), "Fails NegNumbers case 1")

    def testNegNumbers2(self):
        self.assertFalse(self.a.search([0,4,7,9,9,12,21,-12,-4,-4,-1], -400), "Fails NegNumbers case 2")
