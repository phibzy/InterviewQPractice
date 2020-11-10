#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Nov 10, 2020 12:48:31 AEDT
  @file        : maxDiffAncestor

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity:  O(N) - we have to visit every node in the tree
# Space Complexity: O(N) - worst case we have a completely skewed tree and N stack frames
class Solution:
    def maxAncestorDiff(self, root):
        # Will always have at least 2 nodes
        # so we don't need to fret about equal max/min in first recursive call
        return self.rMaxDiff(root, -1, 10**5)
        
    def rMaxDiff(self, root, maxVal, minVal):
        # If null, just return whatever maxV is currently
        if not root: return (maxVal - minVal)
        
        # Set new maxes/mins
        # It's okay if they're equal, that just means we have duplicates
        # somewhere in the path (or it's the first recursive call)
        maxVal = max(maxVal, root.val)
        minVal = min(minVal, root.val)
        
        left  = self.rMaxDiff(root.left, maxVal, minVal)
        right = self.rMaxDiff(root.right, maxVal, minVal)
       
        # return max V for each subtree
        return max(left, right)
