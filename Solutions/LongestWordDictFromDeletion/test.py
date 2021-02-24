#!/usr/bin/python3

"""
    Test Cases:
        - Empty string/dict
        - Single letters, no order (lexo check)
        - Lots of words in dict, none valid
        - All dict words valid

"""

import unittest
from longestDict import Solution

class test(unittest.TestCase):

    a = Solution()

    def testSimple(self):
        self.assertEqual(self.a.findLongestWord("abcde", {}), "")
        self.assertEqual(self.a.findLongestWord("abcde", {x for x in "edcab"}), "a")
        self.assertEqual(self.a.findLongestWord("abcde", {x for x in ["hello", "esh", "twochainz", "bad", "frederickdurst"]}), "")

    def testDefault(self):
        self.assertEqual(self.a.findLongestWord("abpcplea", {x for x in ["ale","apple","monkey","plea"]}), "apple")
        self.assertEqual(self.a.findLongestWord("abpcplea", {x for x in "cab"}), "a")

