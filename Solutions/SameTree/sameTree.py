#!/usr/bin/python3

"""
Given two binary trees, returns True if they are the same

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive solution - DFS
    def isSameTreeR(self, p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False

        if p.val == q.val:
            return self.isSameTreeR(p.left, q.left) and self.isSameTreeR(p.right, q.right)
         
        return False

    # Iterative solution
    def isSameTree(self, p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False

        # Don't use two queues, just use a queue of tuples instead
        pQ = list()
        qQ = list()

        pQ.append(p)
        qQ.append(q)

        while pQ and qQ:
            nextQ = qQ.pop(0)
            nextP = pQ.pop(0)
            
            if nextQ == nextP == None: continue
            if nextQ is None or nextP is None: return False
            
            if nextQ.val != nextP.val: return False

            qQ.append(nextQ.left)
            qQ.append(nextQ.right)

            pQ.append(nextP.left)
            pQ.append(nextP.right)

        return True

