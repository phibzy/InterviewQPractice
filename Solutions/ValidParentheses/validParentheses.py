#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Jul 14, 2020 17:43:17 AEST
  @file        : validParentheses

  Given a string of parentheses, check if the brackets match up


"""

# Time/Space Complexity: O(N)
class Solution:
    def isValid(self, s):
        st = list()
        match = { ')': '(', ']': '[', '}': '{' }
        
        for c in s:
            if c in match:
                if (not st) or (st.pop() != match[c]):
                    return False
            
            else: 
                st.append(c)
        
        return len(st) == 0
