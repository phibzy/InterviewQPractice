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

# Cool solution I saw on hackerRank - Use bits of int (Assuming 32-bit int) to indicate if letter in array
# Have some var = 0, then var |= 1 << char - 'a'. I.e. Sets bit according to number letter of alphabet
# Do twice for each string, then AND the two ints. If they share any letter result will be > 0
# Still O(N + M) but way cooler and depending on language super efficient operations
# Downside: It will always be O(N + M), my solution is only O(N+M) in worst case, it terminates
# when common letter is found

# Another alternative is sets, which is probably best solution in Python
