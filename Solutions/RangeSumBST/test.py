#!/usr/bin/python3

"""
    Test Cases:
        - No matching characters
        - Only one num in range
        - All numbers in range
        - Edge case where one of the next nodes isn't in range,
          but one of its kids is

"""

import unittest
from rangeSum import Solution, TreeNode
from collections import deque

class testRangeSum(unittest.TestCase):

    a = Solution()

    def testNoMatching(self):
        self.assertEqual(self.a.rangeSumBST(TreeNode(6), 8, 10), 0, "Fails no matching node case")

    def testOneNumInRange(self):
        self.assertEqual(self.a.rangeSumBST(list2Node([10,6,20,4,8,15,22,2,None,None,None,12,17,21,None]), 17, 17), 17, "Fails one node in range case")

    def testAllInRange(self):
        self.assertEqual(self.a.rangeSumBST(list2Node([10,6,20,3,7,12,21]), 1, 25), 79, "Fails all nodes in range case")

    def testEdgeKids(self):
        self.assertEqual(self.a.rangeSumBST(list2Node([10,5,15,3,7,None,18]), 7, 15), 32, "Fails kids edge case")

# Helper function so I can easily make test cases
def list2Node(l):
    if not l: return None

    q = deque()

    root = TreeNode(l[0])
    q.append(root)
    i = 1

    while q and i < len(l):
        n = q.popleft()
        if not n: continue

        new = None
        if l[i]: new = TreeNode(l[i])
        n.left = new
        q.append(n.left)
        i += 1

        if i < len(l):
            new = None
            if l[i]: new = TreeNode(l[i])
            n.right = new
            q.append(n.right)
            i += 1

    return root
