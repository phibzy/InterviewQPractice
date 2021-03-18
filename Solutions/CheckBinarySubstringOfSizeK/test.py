#!/usr/bin/python3

"""
    Test Cases:
        - k > s.length
        - True cases:
            - k == 1
            - Some random k
        
        - False cases:
            - s.length == 1
            - String with characters all the same
            - One combo substring off being true



"""

import unittest
from checkBinary import Solution

class testBinarySubstringK(unittest.TestCase):
    
    a = Solution()

    def testBasic(self):
        self.assertFalse(self.a.hasAllCodes("010101", 10))
        self.assertFalse(self.a.hasAllCodes("0", 1))
        self.assertFalse(self.a.hasAllCodes("000000000000000000000000000000000000000", 4))
        self.assertFalse(self.a.hasAllCodes("0111000111", 3))

        self.assertTrue(self.a.hasAllCodes("01", 1))
        self.assertTrue(self.a.hasAllCodes("01011000111", 3))


