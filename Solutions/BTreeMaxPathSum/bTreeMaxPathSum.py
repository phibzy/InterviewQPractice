#!/usr/bin/python3

"""
Given a non-empty Btree, find the maximum sum of path in tree

A path is simply any path linking two nodes in the tree

Path length >= 1

TODO: Iterative solution

"""




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        result = root.val
        leftGain = rightGain = 0
        leftSum = rightSum = float('-inf')
        
        if root.left:
            leftSum, leftGain = self.rMaxPath(root.left)
        
        if root.right:
            rightSum, rightGain = self.rMaxPath(root.right)
            
        maxGain = max(leftGain, rightGain)    
        pyramidSum = root.val + rightGain + leftGain
        
        result = max(result, pyramidSum, leftSum, rightSum,
                     root.val + maxGain)
        
        return result
    
    def rMaxPath(self, root):
        result = root.val
        maxGain = root.val
        rightSum = leftSum = float('-inf')
        rightGain = leftGain = 0
        
        if root.left:
            leftSum, leftGain = self.rMaxPath(root.left)
        
        if root.right:
            rightSum, rightGain = self.rMaxPath(root.right)
            
        maxGain = max(maxGain, root.val + leftGain, root.val + rightGain)    
        pyramidSum = root.val + rightGain + leftGain
        
        result = max(result, pyramidSum, leftSum, rightSum,
                     maxGain)
        
        return result, maxGain
        
