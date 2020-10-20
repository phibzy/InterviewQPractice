#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Oct 19, 2020 11:06:43 AEDT
  @file        : longestPal

"""

class Solution:
    def longestPalindrome(self, s):
        i = 0
        output = s[i]
        length = len(s)

        evenI = 2
        oddI = 3

        while evenI <= length:
            if oddI <= length and self.checkPal(s[i:oddI]):
                output = s[i:oddI]
                oddI += 2
                evenI += 2

            elif self.checkPal(s[i:evenI]):
                output = s[i:evenI]
                oddI += 2
                evenI += 2

            else:
                i += 1
                evenI += i
                oddI += i
            
        return output
        
    def checkPal(self, s):
        start, end = 0, len(s) - 1

        while end > start:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1

        return True
