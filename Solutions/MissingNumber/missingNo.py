#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Mar 04, 2021 13:24:11 AEDT
  @file        : missingNo

"""

class Solution:
    # The cheeeeeeeeeeeese
    # Just find the difference between the expected sum of all numbers 0 to N
    # and the sum of everything in nums

    # TC: O(N) - possibly O(1) depending on list implementation
    # SC: O(1)
    def missingNumber(self, nums):
        return (sum(range(len(nums)+1)) - sum(nums))
        
