#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Feb 09, 2021 14:02:01 AEDT
  @file        : stc

"""

from collections import deque

# TC: O(N) - We make two passes of string
# SC: O(N) - We return list of max length N, and also
#            create a stack of max length N

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # First pass, build stack containing indices of all c chars
        stack = deque([ i for i, v in enumerate(s) if v == c ])
        output = list()
        
        # Guaranteed to have at least one element in list
        # and at least one c char
        
        prev = None
        
        # Then go through again, this time comparing distance between
        # two nearest c chars. Take the minimum of the two for the list
        # Append a 0 for every c char we encounter though
        
        for i, v in enumerate(s):
            if v == c: 
                nextI = 0
                prev = stack.popleft()
                
            elif not stack:
                nextI = abs(i - prev)
                
            elif prev == None:
                nextI = abs(i - stack[0])                
            
            else:
                nextI = min(abs(i - prev), abs(i - stack[0]))
                
            output.append(nextI)
            
        return output
                
            
