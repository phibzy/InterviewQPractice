#!/usr/bin/python3

"""
    Test Cases:
        - One level with one element
        - Many levels with one element
        - Perfectly balanced tree
        - Float and int result values
"""

import unittest
from collections import deque
from averageLevels import Solution, TreeNode

class test(unittest.TestCase):

    a = Solution()

    def testHelper(self):
        self.assertEqual(list2Tree([]), None)
        self.assertEqual(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)))
        self.assertEqual(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
        self.assertEqual(list2Tree([1,2,3,4]), TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)))
        self.assertEqual(list2Tree([1,2,None,3,4]), TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), None))

    def testActual(self):
        self.assertEqual(self.a.averageOfLevels(list2Tree([1])), [1])
        self.assertEqual(self.a.averageOfLevels(list2Tree([1,2,None,3,None,4,None,5,None])), [1,2,3,4,5])
        self.assertEqual(self.a.averageOfLevels(list2Tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])), [1,2.5,5.5,11.5])



# Helper for converting list to tree structure
def list2Tree(l):
    if not l: return None

    head = TreeNode(l[0])

    nextQ = deque()
    nextQ.append(head)

    i = 1
    while i < len(l):
        parent = nextQ.popleft()

        if l[i]:
            parent.left = TreeNode(l[i])
            nextQ.append(parent.left)

        i += 1

        if i < len(l) and l[i]: 
            parent.right = TreeNode(l[i])
            nextQ.append(parent.right)
        
        i += 1

    return head

