#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Oct 20, 2020 16:20:25 AEDT
  @file        : BTreeTilt

"""


# Time Complexity: O(N), where N is number of nodes in tree
# Space Complexity: O(logN), max height of tree is logN
#                   Stack will only ever get logN high due to DFS


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root):
        if root is None: return 0
        
        return self.rTilt(root)[1]
        
        
    def rTilt(self, root):
        if root is None: return (0,0)
        
        l = self.rTilt(root.left)
        r = self.rTilt(root.right)
        
        tilt = abs(l[0] - r[0])
        
        # return total sum of all nodes including own val
        # THEN return sum of all tilts thus far + own tilt
        return (l[0] + r[0] + root.val, l[1] + r[1] + tilt)
        
