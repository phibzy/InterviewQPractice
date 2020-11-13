#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Nov 13, 2020 11:22:09 AEDT
  @file        : permutationsII

"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

class Solution:
    def permuteUnique(self, nums):
        return list(self.rpermuteUnique(nums))         
        
    def rpermuteUnique(self, nums):
        """
        Basic Algo:

        For each recursive call we create a set.
        This set will contain each unique combination for each sublist.

        Our base cases are when we have 1 or 2 elements:
            1 element  - return a list 2D list containing 1 list with the one element
            2 elements - Return list with the only 2 possible combos

        Recursive case:
        
            For each element in list, place it in front position then call recursive function
            on all the other elements.

            Then for each combo in the "tail" of the list, add First Element + Combo to the output set

        NOTE: All the tuple stuff is there because list types aren't hashable,
              so we must use tuples with the set instead

        TC: O(N!) - we have to check every combination, there are at most N!
        SC: O(N!) - we have a set with at most O(N!) entries in it

        """
        
        # Just to make sure python list slices play nicely
        if not nums: return tuple([nums])
        
        # Base cases: length 1 and 2 lists
        if len(nums) == 1: return tuple([nums])
        
        if len(nums) == 2:
            if nums[0] == nums[1]: return tuple([nums])
            return tuple([nums,[nums[1], nums[0]]])
        
        output = set()
        
        # Go through first element + tails combos
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            
            for subList in self.rpermuteUnique(nums[1:]):
                nextL = tuple(nums[:1]) + tuple(subList)
                output.add(tuple(nextL))

        return tuple(output)

