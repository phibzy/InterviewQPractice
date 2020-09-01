#!/usr/bin/python3

"""
   Test Cases:



"""

import unittest
from removeDuplicates import Solution

class testRemoveDuplicates(unittest.TestCase):

    a = Solution()

    def testDefault1(self):
        self.assertEqual(self.a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5, "Fails default case")

    def testDefault2(self):
        self.assertEqual(self.a.removeDuplicates([1,1,2]), 2, "Fails default case 2")
        
    def testCustom(self):
        self.assertEqual(self.a.removeDuplicates([1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,5,5,6,7,7,7,7,8,9,9,10]), 10, "Fails custom case")

    def testNoRepeats(self):
        self.assertEqual(self.a.removeDuplicates([1,2,3,4,5]), 5, "Fails no repetitions case")
