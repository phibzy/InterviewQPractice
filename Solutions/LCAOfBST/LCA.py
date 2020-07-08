#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Jul 08, 2020 11:45:20 AEST
  @file        : LCA

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                  
        """
        p, q are guaranteed to be in the tree
        
        Cases:
        
            - Root is target
            - Direct ancestors are p and q
            - Both targets in one side of tree
            - Targets in different sides of tree
            - Be aware of null cases - since p/q guaranteed to be in tree this won't be a worry
            
        """
        
        
        # If p and q sit in different subtrees of current node, LCA is current node
        # Likewise if current node is equal to either p or q
        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root
        
        # If they're less than current node they are in the left subtree somewhere
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return self.lowestCommonAncestor(root.right, p, q)
        
