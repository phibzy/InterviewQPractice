#!/usr/bin/python3

"""
    Test Cases:
        - One unique
        - Default
        - Custom many unique case

"""

import unittest
from uniqueWords import Solution

class testMorseCode(unittest.TestCase):

    a = Solution()

    def testOne(self):
        self.assertEqual(self.a.uniqueMorseRepresentations(["a"]), 1)

    def testDefault(self):
        self.assertEqual(self.a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]), 2)

    def testPSLeffen(self):
        self.assertEqual(self.a.uniqueMorseRepresentations(["gotta", "say", "bro", "you", "looking", "awfully", "weak", "wait", "and", "see", "what", "happens", "in", "the", "salty", "suite", "vanilla", "fox", "dont", "suit", "you", "go", "find", "another", "teach", "you", "a", "lesson", "and", "take", "back", "my", "colour"]), 30)
