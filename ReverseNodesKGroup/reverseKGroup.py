#!/usr/bin/python3


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import logging
import pdb

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
# logging.disable(logging.DEBUG)

class Solution:
    def reverseKGroup(self, head, k):
        # pdb.set_trace()

        if k == 0 or k == 1 or head is None: return head
        
        # will need to change head
        start = head
        end = start 
    
        while end:
            nextStart = end
            # logging.debug(''.rjust(30, '-'))
            # logging.debug('NEW MAIN LOOP')
            # logging.debug(''.rjust(30, '-'))

            # logging.debug(f"start is {start.val}")
            # logging.debug(f"end is {end.val}")

            kCount = k

            # logging.debug(f"entering kcount loop")
            while kCount > 1 and end.next:
                kCount -= 1
                end = end.next

            # logging.debug(f"end is {end.val}")
            


            # not a multiple, no need to do anything more
            if kCount > 1: return head

            rest = end.next
            end = start

            if end != head: start = start.next

            # logging.debug(f"end is {end.val}")
            
            # if rest:
                # logging.debug(f"rest is {rest.val}")
            # else:
                # logging.debug("rest is None")

            nextNode = start.next
            start.next = rest

            while nextNode != rest:
                # logging.debug(f"nextNode is {nextNode.val}")
                # logging.debug(f"start is {start.val}")

                curr = nextNode.next
                nextNode.next = start
                start = nextNode
                nextNode = curr

            if end == head:

                head = start
                start = end

            else:

                end.next = start    
                start = nextStart

            end = start.next
            # pdb.set_trace()
        
        return head

def printList(head):
    while head:
        print(f" --> {head.val}") 
        head = head.next
        
a = Solution()

thing = a.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5)
printList(thing)

