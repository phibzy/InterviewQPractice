#!/usr/bin/python3

"""
Given a BST root node, checks if it is a valid BST

Returns True if so, False if not

"""
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rValid(self, root, minimum, maximum):
        if root is None: return True

        if (root.left is not None and root.left.val >= root.val): return False
        if (root.right is not None and root.right.val <= root.val): return False
        if (minimum is not None and root.val <= minimum): return False
        if (maximum is not None and root.val >= maximum): return False

        return ((self.rValid(root.left, minimum, root.val)) and (self.rValid(root.right, root.val, maximum)))

    def isValidBST(self, root):
        return self.rValid(root, None, None)
