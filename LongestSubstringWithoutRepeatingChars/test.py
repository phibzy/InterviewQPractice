#!/usr/bin/python3

import unittest
from longestSubstring import lengthOfLongestSubString

"""

Questions to interviewer:
    - Will the string itself ever be empty?

Test Cases:
    - Empty string
    - All unique characters
    - Longest string at beginning
    - Longest string in middle
    - Longest string at end
    - All the same character
    - All the same character but 1

"""

class testCases(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(lengthOfLongestSubString(''), 0, "Error for empty string")

    def testAllUnique(self):
        self.assertEqual(lengthOfLongestSubString('abcdefg'), 7, "Error for all unique values")

    def testAllSame(self):
        self.assertEqual(lengthOfLongestSubString('aaaaaaa'), 1, "Error for all same char")

    def testAllSameButOne(self):
        self.assertEqual(lengthOfLongestSubString('aaaabaa'), 2, "Error for all same but one")











