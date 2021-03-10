#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Mar 10, 2021 10:33:12 AEDT
  @file        : encode

"""

"""
Qs:
    - Min/Max amount of words?
    - Min/max length of words?
    - If I understand correctly, we're basically interested in suffixes?
    - Are we returning indices array? Just min length?
    - Are words unique?
    - What chars in words?

"""

"""
Algo:
    - Sort by size smallest to largest
    - Have counter keeping track of total length of words + num words (for each hash)
    - Check if next smallest is in the equal length suffix of other words
    - If it is in any of them, subtract length of word + 1 (+ 1 for the hash character saved)

    TC: O(N^2 + L) - where N is number of words, L is max length of words
                   - Worst case you have 7 words of length 2000 and you compare
                     each char

"""

class Solution:
    def minimumLengthEncoding(self, words):
        # Sort alphabetically, then by size
        words.sort()
        words.sort(key=len)

        totalLength = sum([len(x) for x in words]) + len(words)

        # For each word
        for i, word in enumerate(words):
           
            # Check whether it's a suffix in the rest of the words
            for checkWord in words[i+1:]:
                if word == checkWord[-len(word):]:
                    totalLength -= (len(word) + 1)
                    break

        return totalLength

