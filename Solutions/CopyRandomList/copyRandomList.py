#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Feb 11, 2021 11:27:34 AEDT
  @file        : copyRandomList

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
One solution:

Two passes, construct normal deep copy list first
Map old node to new copy of that node

"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Empty list case
        if not head: return head
        
        # Otherwise, copy the head first
        # Only set the value since we'll be making new pointers
        newHead = Node(head.val)
        randomMap = dict()
        
        # Keep track of start of new list, since we need
        # to return head of new list at end
        newStart = newHead
        
        # Map old Head to newHead
        randomMap[head] = newHead
                
        # New version - one pass
        # Same as before, but we create random pointer nodes on
        # fly as well
        
        # Only main difference is we check whether next/random nodes are in map
        # before we make copies of original nodes
        
        while head.next:
            # Start with next node
            # Check if new deep copy of node has been made
            # If not, create it and map original node reference to it
            # Then set next pointer of newHead to mapped value of head.next
            if not head.next in randomMap:
                randomMap[head.next] = Node(head.next.val)

            newHead.next = randomMap[head.next]
            
            # Repeat for random too
            if head.random:
                if not head.random in randomMap:
                    randomMap[head.random] = Node(head.random.val)
                
                newHead.random = randomMap[head.random]
            
            # Then iterate through list
            head = head.next
            newHead = newHead.next
            
        # Handle last node random too
        # If it's not null, it HAS to be in map by now.
        # Also handles length 1 case with random pointing to itself
        if head.random:
            newHead.random = randomMap[head.random]
        
        
        
        
        
        """
        # Construct new list without random pointers
        # Then create map hashing old refs as key to
        # new refs as value
        while head.next:
            newHead.next = Node(head.next.val)
            newHead = newHead.next
            head = head.next
            randomMap[head] = newHead
        
        # Go through again, this time setting random pointers too
        head = start
        newHead = newStart
        
        while head:
            # If randomm in original list isn't null,
            # set random of newlist node to equivalent newlist node
            # by using our beloved hashmap
            # Don't need condition for null since random is null by default
            if head.random:
                newHead.random = randomMap[head.random]
        
            head = head.next
            newHead = newHead.next
        """
            
        return newStart
