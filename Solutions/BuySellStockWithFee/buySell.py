#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Mar 29, 2021 12:11:58 AEDT
  @file        : buySell

"""

"""
Qs:
    - Range of elements in list? Only positive numbers
    - Range of fee? 0 or higher
    - Number of elements? 1 or greater
    - What do we return in case of no profit to be made? 0
    - Can buy in at multiple different prices while already holding? No, must sell before buy

"""

"""
Algo:
    - Start at first number which isn't followed by a lower number
    - Make a queue, store starting number and 0 as tuple 

"""

from collections import deque

class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        q = deque()

        # Find first number that's not followed by lower number
        lastNum = prices[0]

        i = 1
        while i < len(prices) and prices[i] < lastNum:
            lastNum = prices[i]
            i += 1

        # Add first number to queue, then we starteth
        q.append([lastNum, 0])

        while i < len(prices):

            if prices[i] < lastNum:
                # do calculations
                calc = lastNum - fee

                # If > 0, add new entry to q based on most recent sum
                if calc - q[0][0] > 0:
                    newEntry = [prices[i], q[0][1] + calc - q[0][0]]
                    q.appendleft(newEntry)

                # Check rest of q for better options if available
                j = 1
                while j < len(q):
                    # If it beats previous best sum, update it
                    q[j][1] = max(q[j][1], calc - q[j][0])
                    j += 1

            lastNum = prices[i]
            i += 1

        # Add condition for list which ends in ascending numbers
        if len(prices) > 1 and prices[-1] >= prices[-2]:
            # do calculations
            calc = lastNum - fee

            # If > 0, add new entry to q based on most recent sum
            if calc - q[0][0] > 0:
                newEntry = [0, q[0][1] + calc - q[0][0]]
                q.appendleft(newEntry)

            # Check rest of q for better options if available
            j = 1
            while j < len(q):
                # If it beats previous best sum, update it
                q[j][1] = max(q[j][1], calc - q[j][0])
                j += 1

        largest = 0
        for item in q:
            largest = max(largest, item[1])

        return largest

