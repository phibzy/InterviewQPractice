#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Sep 01, 2020 14:04:12 AEST
  @file        : removeDuplicates

"""

class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0
        last = nums[0]
        i = 1

        while i < len(nums):
            if nums[i] == last:
                del nums[i]

            else:
                last = nums[i]
                i += 1


        return len(nums)
        
