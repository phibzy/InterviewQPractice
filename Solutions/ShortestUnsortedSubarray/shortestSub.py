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
    # O(N) strat
    # Basically we want to keep track of the maximum element as we go along
    # At each index, we check if the next element is greater than the current maximum
    # if it isn't keep track of that index - that's the furthest index right that needs to be swapped

    # Do the same starting at the other end, but for minimums
    # Keep updating to find leftmost index that needs to be swapped
    def findUnsortedSubarray(self, nums):
        # If one or less elements, it's sorted
        if len(nums) <= 1: return 0

        # Maximum starts out as first element
        # Minimum starts out as last element
        currMax = nums[0]
        currMin = nums[-1]

        start = -1
        end = -1

        # Loop for finding rightmost element
        for i in range(1, len(nums)):
            
            # If not greater/equal to, then it's out of order
            if nums[i] < currMax:
                end = i

            # Otherwise update the max
            else:
                currMax = nums[i]

        # Loop for leftmost element
        for i in range(len(nums) - 2, -1, -1):

            if nums[i] > currMin:
                start = i

            # Otherwise update the max
            else:
                currMin = nums[i]


        # If we never set start, then it's already sorted
        if start == -1: return 0

        return end - start + 1

    # O(NlogN) cheese strategy
    def findUnsortedSubarray1(self, nums):
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

