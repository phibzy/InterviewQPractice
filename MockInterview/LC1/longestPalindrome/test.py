#!/usr/bin/python3

"""
   Test Cases:



"""

import unittest
from longestPal import Solution

class testLongestPal(unittest.TestCase):

   a = Solution()

   def testDefault1(self):
       self.assertEqual(self.a.longestPalindrome("abcd"), "a", "Fails default 1 case")

   def testDefault2(self):
       self.assertEqual(self.a.longestPalindrome("cbbd"), "bb", "Fails default 2 case")

   def testDefault3(self):
       self.assertEqual(self.a.longestPalindrome("b"), "b", "Fails default 3 case")




