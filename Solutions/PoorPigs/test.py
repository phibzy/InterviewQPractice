#!/usr/bin/python3

"""
    Test Cases:
        - 1 bucket
        - Enough time to try all buckets with pigs
        - As many pigs needed as there are buckets
        - Odd bucket out deduction case
        - 8 weird case 

    Remember it's about the MINIMUM amount of pigs needed,
    so think of best case scenario as our beloved piggies search
    for the poisoned bucket

"""

import unittest
from poorPigs import Solution

class testPigs(unittest.TestCase):

    a = Solution()

    def test1Bucket(self):
        self.assertEqual(a.poorPigs(1,1,1), 1, "Fails 1 bucket case")

    def test1PigNeeded(self):
        self.assertEqual(a.poorPigs(4,15,60), 1, "Fails 1 pig needed case")

    def testMaxPigs(self):
        self.assertEqual(a.poorPigs(1000,37,37), 1000, "Fails max pigs case")

    def testOddBucketOutCase(self):
        self.assertEqual(a.poorPigs(11,5,50), 1, "Fails odd bucket out case")

    def test8Case(self):
        self.assertEqual(a.poorPigs(8,5,15), 3, "Fails odd bucket out case")

