#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Mar 18, 2021 10:49:56 AEDT
  @file        : checkBinary

"""

"""
Qs:
    - Min/Max size of K?
    - Will input string ever be empty?
    - Max size of input string?
    - EVERY possible combo?

    Early termination if combos dict reaches 2**K


"""

"""
Algo:

    Put all k size subtrings from s into dict - O(N)
    Since we know that max amount of substrings of size
    k will be 2**k (since only using binary characters),
    we return true if length of dict == 2**k

    TC: O(N) - Visit each character in dict once
    SC: O(N) - Have at most N entries in dict


"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # If k > s.length, then it obviously won't work
        if k > len(s): return False

        # Generate all substrings of size k in string
        # BIG BRAIN MOMENT: since we know that we will have 2**K possible
        # substrings, once the pass is done simply check if size of dict is 2**K
        # Return True if it is, False if it isn't
        substrings = dict()

        i = 0
        nextK = k
        while len(substrings) != 2**k and nextK <= len(s):
            # Get next substring
            nextS = s[i:nextK]
            substrings.setdefault(nextS, 1)
            i += 1
            nextK += 1

        # Check if we have the required number of unique substrings
        return len(substrings) == 2**k
            

