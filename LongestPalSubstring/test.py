#!/usr/bin/python3

from longestPalSubstring import longestPalSubstring
import unittest

"""
Test Cases:
    Empty string
    string of length 1
    Palindrome is the whole string
    Palindrome at start of string
    Palindrome at end of string
    Palindrome of even length


"""


class testSubstring (unittest.TestCase):
    
    def test0Elements(self):
        self.assertEqual(longestPalSubstring(''), '', 'Error - Fails single character case')

    def test1Element(self):
        self.assertEqual(longestPalSubstring('a'), 'a', 'Error - Fails single character case')

    def testWholeStringPalindrome(self):
        self.assertEqual(longestPalSubstring('abcdefgbababgfedcba'),'abcdefgbababgfedcba', 'Error - Fails whole string palindrome case')
    def testEvenPalindrome(self):
        self.assertEqual(longestPalSubstring("aabbaa"), "aabbaa", "Error - Fails even length case")
    
    def testEvenLength2(self):
        self.assertEqual(longestPalSubstring("bb"), "bb", "Error - Fails even length (length 2) case")




    


