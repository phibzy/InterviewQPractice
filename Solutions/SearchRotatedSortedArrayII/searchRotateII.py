#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Saturday Nov 21, 2020 11:49:58 AEDT
  @file        : searchRotateII

"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

class Solution:
    def search(self, nums, target):
        # obv want to do this in better than O(N) time
        if not nums: return False
        if len(nums) == 1: return nums[0] == target
        
        # We use binary search to find start and endpoints of array
        start, end = 0, len(nums) - 1

        # Can speed this up by return True if target
        # found during this first half

        # Only need to find new start/ends if list is actually rotated
        if nums[end] <= nums[start]:

            while end >= start:
                middle = start + (end - start) // 2

                if nums[middle] < nums[start]:
                    end = middle - 1

                else:
                    start = middle + 1

            start = middle 
            end = start + len(nums) - 1

        logging.debug("----------------")
        logging.debug(f"start: {start}, end: {end}")
        logging.debug("----------------")

        # Perform binary search on rotated array using modulo
        while end >= start:
            # Have to keep track of non-modded middle value
            # for calculations to work out nicely
            middle = (start + (end - start) // 2)
            moddedMiddle = middle % len(nums)

            logging.debug(f"start: {start}")
            logging.debug(f"end: {end}")
            logging.debug(f"moddedMiddle: {moddedMiddle}")

            if nums[moddedMiddle] == target:
                return True
            
            elif nums[moddedMiddle] > target:
                end = middle - 1

            else:
                start = middle + 1

        return False

a = Solution()

print(a.search([3,1,1], 3))

