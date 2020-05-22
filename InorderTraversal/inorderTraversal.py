#!/usr/bin/python3

"""
Given a root to a BTree

Return list of values in inorder traversal order

Note: No initial recursive solution or tests since I did this one straight on leetcode

"""


class Solution:
    def inorderTraversal(self, root):
        if root is None: return []
        retList = list()
       
        s = list()
        
        s.append((root,False))
        
        while s:
            node, b = s.pop()
            if node is None: continue
            
            if node.left is None or b == True:
                retList.append(node.val)
                s.append((node.right, False))
            
            elif b == False:
                s.append((node, True))
                s.append((node.left,False))
        
        return retList
        
