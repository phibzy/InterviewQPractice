#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from shortestPath import Solution

class test(unittest.TestCase):

    a = Solution()

    def testBasicPath(self):
        easyGrid = [[0,0],[0,0]]

        self.assertEqual(self.a.shortestPathBinaryMatrix([[0]]), 1)
        self.assertEqual(self.a.shortestPathBinaryMatrix(easyGrid), 2)
        self.assertEqual(self.a.shortestPathBinaryMatrix([[0,1,1,1],[0,0,0,0]]),4)
        self.assertEqual(self.a.shortestPathBinaryMatrix([[0,1,0,0,0],
                                                          [0,1,0,1,0],
                                                          [0,1,0,1,0],
                                                          [0,0,0,1,0]]), 10)
        self.assertEqual(self.a.shortestPathBinaryMatrix([[0,1,1,0,0,1],
                                                          [0,1,0,1,1,0],
                                                          [0,1,1,0,1,0],
                                                          [0,0,0,0,1,0]]), 12)

    def testNoPathGrids(self):
        self.assertEqual(self.a.shortestPathBinaryMatrix([[1]]), -1)
        self.assertEqual(self.a.shortestPathBinaryMatrix([[1,0,0,0],[0,0,0,0]]), -1)
        self.assertEqual(self.a.shortestPathBinaryMatrix([[0,0,0,0],[0,0,0,1]]), -1)
        self.assertEqual(self.a.shortestPathBinaryMatrix([[0,1,1,1],[0,0,0,1]]), -1)

