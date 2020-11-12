#!/usr/bin/python3

"""
   Test Cases:



"""
import unittest
from minHeight import Solution

class testMinHeightT(unittest.TestCase):

   a = Solution()
   def test1(self):
       self.assertEqual(self.a.findMinHeightTrees(4,[[1,0],[1,2],[1,3]]), [1], "Fails default case 1")

   def test2(self):
       self.assertEqual(self.a.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]), [3,4], "Fails default case 2")

   def test3(self):
       self.assertEqual(self.a.findMinHeightTrees(1,[]), [0], "Fails default case 3")

   def test4(self):
       self.assertEqual(self.a.findMinHeightTrees(2,[[0,1]]), [0,1], "Fails default case 4")

