#!/usr/bin/python3

"""
    Test Cases:
        - k == n == 1
        - Crisscross case (i.e. n-k < k)
        - Odd/Even lengths

"""

import unittest
from swapNodes import Solution, ListNode

class test(unittest.TestCase):

    a = Solution()

    def testHelper(self):
        self.assertEqual(list2Node([1,2,3,4,5]), ListNode(1, ListNode(2, ListNode(3, ListNode(4, (ListNode(5)))))))
        self.assertEqual(list2Node([1]), ListNode(1))

    def testSwapNodes(self):
        self.assertEqual(self.a.swapNodes(list2Node([1]), 1), list2Node([1]))
        self.assertEqual(self.a.swapNodes(list2Node([1,2,3]), 1), list2Node([3,2,1]))
        self.assertEqual(self.a.swapNodes(list2Node([1,2,3]), 3), list2Node([3,2,1]))
        self.assertEqual(self.a.swapNodes(list2Node([1,2,3]), 2), list2Node([1,2,3]))

def list2Node(l):
    if not l: return None

    head = ListNode(l[0])
    curr = head

    for v in l[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head

