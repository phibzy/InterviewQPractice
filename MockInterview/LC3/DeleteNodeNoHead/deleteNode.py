#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Oct 22, 2020 12:49:44 AEDT
  @file        : deleteNode

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Since len(list) >= 2, and node is guaranteed not to be tail node
        We have only 2 cases: Case with only 2 elements, all the others
        
        """
        # First, make current node value equal to next node value
        node.val = node.next.val
        
        # Grab next node (which will be deleted), make current node's
        # next pointer equal to temp node's next pointer
        temp = node.next
        node.next = temp.next
        
        # Set temp's pointer to None, we're finished with it
        temp.next = None
