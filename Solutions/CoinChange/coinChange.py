#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Mar 17, 2021 09:35:46 AEDT
  @file        : coinChange

"""

"""
Qs:
    - Will we always get at least one coin denomination?
    - Are we guaranteed to have a valid solution with the given coins?
    - What are the ranges of coin denominations?
    - Will number always be greater than 0? Range?
    - Behaviour for 0?
    - Guaranteed coins will be in order?


    Can't do braindead greedy algo, e.g.

    coins = [10,125,200]
    amount = 500

    Greedy would be 200*2 + 10*10, whereas optimal is 4*125

"""


"""
Algo:

    Pure brute force. Just check if starting amount is 0 to rule out that case.
    Then test all possible combos using a q.

"""

from collections import deque

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # If amount is 0, return 0
        if amount == 0: return 0

        # Could do a BFS...
        # Then have a visited state based on the amount number
        visited = dict()
        q = deque() 
        
        # Append all possible starting coins
        for c in coins:
            q.append((amount - c, 1))

        while q:
            nextAmount, steps = q.popleft()

            # We have our answer if the amount reaches 0!
            if nextAmount == 0: return steps

            # If we go go bust, don't bother with this path anymore
            # If we've already reached our nextAmount same other way,
            # due to BFS we can't possibly reach it in quicker time with current path
            if nextAmount < 0 or nextAmount in visited: continue

            # Mark as visited
            visited[nextAmount] = 1

            # Add next nodes
            for c in coins:
                n = nextAmount - c
                s = steps + 1
    
                if n >= 0 and n not in visited:
                    q.append((n, s))
        
        return -1


