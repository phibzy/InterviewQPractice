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

        # Setup like we would for binary search        
        start, end = 0, len(nums) - 1


        # This is still a game of halves
        # Even with a rotated array, we can work out which half
        # of array that our target lies in

        # Perform binary search on rotated array using modulo
        while end >= start:
            # Have to keep track of non-modded middle value
            # for calculations to work out nicely
            middle = (start + (end - start) // 2)

            if nums[middle] == target:
                return True

            if nums[start] == nums[middle]:
                while nums[start] == nums[middle]:
                    start += 1
                
                if start > middle: break
            
            if nums[middle] > target:
                if nums[start] > target:
                    start += 1
                
                end = middle - 1

            else:
                start = middle + 1

                if nums[start] > target:


        return False

a = Solution()

print(a.search([1,3,1,1,1],3))

