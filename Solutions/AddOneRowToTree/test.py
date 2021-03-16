#!/usr/bin/python3

"""
    Test Cases:
        - Insert at root
        - Insert 1 after root
        - Insert middle of decent sized tree
        - Insert at level where there's only one or two applicable nodes
        - Inert at end of tree

"""

import unittest
from addRow import Solution, TreeNode

from collections import deque

class test(unittest.TestCase):

    a = Solution()

    def testHelper(self):
        self.assertEqual(list2Tree([1,2,3]), TreeNode(1, TreeNode(2), TreeNode(3)))
        self.assertEqual(list2Tree([1,None,2,3]), TreeNode(1, None, TreeNode(2, TreeNode(3))))
        self.assertEqual(list2Tree([1,2,3,4,5,6,None,7]), TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, TreeNode(6))))
        self.assertEqual(list2Tree([1,2,None,4,None,6,None,7]), TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6, TreeNode(7))))))

        self.assertEqual(list2Tree([1,2,3,-10,-10,-10,-10,4,None,None,5, 6,None, None, 7]), TreeNode(1, TreeNode(2, TreeNode(-10, TreeNode(4)), TreeNode(-10, None, TreeNode(5))),  TreeNode(3, TreeNode(-10, TreeNode(6)), TreeNode(-10, None, TreeNode(7)))))

    def testBasic(self):
        self.assertEqual(self.a.addOneRow(list2Tree([1]), 2, 2), list2Tree([1,2,2]))
        self.assertEqual(self.a.addOneRow(list2Tree([1]), 2, 1), list2Tree([2,1]))
        self.assertEqual(self.a.addOneRow(list2Tree([1]), 2, 1), list2Tree([2,1]))
        self.assertEqual(self.a.addOneRow(list2Tree([1,2,3,4,5,6,7]), -10, 3), list2Tree([1,2,3,-10,-10,-10,-10,4,None,None,5, 6,None, None, 7]))

    def testAvg(self):
        self.assertEqual(self.a.addOneRow(list2Tree([1,4,6,None,7,9,None,8,12,None,-3]), -10, 3), \
                list2Tree([1,4,6,-10,-10,-10,-10,None,None,None,7,9,None,None,None,8,12,None,-3]))

# Helper function to convert list to tree
def list2Tree(l):
    if not l: return None

    # Use q method we are familiar with
    head = TreeNode(l[0])
    
    q = deque()
    q.append(head)

    i = 1
    # Remember NULL cases
    while i < len(l):
        parent = q.popleft()
        
        if l[i]: parent.left = TreeNode(l[i])
        i += 1

        if i < len(l) and l[i]: parent.right = TreeNode(l[i])
        i += 1

        # Add children to q if they're not null
        if parent.left: q.append(parent.left)
        if parent.right: q.append(parent.right)
    
    return head

