#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Feb 04, 2021 12:13:21 AEDT
  @file        : trimBST

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # None case
        if not root: return root
        
        # Cases where we need a new root
        if root.val < low:
            root = self.trimBST(root.right, low, high)
            
        elif root.val > high:
            root = self.trimBST(root.left, low, high)
            
        # Otherwise it's in range, build rest of tree through traversal
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        
        return root
