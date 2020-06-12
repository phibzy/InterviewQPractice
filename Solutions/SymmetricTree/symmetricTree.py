#!/usr/bin/python3

"""
Given a BTree, check that it's right side mirrors its left

My Solution: Use two Qs, use level order traversal
             For one side check left branch first, the other right branch first

Time Complexity: O(N) - we visit every node exactly once

Space Complexity: O(W) - Where W is max width of tree
                       - Worst case perfectly balanced, bottom level has roughly N/2 nodes
                  Therefore O(N) Worst case


Other Solution: Use similar approach but with DFS
                Time Complexity: O(N)
                Space Complexity: Average case: O(logN)
                                  Worst case: O(N) (hollow tree)

"""





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
