#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Jan 03, 2021 10:03:05 AEDT
  @file        : nodeClone

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Will solve for followup straight off the bat
    # Since we're looking for same reference in original tree,
    # we will traverse both trees at the same time
    # until we find the target TreeNode in the original tree.
    # We will then return the corresponding TreeNode at that point
    # in the cloned tree.

    # This will work even in a tree of duplicates because instead
    # of checking whether the value of a node is equal to the target,
    # we are checking if the target node is equal to the current node
    # in the original tree.
    def getTargetCopy(self, original, cloned, target):
        # base case - root is target
        # return wherever we are in the cloned tree
        if original == target:
            return cloned

        # null case if branch doesn't have target
        if not original: return None

        # Otherwise, traverse tree and return 
        # whichever subcall contains the target
        return self.getTargetCopy(original.left, cloned.left, target) or \
                self.getTargetCopy(original.right, cloned.right, target)





