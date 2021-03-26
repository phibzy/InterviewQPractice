#!/usr/bin/python3

"""
    Test Cases:
        - Just a bunch of random URLs should suffice for basic tests
        - Test http and https
        - Test collision resolution
"""

import unittest
from encode import Codec

class test(unittest.TestCase):

    a = Codec()

    def testBasic(self):
        url = "https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3673/"
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        url = "https://www.espncricinfo.com/series/sri-lanka-tour-of-west-indies-2020-21-1252062/west-indies-vs-sri-lanka-1st-test-1252073/live-cricket-score"
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        url = "https://brake.example.com/"
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        url = "https://example.com/bait"
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        url = "http://www.example.com/behavior/attraction?arch=believe"
        self.assertEqual(url, self.a.decode(self.a.encode(url)))

    def testCollision(self):
        url = "https://example.com/bait"
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        self.assertEqual(url, self.a.decode(self.a.encode(url)))
        self.assertEqual(url, self.a.decode(self.a.encode(url)))

