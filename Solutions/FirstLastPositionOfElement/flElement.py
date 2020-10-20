#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Oct 20, 2020 11:21:15 AEDT
  @file        : flElement

"""

import logging 

# logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

# Time Complexity: O(logN) - just binary search over and over
# Space Complexity: O(1)

class Solution:

    def searchRange(self, nums, target):
        # Case 1: empty array
        output = [-1, -1]
        # logging.debug(f"nums is {nums}")
        if not nums: return output

        # Case 2: out of bounds
        if target < nums[0] or target > nums[-1]: return output

        # Middle: start + (end - start) // 2
        start, end = 0, len(nums) - 1

        while end >= start:
            middle = start + (end-start) // 2

            # logging.debug(f"start is {start}, end is {end}, middle is {middle}")

            if nums[middle] == target:
                output = [middle, middle]
                # find real start
                self.findStart(nums, output, start, middle, target)
                # find real end
                self.findEnd(nums, output, middle, end, target)
                break

            elif target > nums[middle]:
                start = middle + 1
            
            else:
                end = middle - 1

        return output

    def findStart(self, nums, output, start, end, target):
        while end > start:
            middle = start + (end-start) // 2
            # logging.debug(f"middle is {middle} in fstart")

            if nums[middle] == target:
                output[0] = middle
                end = middle

            # Can only be equal or less than target at this point
            else:
                start = middle + 1


    def findEnd(self, nums, output, start, end, target):
        # logging.debug(f"OG start {start}, end {end} in fend")
        while end >= start:
            middle = start + (end-start) // 2
            # logging.debug(f"middle is {middle}, start {start}, end {end} in fend")

            if nums[middle] == target:
                output[1] = middle
                start = middle + 1

            # Can only be equal or greater than target at this point
            else:
                end = middle - 1


