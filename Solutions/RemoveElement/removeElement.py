#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Sep 02, 2020 10:42:57 AEST
  @file        : removeElement

"""

class Solution:
    def removeElement(self, nums, val):
        if not nums: return 0
        
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            elif nums[i] > val:
                break
            else:
                i += 1
        
        return len(nums)
