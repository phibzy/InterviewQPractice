#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Nov 02, 2020 11:12:55 AEDT
  @file        : balancedBTree

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        if not root: return True
        
        return self.rBal(root)[0]
    
    """
    TC: O(N)    - we visit each node of the tree once
    SC: O(logN) - we have at most logN frames on stack at one time,
                  due to DFS (i.e. height of tree)
    """
    
    def rBal(self, root):
        if not root: return (True, 0)

        # Check each recursive branch immediately after return
        # Drastically improves performance for heavily right-skewed trees
        lHeight = self.rBal(root.left)
        if not lHeight[0]: return (False, 0)
                
        rHeight = self.rBal(root.right)
        if not rHeight[0]: return (False, 0)
        
        diff = abs(lHeight[1] - rHeight[1])
        
        return ((diff <= 1), max(lHeight[1], rHeight[1]) + 1)
