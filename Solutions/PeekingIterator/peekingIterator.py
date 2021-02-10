#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Feb 10, 2021 22:25:03 AEDT
  @file        : peekingIterator

"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


"""
Algo:

    Idea is to keep iternal representation of actual iterator
    Then we also use a variable to keep track of next item
    
    When peek is used for the first time in current position, we use
    the .next() method of original iterator, storing returned value in var.
    We keep track of first usage by setting it to null everytime peekingIt.next() is called.

    peekingIterator.next() therefore checks if we've already peeked, if
    we have then we just need to return var's value before setting it to null again

    For hasNext, we check that either our peekVal exists or if original iterator.hasNext()
    Reason being because if we peek last element then original iterator won't have anything left

"""



class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.peekVal = None       

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peekVal == None:        
            self.peekVal = self.it.next()
        
        return self.peekVal

    def next(self):
        """
        :rtype: int
        """
        if self.peekVal != None:
            rVal = self.peekVal
            self.peekVal = None
            
        else:
            rVal = self.it.next()
        
        return rVal


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peekVal != None or self.it.hasNext()
        
        
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
