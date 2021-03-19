#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Mar 19, 2021 14:49:44 AEDT
  @file        : swapNodes

"""
"""
Qs:
    - k from start and k from end - is list guaranteed to be of length k?
    - Range of list length?
    - Pointer manipulation only I presume?

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, x):
        if not self and not x: return True

        if not self or not x: return False

        return self.val == x.val and self.next == x.next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        ogHead = head
        curr1 = head
        curr2 = head
        length = 2

        # Need condition for new head
        if k != 1:
            # First pass, get pointer to node before target and length of list
            while curr1.next != None:
                if length == k:
                    head = curr1

                curr1 = curr1.next
                length += 1
        
        curr1 = head
        head = ogHead

        # Find index of swap node based on length
        if length - k != 1:
            target = length - k
            c = 2

            while c != target:
                curr2 = curr2.next
                c += 1
        
        # If one of the swapped nodes is the head,
        # we have to treat it differently
        if k == 1 or length - k == 1: 
            # Swap pointers if curr2 is the head
            if length - k < k: curr2 = curr1

            temp = curr2.next
            curr2.next = head
            temp.next = head.next
            
            head = curr2

            



            







        
