#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Oct 26, 2020 14:07:09 AEDT
  @file        : searchInsert

"""

class Solution:
    def searchInsert(self, nums, target):
        # Binary search
        # Time Complexity: O(logN)
        
        start, end = 0, len(nums) - 1
        
        while end >= start:
            # get middle element
            middle = start + (end-start) // 2
            
            if nums[middle] == target:
                return middle
            
            if target > nums[middle]:
                start = middle + 1
            
            else:
                end = middle - 1
        
        # if while condition breaks, target isn't in list
        # Either endpost has gone beyond start post (less than first element),
        # or start post goes beyond end post (greater than last element)
        # Each case means start index is the right insertion position
        return start
