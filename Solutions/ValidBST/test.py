#!/usr/bin/python3

"""
Test Cases:
    - Null node
    - One node
    - Valid simple BST
    - Invalid simple BST
    - Invalid BST due to element on right of root being less than original root
    - Inverse of previous test case
    - Negative number case
    - Node val equal to root

"""

import unittest
from validBST import Solution, TreeNode

class testValidBST(unittest.TestCase):

    a = Solution()

    def testNoneRoot(self):
        self.assertTrue(self.a.isValidBST(None), "Error - fails None root case")

    def testOneNode(self):
        self.assertTrue(self.a.isValidBST(TreeNode(42)), "Error - Fails one node case")

    def testValidSimpleTree(self):
        self.assertTrue(self.a.isValidBST(TreeNode(42, TreeNode(20), TreeNode(60, TreeNode(50), TreeNode(77)))), "Error - Fails simple valid tree case")

    def testInvalidSimpleTree(self):
        self.assertFalse(self.a.isValidBST(TreeNode(42, TreeNode(20), TreeNode(60, TreeNode(64), TreeNode(77)))), "Error - Fails simple invalid tree case")

    def testInvalidRightNotAdhering(self):
        self.assertFalse(self.a.isValidBST(TreeNode(42, TreeNode(20), TreeNode(60, TreeNode(36), TreeNode(77)))), "Error - Fails invalid right not adhering case")

    def testInvalidLeftNotAdhering(self):
        self.assertFalse(self.a.isValidBST(TreeNode(42, TreeNode(20, TreeNode(10, None, TreeNode(43)), TreeNode(44)), TreeNode(60, TreeNode(43), TreeNode(77)))), "Error - Fails invalid left not adhering case")
