#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Nov 26, 2020 10:14:04 AEDT
  @file        : smallestInt

"""


class Solution:
    def smallestRepunitDivByK(self, K):
        # Obviously if K is even, then it won't divide into
        # an odd number - i.e. every possible N
        if K % 2 == 0: return -1
        
        # Likewise, any N can't be divisible by 5
        if K % 5 == 0: return -1
       
        # So for our remaining possible K values, we have numbers
        # ending in 1, 3, 7 or 9. All of whom are able to multiply
        # and give numbers ending in a 1 digit

        # We brute force our way to finding the longest number
        # since we know it exists
        n = 1
        while True:
            if n % K == 0:
                return len(str(n))
            
            n = n*10 + 1
