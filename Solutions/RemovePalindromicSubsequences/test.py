#!/usr/bin/python3

"""
    Test Cases:
        - Single char
        - Palindrome string
        - Non-palindrome string

"""

import unittest
from removePal import Solution

class test(unittest.TestCase):

    a = Solution()

    def testPal(self):
        self.assertEqual(self.a.removePalindromeSub("a"), 1)
        self.assertEqual(self.a.removePalindromeSub("aaaaaaaaaaa"), 1)
        self.assertEqual(self.a.removePalindromeSub("baba"), 2)
        self.assertEqual(self.a.removePalindromeSub("baaaab"), 1)
        self.assertEqual(self.a.removePalindromeSub("baaaabb"), 2)

    def testPalCheck(self):
        self.assertFalse(self.a.isPal("aabbbba"))
        self.assertFalse(self.a.isPal("baaaabb"))

        self.assertTrue(self.a.isPal("abbbba"))
        

