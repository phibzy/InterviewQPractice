#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Nov 08, 2020 19:30:05 AEDT
  @file        : addTwo

"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # First, need to check which is longer
        # We will place the longer one in l1
        len1 = self.lenList(l1)
        len2 = self.lenList(l2)
        
        if len2 > len1:
            l1, l2 = l2, l1

        # No leading 0s unless number is 0
        if l2.val == 0: return l1
        
        # find difference
        diff = abs(len1 - len2)
        
        # Gonna use stack to keep track of node values
        # creating return list as we go
        valStack = list()
        rList = None
        
        for _ in range(diff): 
            valStack.append((l1.val, 0))
            l1 = l1.next
            
        while l1:
            valStack.append((l1.val, l2.val))
            l1 = l1.next
            l2 = l2.next
            
            
        # STILL NEED TO HANDLE LEN1 ADDING NODE AT FRONT CASE
        carry = 0
        while valStack:
            n1, n2 = valStack.pop()
            sumN = n1 + n2 + carry
            
            if (sumN >= 10):
                carry = 1
            
            else:
                carry = 0
            
            rList = ListNode((sumN % 10), rList)
            
        if carry:
            rList = ListNode(1, rList)
            
            
        return rList
    
    def lenList(self, l):
        c = 0
        while l:
            c += 1
            l = l.next
        
        return c
