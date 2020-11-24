#!/usr/bin/python3

"""
    Test Cases:
        - Default cases (i.e. basic alternating level cases)
        - Non-alternating level cases

"""

import unittest
from collections import deque
from houseRobberIII import Solution, TreeNode

class test(unittest.TestCase):

    a = Solution()

    def testDefault1(self):
        self.assertEqual(self.a.rob(list2Tree([3,2,3,None,3,None,1])), 7)

    def testDefault2(self):
        self.assertEqual(self.a.rob(list2Tree([3,4,5,1,3,None,1])), 9)

    def testSize1(self):
        self.assertEqual(self.a.rob(list2Tree([3])), 3)

    def testNonAlt1(self):
        self.assertEqual(self.a.rob(list2Tree([6,1,1,2,1,None,None,None,None,10])), 18)

    def testNonAlt2(self):
        self.assertEqual(self.a.rob(list2Tree([5,2,2,1,4,3,5,9,2,1,None,None,3,None,8])), 31)

    def testNonAlt3(self):
        self.assertEqual(self.a.rob(list2Tree([5,2,2,3,1,4,5,4,7,9,2,1,5,8,9,1,1,1,1,1,1,None,None,None,None,None,None,None,None,None,None,3,None,7,None,None,None,None,2])), 62)

    def testPickNChoose1(self):
        self.assertEqual(self.a.rob(list2Tree([3,4,7,2,4,1,1,None,None,None,None,None,None,None,2])), 15)

    def testPickNChoose2(self):
        self.assertEqual(self.a.rob(list2Tree([3,4,7,2,4,1,1,None,None,None,None,3,2,None,2,8])), 25)



# Helper function for creating trees so testing is easier
def list2Tree(l):
    if not l or l[0] is None: return None

    q = deque()
    root = TreeNode(l[0])
    q.append(root)

    i = 1
    while i < len(l):
        n = q.popleft()

        if l[i]:
            n.left = TreeNode(l[i])
            q.append(n.left)

        i += 1

        if i < len(l) and l[i]:
            n.right = TreeNode(l[i])
            q.append(n.right)

        i += 1

    return root




