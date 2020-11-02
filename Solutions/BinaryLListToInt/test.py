#!/usr/bin/python3

"""
   Test Cases:
        - 0 (many 0's?)
        - 1
        - Random binary number
        - All 1's
        - 30 nodes


"""

import unittest
from binToInt import Solution, ListNode

class test(unittest.TestCase):

   a = Solution()

   def test1(self):
       self.assertEqual(self.a.getDecimalValue(ListNode(1)), 1, "Fails 1 case")

   def test0(self):
       self.assertEqual(self.a.getDecimalValue(ListNode(0)), 0, "Fails 0 case")

   def test23(self):
       self.assertEqual(self.a.getDecimalValue(ListNode(1, ListNode(0, ListNode(1, ListNode(1, ListNode(1)))))), 23, "Fails 23 case")

   def test16(self):
       self.assertEqual(self.a.getDecimalValue(ListNode(1, ListNode(0, ListNode(0, ListNode(0, ListNode(0)))))), 16, "Fails 16 case")

   def test30Nodes(self):
       self.assertEqual(self.a.getDecimalValue(ListNode(1, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(0, ListNode(1, ListNode(0, ListNode(1, ListNode(1, ListNode(0, ListNode(1, ListNode(1, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(0, ListNode(1, ListNode(0, ListNode(1, ListNode(1, ListNode(0, ListNode(1))))))))))))))))))))))))))))))), 567722925, "Fails 30 nodes case")

