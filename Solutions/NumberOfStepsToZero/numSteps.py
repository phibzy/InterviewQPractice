#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Feb 15, 2021 12:03:48 AEDT
  @file        : numSteps

"""

"""
Extra:
    If the question instead had an array of numbers which we had to calculate,
    we could use memoisation with a dict to speed up the process whenever we
    encounter a number we've seen before



"""

class Solution:
    def numberOfSteps (self, num: int) -> int:
        # use mod to check if even/odd, then perform operation
        steps = 0
        
        while num != 0:
            if num % 2 == 0:
                num //= 2
            
            else:
                num -= 1
            
            steps += 1
                
        return steps
