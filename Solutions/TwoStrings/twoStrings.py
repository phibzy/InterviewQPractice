#!/usr/bin/python3

"""
Given two strings s1 and s2, check if they share any substrings

Note that a substring can be as small as a single character

"""


# Time Complexity: O(s1 + s2) - Worst case we have to check every character of each string
# Space Complexity: O(s1) - We create a hash with all the letters of first string

# Improvement: Check which string is smaller, use the smaller string for the hash to reduce space complexity


def twoStrings(s1, s2):
    # Because a substring can be as small as a single letter, the 
    # question is really: "Do these strings share any letters?"

    letters = dict()
    for i in s1:
        letters.setdefault(i, 1)

    for i in s2:
        if i in letters:
            return "YES"

    return "NO"
