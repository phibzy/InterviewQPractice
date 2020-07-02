#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Jul 02, 2020 14:30:15 AEST
  @file        : numberOf1Bits

  Given an integer, return the number of 1 bits in its binary representation

"""

class Solution:
    def hammingWeight(self, n):

        # Solution 1: O(N) - where N is number of bits in given integer
        # Algo: Keep shifting by 1 bit to the right, add one to counter if smallest digit is 1

        # ones = 0
        
        # while n != 0:
            # ones += n&1
            # n >>= 1
            
        # return ones


        # Solution 2: O(k) - where k is the number of 1 bits in given integer
        """
        Algo: General idea is to skip over 0 digits
        
        When n is ANDed with n-1, all bits after the next nearest 1 digit (if any) will be cleared
        Think right to left

        E.g. 001010

        We and it with 001001, giving us: 001000 - notice how all the bits after the second 1 bit (when thinking right to left)
        have been cleared. We repeat process again and we end up with zero. Our count returns 2.
        """


        ones = 0

        while n != 0:
            n &= n - 1
            ones += 1

        return ones








