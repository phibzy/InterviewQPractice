#!/usr/bin/python3

"""
   Test Cases:



"""

import unittest
from numNodesInSubtree import Solution

class testNumNodes(unittest.TestCase):
   a = Solution()

   def test7(self):
       self.assertEqual(self.a.countSubTrees(7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], "aaabaaa"), [6,5,4,1,3,2,1], "Fails example case 7")

   def test4(self):
       self.assertEqual(self.a.countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed"), [1,1,2,1], "Fails example case 4")

