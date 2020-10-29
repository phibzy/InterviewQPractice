#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Oct 29, 2020 12:48:04 AEDT
  @file        : firstUniqueChar

"""

class Solution:
    def firstUniqChar(self, s):
        # if not s: return -1
        
        # # Hash keeping track of which letters have been seen
        # letters = dict()
        
        # # Use stack to keep track of changing output
        # output = list()
        
        # # TC: O(N) - We go through string once, go through stack of length N for amortised N cost
        # # SC: O(N) - A hash of size N and a stack of size N
        
        # # go backwards
        # for i in range(len(s)-1, -1, -1):
            # letters.setdefault(s[i], 0)
            # letters[s[i]] += 1
            
            # if letters[s[i]] == 1:
                # output.append(i)
            
            # else:
                # # keep popping to get rid of duplicates
                # while (output) and (letters[s[output[-1]]] > 1):
                    # output.pop()                
        
        # if output: return output[-1]
        
        # return -1

        # Better solution: TC O(N) and SC O(1)
        # First pass - count character frequency
        # Second pass - find first char that shows up only once
        # Otherwise return -1

        letters = dict()
        
        for i in s:
            letters.setdefault(i, 0)
            letters[i] += 1
        
        for i, val in enumerate(s):
            if letters[val] == 1:
                return i
            
        return -1             
