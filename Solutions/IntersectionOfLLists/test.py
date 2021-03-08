#!/usr/bin/python3

"""
    Test Cases:
        - Length 1 and 2 with intersection
        - No intersection
        - Average intersection case

"""

import unittest
from intersect import Solution, ListNode

class test(unittest.TestCase):

    a = Solution()

    def testHelper(self):
        self.assertEqual(convertToLList([1,2,3]), ListNode(1, ListNode(2, ListNode(3))))
        self.assertEqual(convertToLList([1]), ListNode(1))
        self.assertEqual(getLastNode(convertToLList([2,4,7,1])), ListNode(1))

    def test1and2(self):
        list1 = ListNode(3)
        list2 = ListNode(1, list1)

        self.assertEqual(self.a.getIntersectionNode(list1, list2), 3)

    def testNoInt(self):
        self.assertEqual(self.a.getIntersectionNode(convertToLList([1,4,6,2,8,5,4]), convertToLList([5,4,3,2,2,1])), 0)

    def testAverage(self):
        intersect = convertToLList([4,2,3,6,8])
        head1 = convertToLList([1,2,3,4,5,7,9000])
        end1  = getLastNode(head1)
        end1.next = intersect

        head2 = convertToLList([9,4,3,7,2,0,9])
        end2  = getLastNode(head2)
        end2.next = intersect

        self.assertEqual(self.a.getIntersectionNode(head1, head2), 4)

def convertToLList(l):
    head = ListNode(l[0])
    curr = head

    for v in l[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head

def getLastNode(l):
    curr = l

    while curr.next:
        curr = curr.next

    return curr

