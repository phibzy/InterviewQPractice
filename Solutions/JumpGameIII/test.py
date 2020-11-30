#!/usr/bin/python3

"""
    Test Cases:
        - Start index is 0
        - Extending over array failures (both ways, single way)
        - Path to 0 exists
        - Multiple 0 paths
        - No paths

"""

import unittest
from jumpGameIII import Solution

class test(unittest.TestCase):

    a = Solution()

    def testStart0(self):
        self.assertTrue(self.a.canReach([1,2,0,4,5],2))

    def testPathExists(self):
        self.assertTrue(self.a.canReach([6,2,2,4,5,0,1,2],2))

    def testNoPathExists(self):
        self.assertFalse(self.a.canReach([6,2,2,4,5,0,1,3],3))

    # NGL this one was easy, so I didn't bother with the other test cases lol
