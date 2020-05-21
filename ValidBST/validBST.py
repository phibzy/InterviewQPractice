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

        if (root.left is None or root.left.val < root.val) and \
                (root.right is None or root.right.val > root.val) and \
                ((minimum is None or root.val > minimum) and (maximum is None or root.val < maximum)):
                return ((self.rValid(root.left, minimum, root.val)) and (self.rValid(root.right, root.val, maximum)))

        return False

    def isValidBST(self, root):
        if root is None: return True

        if (root.left is None or root.left.val < root.val) and \
            (root.right is None or root.right.val > root.val):
                return (self.rValid(root.left, None, root.val) and self.rValid(root.right, root.val, None))

        return False

