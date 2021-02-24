#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Feb 24, 2021 15:08:01 AEDT
  @file        : longestDict

"""

from collections import deque
from copy import deepcopy

# What is the min/max string length?
# Dictionary - guaranteed at least one entry? Order for dictionary?
# What type of characters in string? All lowercase?
# Matching case?

# string length: 0 <= L <= 1000
# Dict length: Same
# Assume no order in dict

# TC: O(N+M) - Where N is length of s, and M is combined length of all words in dict
# SC: O(N) - We have a dictionary containing queues with N entries for each letter

class Solution:
    def findLongestWord(self, s, d):
        output = ""

        # First case - empty string or dict
        if not s or not d: return output
       
        # Create dict -> q data structure
        chars = dict()

        for i in range(len(s)):
            # Insert character into q, then keep track of index
            chars.setdefault(s[i], deque())
            chars[s[i]].append(i)

        # Then we check each word in dict
        # Keep track of longestLength word, we can skip
        # any words shorter than this length
        longestLength = 0

        for word in d:
            # If current word can't be current best length, continue
            if longestLength > len(word): continue

            # Otherwise check char by char
            # Make sure to copy chars DS first
            # We need a deep copy though
            check = deepcopy(chars)

            remWord = len(word)
            currIndex = 0
            for nextChar in word:
                remString = len(s) - currIndex
               
                # If there's not enough string left, stop
                if remWord > remString: break

                # If next char not in string, stop
                if not nextChar in check: break

                # Otherwise, check there's an occurrence of this letter
                # after the current index
                nextI = check[nextChar].popleft()

                while check[nextChar] and nextI < currIndex:
                    nextI = check[nextChar].popleft()

                # If the only available index is behind us, stop
                if nextI < currIndex: break

                # If q empty (i.e. no more of that char remaining), delete dict entry too
                if not check[nextChar]: del check[nextChar]

                # Update the new current index, update remaining length too
                currIndex = nextI
                remWord -= 1

            # Updating output word + length
            # If we checked off all letter of the word, then update it
            # Condition for checking lexograph
            if remWord == 0:
                # Do lexographic check
                if len(word) == longestLength:
                    # Sort the words and take the one that comes first!
                    output = sorted([output, word])[0]

                else:
                    output = word
                    longestLength = len(word)

        # Return the longest word
        return output 

