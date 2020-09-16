#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Sep 16, 2020 17:07:49 AEST
  @file        : solution

"""

"""

The "column" approach

Compare each sequential character of each string.
Return as soon as a character in one string is not the same.

Complexity:
    Time: O( N * M) - Where N is number of strings, M length of strings
                    - Worst case all strings are of equal length
    Space: O(1)

"""

def longestCommonPrefix(self, strs):
    # If list is empty, or first string an empty string
    # We return empty string
    if not strs or not strs[0]: return "" 
    
    i = 0

    # We stop if the char position index ever exceeds length of first string
    while i < len(strs[0]):
        # Char to compare
        char = strs[0][i]
        
        for s in strs:
            # Return if exceeds length or if char not same
            if i >= len(s) or s[i] != char: return strs[0][0:i]
              
        i += 1
        
    return strs[0][0:i]

