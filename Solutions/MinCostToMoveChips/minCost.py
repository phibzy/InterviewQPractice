#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Nov 06, 2020 14:50:15 AEDT
  @file        : minCost

"""

class Solution:
    def minCostToMoveChips(self, position):
        """
        Since Even jumps cost nothing, the main concern is:
        
            - How many odd and even positions there are
            - Which one is greater
            
        The resulting cost is the sum of the minimum group
        
        """
        
        if len(position) == 1: return 0
        
        # Count odd and even positions
        oddCount, evenCount = 0, 0
        
        for i in position:
            if i % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        
        # if all positions are either even or odd, total cost will always be 0
        # since they can make leaps in multiples of 2
        if oddCount == 0 or evenCount == 0:
            return 0
        
        return min(oddCount, evenCount)
