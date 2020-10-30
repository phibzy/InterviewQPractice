#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Oct 30, 2020 17:53:04 AEDT
  @file        : listCycle

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        
        # Use two pointers, make one iterate through list twice as fast
        # If there is a cycle, they will eventually meet
        
        #TC: O(N) - Length of the list
        #SC: O(1) - We only use two pointers for every output size
        
        if not (head and head.next): return False
        
        fastPointer = head.next.next
        
        # Checking fastPointer.next saves condition checks
        while (head and fastPointer):
            if head == fastPointer:
                return True
            
            if fastPointer.next is None: break
                     
            head = head.next
            fastPointer = fastPointer.next.next
        
        return False
