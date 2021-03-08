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

"""
Since problem description contradicts engine results:
    O(1) space and O(N^2) time Solution:
        For every node in A, check every node in B to see if it's the same
        Optimisations: Find shorter list to speed up checks

    O(1) Space and O(N) time:
        If intersection:
            len(a) +len(c) + len(b) = len(b) + len(c) + len(a)
            where c is the common "tail" of each list

            because of this, we can loop through a and b, checking if they're equal.
            if a reaches null, set it to head of b
            if b reaches null, set it to head of a

            This will work since after resetting pointers, since they'll differ by
            difference of len(a) and len(b), meaning that the pointer switch will put them in sync


"""
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        
        if not headA or not headB: return None
        
        # Even if they equal None at the end, we can reset them
        while headA != headB:
            if not headA: 
                headA = b
            else:
                headA = headA.next
                
            if not headB:
                headB = a
            else:
                headB = headB.next
            
        return headA

