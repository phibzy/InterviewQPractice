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
        if len(nums) == 2: return nums[0] == target or nums[1] == target

        
        # We use binary search to find start and endpoints of array
        start, end = 0, len(nums) - 1

        # Can speed this up by return True if target
        # found during this first half
        minVal = float('inf')
        minI = 0

        # Only need to find new start/ends if list is actually rotated
        if nums[end] <= nums[start]:

            while end >= start:
                middle = start + (end - start) // 2

                # The annoying case
                if nums[start] == nums[middle]:

                    while nums[start] == nums[middle]:
                        
                    

                elif nums[start] < nums[middle]:

                    if nums[start] < minVal:
                        minVal = nums[start]
                        minI = start

                    start = middle + 1                    

                else:

                    if nums[middle] < minVal:
                        minVal = nums[middle]
                        minI = middle

                    start += 1
                    end = middle - 1

            start = minI
            end = start + len(nums) - 1

        # Perform binary search on rotated array using modulo
        while end >= start:
            # Have to keep track of non-modded middle value
            # for calculations to work out nicely
            middle = (start + (end - start) // 2)
            moddedMiddle = middle % len(nums)

            if nums[moddedMiddle] == target:
                return True
            
            elif nums[moddedMiddle] > target:
                end = middle - 1

            else:
                start = middle + 1

        return False

a = Solution()

print(a.search([1,3,1,1,1],3))

