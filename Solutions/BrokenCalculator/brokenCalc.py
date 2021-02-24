#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Feb 24, 2021 11:13:18 AEDT
  @file        : brokenCalc

"""

from collections import deque

class Solution:

    # Optimisations - x > y, the only way to get to y
    # is by decrementing. So we could just return x - y for that case

    # Could also have a visited hash
    def brokenCalc1(self, x, y):
        # Brute force - run a BFS
        q = deque()
        nextQ = deque([x])
        numOps = 0

        while nextQ:
            q = nextQ
            nextQ = deque()

            while q:
                x = q.popleft()
                print(x)

                # If X is the same as Y, return numOps
                if x == y: return numOps

                # Append the two possible next numbers

                # Can't have negative numbers
                if x > 1: nextQ.append(x-1)
                nextQ.append(x*2)

            numOps += 1       

            print("".rjust(10, '-') + "Next batch" + "".rjust(10,'-'))

    # Improved solution
    def brokenCalc(self, x, y):
        # New plan - think from y perspective
        # When thinking of x's perspective, it's hard to tell
        # when we should double or decrement, since we can always do both.
        # From y's perspective, we can only halve when y is even
        # From y's perspective, if we have an even number it is always
        # more optimal to halve - since you would have to increment twice to
        # be able to halve again, which requires an extra step compared to halving and incrementing

        # TC: O(logN) - Where N is the number Y. Worst case we have to reduce down to 1.
        #               Along the way we can only increment a max of logN times, since halving is
        #               always optimal
        # SC: O(1) - We don't use any extra space
        
        if x == y: return 0
        
        numOps = 0        
        
        while (y > x):
            # If y is even, halve it
            if y % 2 == 0:
                y //= 2
           
            # otherwise increment
            else:
                y += 1
                
            numOps += 1
                
        numOps += (x - y)
        
        return numOps
        
