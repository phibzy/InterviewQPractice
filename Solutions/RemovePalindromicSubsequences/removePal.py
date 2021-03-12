#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Mar 12, 2021 10:25:31 AEDT
  @file        : removePal

"""

"""
Qs:
    - What defines a substring? Just letters in a particular order?
    - What characters can we get?
    - What is the minimum length of the string?
    - What is the max length?
    - And we just return the number of steps yeah?
        - If whole string is pal, is that one step?

"""

"""
Algo:
    - Long story short, if whole string is not a palindrome,
      then output will be 2
    - Why? Because a substring is any sequence where characters have
      been removed and order is preserved
    - Because we only have 2 possible characters, we can always just
      delete all the a characters (a valid subsequence) and then delete
      all the b characteres -> output of 2
    - A sequence of all As or all Bs will be a pal regardless of length

    - So basically check if string is palindrome, if it is return 1,
      otherwise return 2

    TC: O(N) - because we have to check if whole string is palindrome

"""

class Solution:
    def removePalindromeSub(self, s):
        return 1 if self.isPal(s) else 2 

    # Checks if string is pal
    def isPal(self, s):
        start, end = 0, len(s) - 1

        while (end > start):
            if s[start] != s[end]: return False
            start += 1
            end   -= 1

        return True
       
