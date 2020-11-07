#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Saturday Nov 07, 2020 18:26:32 AEDT
  @file        : smallestDivisor

"""

import math

class Solution:
    
    # Time Complexity: O(NlogM) - Go through list of N items logM times (aka N binary searches)
    #                           - where M is the max value in list
    
    def smallestDivisor(self, nums, threshold):
        largest = 0
        total = 0
        
        for i in nums:
            total += i
            largest = max(largest, i)
            
        # Case for divisor of 1
        if total <= threshold: return 1
            
        # Find middle int of 1 and largest number
        start = 1
        retVal = 1
       
        # Perform binary search
        while largest >= start:
                
            middle = start + ((largest - start) // 2)
            total = 0
            
            for i in nums:
                # Perform sum with middle as divisor
                total += math.ceil(i / middle)
                
            if total <= threshold:
                retVal = middle
                largest = middle - 1
                
            else:
                start = middle + 1
                
        return retVal
