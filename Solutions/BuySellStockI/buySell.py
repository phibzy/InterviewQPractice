#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Nov 18, 2020 21:12:41 AEDT
  @file        : buySell

"""

# TC: O(N) - We make one pass of the list
# SC: O(1) - We use same amount of space regardless of list size

class Solution:
    def maxProfit(self, prices):
        # If there's no prices or only one price,
        # we can't make any profit
        if len(prices) < 2: return 0

        # TL;DR want to find difference between max and min value
        # However, we only keep track of minimums as we go along
        i = 0

        maxProfit = 0
        minVal = prices[0]

        while (i + 1) < len(prices):
            minVal = min(minVal, (prices[i]))

            diff = prices[i+1] - minVal

            if diff > 0:
                maxProfit = max(maxProfit, diff)
            
            i += 1

        return maxProfit



        
