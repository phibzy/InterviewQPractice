#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Nov 09, 2020 14:37:24 AEDT
  @file        : BTreeTilt2

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Time Complexity: O(N) - we visit every node once
Space Complexity: O(N) - Worst case we have a completely skewed tree,
                         ending up with N stack frames on stack

Challenge: How would you do it iteratively?

"""

class Solution:
    def findTilt(self, root):
        # Can have empty trees
        if not root: return 0

        return self.rTilt(root)[0]

    def rTilt(self, root):
        # Base case: return (0,0) if None
        if not root: return (0,0)

        leftTilt, leftSum =   self.rTilt(root.left)
        rightTilt, rightSum = self.rTilt(root.right)

        tilt = abs(leftSum - rightSum)

        return (leftTilt + rightTilt + tilt ,leftSum + rightSum + root.val)

