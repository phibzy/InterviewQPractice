#!/usr/bin/python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        # Strat - 2 Queues doing BFS, one on left checks left branch first, other right branch first
        if not root: return True
        leftQ = list()
        rightQ = list()
        
        leftQ.append(root.left)
        rightQ.append(root.right)
        
        while leftQ and rightQ:
            left = leftQ.pop()
            right = rightQ.pop()
            
            if not left or not right:
                if left != right: return False
                continue
                
            if left.val != right.val: return False
        
            leftQ.append(left.left)
            leftQ.append(left.right)
            
            rightQ.append(right.right)
            rightQ.append(right.left)
        
        return True
