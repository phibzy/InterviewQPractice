#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Mar 08, 2021 11:23:44 AEDT
  @file        : intersect

"""

"""
Qs:
    - Length range of each llist, can either be empty?
    - Are they guaranteed to intersect?
    - Are values unique?
    - What do we return on no intersection?
    - While heads of list always be non-intersecting?
    - Does "original structure" mean keeping same values as well?
        - Does it mean no modifications at all?
        - If so, just *-1 to fix again

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n 

    def __eq__(self, x):
        return self.val == x.val

"""
Initial Solution:
    Use dict, with node refs as keys. If one shows up again then you have your
    intersecting val.

    O(N+M) TC and SC

O(1) Space Solution:
    Since we know values can't be negative, we can do the same as before except
    instead of using a hash, we just multiply vals by -1.

    If we ever come across a value < 0, then we have our intersection.
    
    Addendum: It says to preserve structure, says nothing about values. If values
    had to be restored you could iterate from each head multiplying by -1 until you
    reach a positive number.

"""

class Solution:
    def getIntersectionNode(self, headA, headB):
        # Loop through, find tha node
        intersectVal = 0
        a, b = headA, headB

        while headA or headB:
            if headA:
                if headA.val < 0: 
                    intersectVal = abs(headA.val)
                    break

                headA.val *= -1
                headA = headA.next
        
            if headB:
                if headB.val < 0: 
                    intersectVal = abs(headB.val)
                    break

                headB.val *= -1
                headB = headB.next

        # Restore vals if need be before returning

        return intersectVal

