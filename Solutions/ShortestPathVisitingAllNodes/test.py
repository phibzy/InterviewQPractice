#!/usr/bin/python3

"""
    Test Cases:
        - Completely connected graph to test TLE
        - Graphs with 1/2 nodes



"""

import unittest
from shortestPath import Solution 

class test(unittest.TestCase):
    
    a = Solution()

    def testDefault(self):
        self.assertEqual(self.a.shortestPathLength([[1,2,3],[0],[0],[0]]), 4)
        self.assertEqual(self.a.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]), 4)
        self.assertEqual(self.a.shortestPathLength([[2,3,7],[3,6],[0,4],[0,1,4,5],[3,7,2,6],[3],[4,1],[4,0]]), 7)
        self.assertEqual(self.a.shortestPathLength([[2,5,7],[2,4],[0,1],[5],[5,6,1],[4,10,8,0,3],[4,9],[0],[5],[6],[5]]), 13)

    def testSmallInput(self):
        self.assertEqual(self.a.shortestPathLength([]), 0)
        self.assertEqual(self.a.shortestPathLength([[]]), 0)
        self.assertEqual(self.a.shortestPathLength([[1],[0]]), 1)
