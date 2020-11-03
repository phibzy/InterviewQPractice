#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Nov 03, 2020 10:56:36 AEDT
  @file        : insertionSort

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Overloaded equals operator for tests
    def __eq__(self, n):
        head = self
        while head and n:
            if head.val != n.val:
                return False

            head = head.next
            n = n.next

        return head == n

class Solution:
    def insertionSortList(self, head):
        if not head: return head
        
        curr = head
        
        while curr.next:
            # Case where we don't need to move end element
            if curr.next.val >= curr.val:
                curr = curr.next
                continue
                
            # Otherwise we take out next node and search from start
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = None

            # Change head if new node less than current head
            if nextNode.val < head.val:
                nextNode.next = head
                head = nextNode
                continue

            insertNode = head
            while insertNode.next.val < nextNode.val:
                insertNode = insertNode.next
                
            nextNode.next = insertNode.next
            insertNode.next = nextNode
                
        return head
