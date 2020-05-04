#!/usr/bin/python3

"""
Given a string, find the longest substring without repeating characters.

Just needs to return an int, not the substring itself

"""

import logging

logging.basicConfig(level=logging.DEBUG, format = "%(levelname)s - %(message)s")

def lengthOfLongestSubString(s: str) -> int:
    longestLength = 0
    sLength = len(s)

    # If string is empty return zero
    chars = dict()
    i = 0
    startIndex = 0

    while i < sLength:
        if s[i] in chars and chars[s[i]] >= startIndex:
            logging.debug(f"i, s[i] is {i}, {s[i]}")

            startIndex = chars[s[i]] + 1
                
        # Adds char to hashmap, with its value being the index of its location
        chars[s[i]] = i

        logging.debug(f"i, s[i], chars[s[i]] is {i}, {s[i]}, {chars[s[i]]}")

        longestLength = max(longestLength, i - startIndex + 1)

        i += 1

    return longestLength
