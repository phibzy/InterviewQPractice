#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Nov 02, 2020 10:40:18 AEDT
  @file        : binToInt

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head):
        total = 0

        while head:
            total = total*2 + head.val
            head = head.next

        return total
