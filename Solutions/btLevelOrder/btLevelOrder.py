#!/usr/bin/python3

"""
Takes in list that is a BTree

Returns list of list representing level order
of nodes in tree e.g.

    3
   / \
  9  20
     / \
    15  7

Comes out as:

[
    [3],
    [9,20],
    [15,7]
]

Test cases:
    - Normy 3 level tree balanced
    - Tree 3 levels deep all RHS nodes
    - Tree 3 levels deep all LHS nodes
    - Empty tree
    - One node

"""

#definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def levelOrder(self, root):
        retList = list()
        if root == None or root.val == None: return retList

        q = list()
        q.append((root, 0))

        while q:
            node, lev = q.pop(0)
            
            # if level doesn't exist in retList, make new empty list for all nodes in that level
            if not lev < len(retList):
                retList.append([node.val])
            else:
                retList[lev].append(node.val)

            if node.left is not None: q.append((node.left, lev+1))
            if node.right is not None: q.append((node.right, lev+1))

        return retList

