#!/usr/bin/python3

"""
Given a BTree, return its max depth

One node is depth 1, null tree is depth 0

Very easy, didn't even bother with testing

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))
