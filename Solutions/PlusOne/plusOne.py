#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Oct 27, 2020 19:10:13 AEDT
  @file        : plusOne

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Two methods:
        # Add 1 to last element then keep going backwards for overflow,
        # inserting at front if extra digit added
        # Worst case TC: O(N) - a number like 99999 where we have to add extra digit at front
        
        # Other method: convert list to number then add 1, then split on each char
        
        # length at least 1
        i = len(digits) - 1
        
        digits[i] = (digits[i] + 1) % 10
        
        while i > 0 and digits[i] == 0:
            i -= 1
            digits[i] = (digits[i] + 1) % 10
        
        if digits[0] == 0:
            digits = [1] + digits
            
        return digits
