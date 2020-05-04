#!/usr/bin/python3

"""
Given a string, find the longest substring without repeating characters.

Just needs to return an int, not the substring itself

"""

import logging

logging.basicConfig(level=logging.DEBUG, format = "%(levelname)s - %(message)s")

def lengthOfLongestSubString(s: str) -> int:
    length = 0
    longestLength = 0
    sLength = len(s)

    # If string is empty return zero
    if s != '':
        chars = dict()
        i = 0
        longestLength = 0
        startIndex = 0

        while i < sLength:
            if s[i] in chars:
                logging.debug(f"i, s[i] is {i}, {s[i]}")


                repeatIndex = chars[s[i]]

                logging.debug(f"repeatIndex is {repeatIndex}")

                newStartIndex = repeatIndex + 1

                # Remove everything in hash from repeat value backwards
                while repeatIndex >= startIndex:
                    logging.debug(f"About to delete chars[s[repeatIndex]] = chars[{s[repeatIndex]}] = {chars[s[repeatIndex]]}")
                    del chars[s[repeatIndex]]
                    repeatIndex -= 1
                    length -= 1

                startIndex = newStartIndex    
                    
            # Adds char to hashmap, with its value being the index of its location
            chars[s[i]] = i
            length += 1

            logging.debug(f"i, s[i], chars[s[i]], length is {i}, {s[i]}, {chars[s[i]]}, {length}")

            if length > longestLength:
                longestLength = length

            i += 1


    return longestLength
