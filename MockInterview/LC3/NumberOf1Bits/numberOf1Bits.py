#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Oct 22, 2020 12:49:06 AEDT
  @file        : numberOf1Bits

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Brute force, O(logN) solution
        # logN because a number's binary representation is logN bits
        # Get binary representation, go left to right and add up 1s
        num = bin(n)
        
        hammingWeight = 0
        
        #for i in num:
        #    if i == '1':
        #        hammingWeight += 1
                
        #return hammingWeight
        
        # Subtracting highest 1 digit approach
        # Skip over the 0s in the middle by subtracting highest
        # placed 1 digit.
        
        # My method: Get binary representation length, -2 for the '0b' part
        # of string, -1 after for 0-indexing of exponent
        # Subtract 2^result, i.e. the place of the digit        
        
        # TC: DlogN - where D is number of 1 digits
        # logN because bin(n) has complexity of logN
        
        while n > 0:
            n -= 2**(len(bin(n))-3)
            hammingWeight += 1
         
       # while n > 0:
       #     twoC = ~n + 1
       #     twoC >>= 1
       #     n-=twoC
       #     hammingWeight+=1                
        
        return hammingWeight
