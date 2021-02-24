#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Feb 24, 2021 11:13:18 AEDT
  @file        : brokenCalc

"""

from collections import deque

class Solution:
    def brokenCalc(self, x, y):
        # Brute force - run a BFS
        q = deque()
        nextQ = deque([x])
        numOps = 0

        while nextQ:
            q = nextQ
            nextQ = deque()

            while q:
                x = q.pop()

                # If X is the same as Y, return numOps
                if x == y: return numOps

                # Append the two possible next numbers

                # Can't have negative numbers
                if x > 1: nextQ.append(x-1)
                nextQ.append(x*2)

            numOps += 1       

        
