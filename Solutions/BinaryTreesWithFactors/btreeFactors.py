#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Mar 19, 2021 14:42:12 AEDT
  @file        : btreeFactors

"""

"""
Qs:
    - Can numbers repeat?
    - Are numbers in array unique?
    - Range of array length?
    - Range of array values?
    - Are numbers in order?


"""


"""
Basic Algo:
    Create hash containing all numbers inside of the array as keys, setting values to 1.
    We will also sort the array in ascending order.

    We will then go through each number N checking if that number divided by any of the previous numbers
    exists in the array. If it does, add factor totals to N's value in the hash. Then add the total of the factors'
    hash values to the grand total.

    TC: O(N^2logN) 
    SC: O(N)

"""

class Solution:
    MOD = 10**9 + 7

    def numFactoredBinaryTrees(self, arr) -> int:
        # Keep track of numbers seen
        seen = dict()
        total = 0

        # Sort nums in ascending order
        arr.sort()
        
        for n in arr:
            seen.setdefault(n, 1)

        # Go through every number checking for pairings
        i = 0
        while i < len(arr):
            checkNum = arr[i]

            # Check all preceding numbers to see if we have factor pairings
            for num in arr[:i]:
                factor = checkNum / num

                # if other factor isn't an int, then keep going
                if factor % 1 != 0: 
                    continue

                factor = int(factor)

                if factor in seen:
                    # Add only one hash value if factors are equal
                    seen[checkNum] += seen[factor]*seen[num]

            i += 1
            total += seen[checkNum]
        
        return total % self.MOD






        
