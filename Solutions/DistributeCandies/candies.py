#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Mar 04, 2021 12:00:57 AEDT
  @file        : candies

"""

"""
Questions:
    - Range of number of candies?
    - Will number of candies always be even? Need to floor if odd?
    - Will candy types just be ints >= 0?
    - Neg ints?
    - Empty candy list a possibility?
    - Range of N

"""

"""
Algo:
    Count how many different candies there are (using dict) and then
    return the minimum of N/2 and those number of candies

    TC: O(N)
    SC: O(N)

"""

class Solution:
    def distributeCandies(self, candyType):
        # Number of candies we can eat
        numEat = len(candyType) // 2

        # Keep track of unique candy types
        uniq = dict()

        # Check if candy is unique, add to dict
        for candy in candyType:
            uniq.setdefault(candy, 1)

            # If number of unique candies is equal to the max
            # we're allowed to eat, we can early exit
            if len(uniq) == numEat:
                return numEat

        # Otherwise return the number of unique candies
        return len(uniq)

