#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Feb 26, 2021 12:50:32 AEDT
  @file        : shortestSub

"""

"""
    Qs:
        - Range for length of array
        - Empty array possible?
        - Range of values?
        - If understood correctly, array will be in ascending order apart from subarray?
        `

"""

class Solution:
    # O(NlogN) cheese strategy

    def findUnsortedSubarray(self, nums):
        # If one or less elements, it's sorted
        if len(nums) <= 1: return 0

        # Make copy of list and sort it
        # Find the indices of elements at start and end
        # which differ, then return difference
        sortNums = sorted(nums)

        end = len(nums) - 1
        start = 0

        while start < len(nums):
            if nums[start] != sortNums[start]:
                break

            start += 1

        while end >= 0:
            if nums[end] != sortNums[end]:
                break

            end -=1

        # If already sorted don't need to do anything more
        if end < 0: return 0

        # Otherwise return diff + 1
        return (end - start) + 1

