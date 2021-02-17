#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from isGraphBipartite import Solution

class test(unittest.TestCase):

    a = Solution()

    def testFail(self):
        self.assertFalse(self.a.isBipartite([[1,2], [0,2],[0,1]]))
        self.assertFalse(self.a.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))

    def testPass(self):
        self.assertTrue(self.a.isBipartite([[1,3], [0,2],[1,3], [2,0], []]))
        self.assertTrue(self.a.isBipartite([[1], [0,2], [1,3,5], [2,4], [3], [2,6], [5], [8], [7]]))
        self.assertTrue(self.a.isBipartite([[1,3],[0,2],[1,3],[0,2]]))


