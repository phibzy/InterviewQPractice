#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Oct 21, 2020 12:01:14 AEDT
  @file        : FIFO

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
        
    def __init__(self):
        self.front = None
        self.end = None
        

    # TC: O(1)
    def push(self, x):
        newNode = Node(x)
        
        if self.empty():
            
            self.front = newNode
            self.end = newNode
        
        else:
            
            self.end.next = newNode
            self.end = self.end.next
        
    # TC: O(1)
    def pop(self):
        if self.empty(): return None
        
        rVal = self.front
        
        self.front = self.front.next
        if self.empty(): self.end = None
            
        return rVal.val
    
    def peek(self):
        if self.empty(): return None
    
        return self.front.val

    def empty(self):
        return self.front is None

class MyQueueAmortized:

    
    # SC: O(N) - Kinda goes without saying, but you will have all the elements
    # of queue in your stacks...
    # All pops/peeks are valid, don't need to check for empty stack
    def __init__(self):
        # s1 is used as a normal stack
        # s2 is the stack with the queue order
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        self.s1.append(x)      
        
        
    """
    Reason this works for amortized O(1):
    
    We only care about queue order when peeking/popping.
    That means instead of reording our stack at every push, we only
    do it when need to.
    
    When we peek/pop, if our second stack is empty that means we don't 
    know what's at the front of queue. So we check our normal stack s1 and
    pop off s1 and append to s2 to end up with the correct order.
    
    We don't care what's on s1 much while s2 isn't empty, since the order will
    be redone again once more when needed   

    This means we are worst case doing N/2 operations twice or N operations once,
    which overall will give us amortized O(1)
    
    """        
        
    # TC: O(1)
    def pop(self) -> int:
        self.peek()
                        
        return self.s2.pop()
        
    # Order stack
    # At worst a O(N) operation that is done once - giving us overall O(1)
    def peek(self) -> int:
        if not self.s2:
            while (self.s1):
                self.s2.append(self.s1.pop())
        
        return self.s2[-1]
        
    # TC: O(1)
    # If both stacks are empty, we got nuthin dawg
    def empty(self) -> bool:
        return (not self.s1) and (not self.s2)
        """
        Returns whether the queue is empty.
