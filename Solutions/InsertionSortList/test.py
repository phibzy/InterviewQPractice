#!/usr/bin/python3

"""
   Test Cases:

       - Empty List
       - 1 Element
       - 2 Elements
       - Descending order list
       - Normal case
       - Already sorted list

"""

import unittest
from insertionSort import Solution, ListNode

class testISort(unittest.TestCase):

   a = Solution()
    
   def testEmpty(self):
       self.assertEqual(self.a.insertionSortList(None), None, "Fails None case")

   def testOne(self):
       self.assertEqual(self.a.insertionSortList(ListNode(9)), ListNode(9), "Fails 1 Element case")

   def testTwo(self):
       self.assertEqual(self.a.insertionSortList(ListNode(9, ListNode(4))), ListNode(4, ListNode(9)), "Fails 2 Element case")

   def testDescending(self):
       self.assertEqual(self.a.insertionSortList(ListNode(9, ListNode(8, ListNode(7, ListNode(6, ListNode(5, ListNode(4))))))), ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))), "Fails descending order case")

   def testAscending(self):
       self.assertEqual(self.a.insertionSortList(ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9))))))), ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))), "Fails already sorted case")


