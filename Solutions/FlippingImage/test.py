#!/usr/bin/python3

"""
   Test Cases:



"""

import unittest
from flipImage import Solution

class testFlipImage(unittest.TestCase):

   a = Solution()

   def test1x1(self):
       self.assertEqual(self.a.flipAndInvertImage([[1]]), [[0]], "Fails 1x1 case")

   def test2x2(self):
       self.assertEqual(self.a.flipAndInvertImage([[1,0], [0,1]]), [[1,0],[0,1]], "Fails 2x2 case")
   
   def testDefaul1(self):
       self.assertEqual(self.a.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]), [[1,0,0],[0,1,0],[1,1,1]], "Fails default 3x3 case")

   def testDefault2(self):
       self.assertEqual(self.a.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]), [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]], "Fails default 3x3 case")
