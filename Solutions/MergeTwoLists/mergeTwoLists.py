#!/usr/bin/python3

"""
Given two sorted singly linked lists, merge them into one ordered list

Return head of sorted list

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Two approaches:

    # 1 - Create dummy head and just keep adding on 
    # 2 - Use one of the existing heads

    # Approach 1
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # newL = None
        # if l1 is None and l2 is None: return None
        # if l1 and not l2: return l1
        # if l2 and not l1: return l2


        # if l1.val < l2.val:
            # head = l1
            # newL = l1
            # l1 = l1.next

        # else:
            # head = l2
            # newL = l2
            # l2 = l2.next

        # newL.next = None

        # while l1 and l2:
            # if l1.val < l2.val:
                # newL.next = l1
                # l1 = l1.next
            # else:
                # newL.next = l2
                # l2 = l2.next
            
            # newL = newL.next
            # newL.next = None
        
        # if l1: newL.next = l1                  
        # if l2: newL.next = l2

        # return head

    # Approach 2
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if not l1 and l2: return l2
        if l1 and not l2: return l1

        if l2.val < l1.val:
            temp = l2
            l2 = l1
            l1 = temp

        head = l1

        while l1.next and l2:
            if l2.val < l1.next.val:
                rest1 = l1.next
                rest2 = l2.next
                l1.next = l2
                l1.next.next = rest1
                l2 = rest2

            l1 = l1.next

        if l2: l1.next = l2

        return head        

        




        

    def printList(self, l):
        while l:
            print(f" {l.val} -->", end='')

        print()





