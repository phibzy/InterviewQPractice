#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Nov 24, 2020 10:04:16 AEDT
  @file        : houseRobberIII

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(N) - we visit each node exactly once
# SC: O(N) - Tree is completely skewed and we have N calls on the stack

class Solution:
    def rob(self, root):
        return max(self.rRob(root))
    
    # Will return tuple containing
    # max sum of subtree that includes root,
    # and max sum that doesn't include root

    # First element of returned tuple will include root, second won't
    def rRob(self, root):
        # Base case for null
        if not root: return (0, 0)

        leftSums = self.rRob(root.left)
        rightSums = self.rRob(root.right)

        # If root is included, then maxSum must not include
        # the root's immediate children - so we take their maxSums that
        # do not include themselves
        maxWithRoot = root.val + leftSums[1] + rightSums[1]

        # if the root isn't included, then we can take EITHER the maxSum
        # including a child OR the max sum excluding a child.
        # Important to note that we can take differnt options for each child
        maxWithoutRoot = max(leftSums) + max(rightSums)

        return (maxWithRoot, maxWithoutRoot)

