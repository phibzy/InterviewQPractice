#!/usr/bin/python3

"""
   Test Cases:



"""

import unittest
from maxDiffAncestor import Solution, TreeNode

class testMaxDiff(unittest.TestCase):

   a = Solution()

   def testDefault1(self):
       self.assertEqual(self.a.maxAncestorDiff(listToTree([8,3,10,1,6,None,14,None,None,4,7,13])), 7, "Fails 1st default case")

   def testAllEqual(self):
       self.assertEqual(self.a.maxAncestorDiff(listToTree([42,42,42,42,42,42,42])), 0, "Fails all equal case")

   def testMaxVOnLastCall(self):
       self.assertEqual(self.a.maxAncestorDiff(listToTree([42,42,42,42,42,42,100])), 58, "Fails last call case")

# Helping function for turning list input into tree
def listToTree(l):

    # Use queue
    # Next time remember to use a deque pls
    s = list()

    root = TreeNode(l[0])

    s.append(root)
    del l[0]

    while l:
        nextN = s[0]
        del s[0]
        
        if l[0] is None: 
            left = None
        else:
            left = TreeNode(l[0])

        del l[0]

        if (not l) or (l[0] is None):
            right = None
            if l: del l[0]

        else:
            right = TreeNode(l[0])
            del l[0]

        nextN.left = left 
        nextN.right = right

        if left: s.append(left)
        if right: s.append(right)

    return root







