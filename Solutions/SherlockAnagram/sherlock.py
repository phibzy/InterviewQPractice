#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Jun 18, 2020 16:50:40 AEST
  @file        : sherlock

"""

from collections import deque

# Complete the sherlockAndAnagrams function below.
# Time Complexity - O(N^3logN)
# Space Complexity - O(N)


# Originally tried sliding window with string sums
# That approach is fine, eventually got too annoyed/frustrated
# and just bruteforced it
def sherlockAndAnagrams(s):
    # We know that the max size of an anagram is len(s) / 2
    # Since it's impossible to have anything larger
    maxPairSize = len(s) - 1
    result = 0
    # startSum = 0
    startString = deque()

    for i in range(maxPairSize):
        start = 0
        end = start + i
        anagram = dict()

        #startSum    += ord(s[end])
        startString.append(s[end])
        subStr = startString.copy()
        anagram[str(sorted(subStr))] = 1
        end += 1
        while end <= maxPairSize:
            # I think best way to do this:
            # Track of character orders
            # Insert new character in sorted position
            subStr.popleft()
            subStr.append(s[end])

            sHash = str(sorted(subStr))

            # Sliding window, add on next character, drop first character            
            #aSum = aSum - ord(s[start]) + ord(s[end])

            if sHash in anagram:
                
                result += anagram[sHash]
                anagram[sHash] += 1





            else:
                anagram[sHash] = 1

            start += 1
            end += 1

    return result
