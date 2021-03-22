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

    def __str__(self):
        output = "--> "
        curr = self

        while curr:
            output += f"{curr.val} --> "
            curr = curr.next

        return output

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        ogHead = head
        curr1 = head
        curr2 = head
        length = 2

        # Need condition for new head
        # First pass, get pointer to node before target and length of list
        while curr1.next != None:
            if length == k:
                head = curr1

            curr1 = curr1.next
            length += 1
        
        curr1 = ogHead if k == 1 else head
        head = ogHead

        # If they're the same node we don't need to change list
        if k == length - k: return ogHead

        # Find index of swap node based on length
        if length - k != 1:
            target = length - k
            c = 2

            while c != target:
                curr2 = curr2.next
                c += 1

        # Swap pointers to preserve curr1/curr2 order
        if length - k < k: 
            curr2, curr1 = curr1, curr2

        if k == 1 or length - k == 1:
            curr1.val, curr2.next.val = curr2.next.val, curr1.val

        else:
            curr1.next.val, curr2.next.val = curr2.next.val, curr1.next.val

        return ogHead

        # # Swap pointers to preserve curr1/curr2 order
        # if length - k < k: 
            # curr2, curr1 = curr1, curr2

        # # If one of the swapped nodes is the head,
        # # we have to treat it differently
        # if k == 1 or length - k == 1: 

            # temp = curr2.next
            # curr2.next = head
            # temp.next = head.next
            # head = temp 

        # else:
            # # Need to preserve tails too
            # temp = curr2.next
            # tempTail = curr2.next.next

            
            # curr1Tail = curr1.next.next
            # curr2.next = curr1.next
            # curr1.next.next = tempTail

            


            


            
