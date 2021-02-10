#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Feb 11, 2021 10:37:01 AEDT
  @file        : bst2greater

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Go as far right as possible
    # The use this total var to keep track of cumulative sum
    # starting with rightmost element
    # Do it this way to preserve sum when recursing down left branches of tree
    total = 0
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        
        self.updateBST(root)
        
        return root
    
    def updateBST(self, root):
        # Base case: Null
        if not root: return
        
        # Go as far right as possible
        self.updateBST(root.right)
        
        # Update current node total with sum of everything greater
        # Then update cumulative sum again before recursing left and repeating
        self.total += root.val
        root.val = self.total
        
        # Repeat on left side too
        self.updateBST(root.left)
