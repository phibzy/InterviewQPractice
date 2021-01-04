#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Jan 04, 2021 09:59:12 AEDT
  @file        : arrange

"""

from pprint import pprint
from copy import deepcopy

class Solution:
    def countArrangement(self, n: int) -> int:
        iDicts = [ dict() for _ in range(n+1) ]

        # Create dictionary for each i that contains every
        # number that can be placed at that position
        # Place all these in a 1-indexed array for easy access
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i % j == 0 or j % i == 0:
                    iDicts[j][i] = 1

        # Calculate possibilities
        return self.calcPossible(iDicts, 1, n)

    def calcPossible(self, iDicts, i, n):
        # print(f"i: {i}, iDicts: {iDicts}, iDicts[i]: {iDicts[i]}")
        # If we get to end of array and last element's dict
        # isn't empty, we found a path!
        if i == n and iDicts[i]: return len(iDicts[i])

        # If there's no possibilities, we return 0
        if not iDicts[i]: return 0

        possibleCount = 0

        # For each possible number we can place at ith position
        # Remove that number from all dictionaries ahead of it
        # and then check all possibilities for other positions
        for num in iDicts[i]:
            # print(f"recursing on {num} in i: {i}")
            tempDicts = deepcopy(iDicts)

            # If removal of number causes a dict ahead of i
            # to reach length of 0, there's 0 possibilities
            # for this path
            for j in range(i + 1, n + 1):
                if num in tempDicts[j]:
                    del tempDicts[j][num]
                    if len(tempDicts[j]) == 0: continue

            # Count all possible paths from this position
            possibleCount += self.calcPossible(tempDicts, i+1, n)

        return possibleCount

a = Solution()
