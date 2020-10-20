#!/usr/bin/python3

"""
   Test Cases:
     - Default
     - Empty tree
     - Tree with one node


"""

import unittest
from BTreeTilt import Solution, TreeNode

class testTilt(unittest.TestCase):

   a = Solution()

   def testDefault(self):
       self.assertEqual(self.a.findTilt(TreeNode(1, TreeNode(2), TreeNode(3))), 1, "Fails default case") 
    
   def testEmptyTree(self):
       self.assertEqual(self.a.findTilt(None), 0, "Fails empty tree case") 
       
   def testOneNodeTree(self):
       self.assertEqual(self.a.findTilt(1), 0, "Fails one node tree case") 
