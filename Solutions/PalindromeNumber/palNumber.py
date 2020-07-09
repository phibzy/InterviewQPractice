#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Jul 09, 2020 18:57:39 AEST
  @file        : palNumber

    
  Given a number, determine whether it's a palindrome or not

  Challenged myself to do it without converting to a string

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        revNum = 0
        tempX = x
        
        # To get next digit just mod by 10
        while tempX > 0:
            revNum = revNum * 10 + tempX % 10
            tempX //= 10
            
        return x == revNum
