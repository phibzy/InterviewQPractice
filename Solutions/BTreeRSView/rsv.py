#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Feb 08, 2021 14:04:59 AEDT
  @file        : rsv

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # DFS, keep track of level, go down left side first
        # If index not in list, add to list
        # Otherwise overwrite current value
        rhView = list()
        
        # DFS tree
        self.DFS(root, 0, rhView)
        
        return rhView
        
    #TC: O(N) - have to visit all nodes
    #SC: O(N) - worst case completely skewed tree
    def DFS(self, root, level, rhView):
        if not root: return
        
        if level >= len(rhView):
            rhView.append(root.val)
        
        else:
            rhView[level] = root.val
            
        self.DFS(root.left, level + 1, rhView)
        self.DFS(root.right, level + 1, rhView)
