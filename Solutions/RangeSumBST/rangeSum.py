#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Nov 16, 2020 10:10:20 AEDT
  @file        : rangeSum

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(N) - Worst case range encompasses all nodes in tree
#            and we have to visit all of them

# SC: O(H) - Where H is height of tree, since we have at most that
#            many calls on the stack. Avg. case O(logN) for relatively
#            balanced trees, but worst case O(N) for completely skewed tree 


class Solution:
    def rangeSumBST(self, root, low, high):
        totalSum = 0
        # Base case: return nothing if node is null
        if not root: return totalSum
        
        # Skip current node + left subtree if value too low
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # Skip current node + right subtree if value too high
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # Otherwise current node value lies in range 
        totalSum += root.val

        # Check if there's any more possible values to find
        if high > root.val: totalSum += self.rangeSumBST(root.right, low, high)
        if low  < root.val: totalSum += self.rangeSumBST(root.left, low, high)

        return totalSum


