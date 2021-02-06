#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Saturday Feb 06, 2021 12:53:55 AEDT
  @file        : LHS

"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Another way:
        # Freq dict, add each number
        # if -1 exists, add freqs and check max
        # same for + 1
        maxLength = 0
        freq = dict()
        
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
            
            # Have to check that diff 1 number exists
            # before updating maxLength, because if it doesn't
            # then it's not a sequence
            if num-1 in freq:
                maxLength = max(maxLength, freq[num] + freq[num-1])
                
            if num+1 in freq:
                maxLength = max(maxLength, freq[num] + freq[num+1])
            
        return maxLength
