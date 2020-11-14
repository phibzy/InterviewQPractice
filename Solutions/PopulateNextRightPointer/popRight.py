#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Saturday Nov 14, 2020 13:58:19 AEDT
  @file        : popRight

"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root):
        # Use level order traversal - with a queue
        # For each level, we make each node's next equal to 
        # the next node in the queue.
        # When we get to last node in each level, the next will equal None
        
        # TC: O(N) - we visit every node once
        # SC: O(W) - where W is max width of tree
        
        if not root: return root
        
        # Create queue and add root of tree to start traversal
        q = deque()
        q.append(root)
        
        
        while q:
            # newQ is the queue for the next level of nodes
            newQ = deque()
            
            # Go through each node in each level
            # Adding children to the next level q
            while q:
                n = q.popleft()

                # Check if we're at the last node in a given level
                # If we are, then our next pointer = None
                if q: n.next = q[0]
                else: n.next = None
                    
                # Don't need to check both since we either have 2 kids
                # or none.
                if n.left:
                    newQ.append(n.left)
                    newQ.append(n.right)
            
            # load up the next level of nodes!
            q = newQ
        
        return root
