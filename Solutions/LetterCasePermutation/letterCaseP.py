#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Feb 18, 2021 11:39:20 AEDT
  @file        : letterCaseP

"""

# Will letters be the only characters in this string?
# What characters will we see?
# At the start, can letters be either lower/uppercase?
# Empty string?
# Range of length of string? - depending on which may elimiinate recursive solution
# If ask to change case manually, either - 'a' or + ('A' - 'a')


#TC: O(2^N) - Worst case, every letter is a digit, meaning we iterate through
# 2^N possibilities
# SC: O(2^N) - We have to creeate a list of size 2^N worst case

class Solution:
    def letterCasePermutation(self, S):
        # Can use recursion since upper limmit is low
        # Have an output list, pass reference to it for recursive calls
        # Pass new preceding string each time
        lastIndex = len(S) - 1

        return self.createPerms(S, 0, lastIndex)

    # Bit of back tracking
    # Go all the way to the end, then check if char is a letter
    # if it is, then return list with upper and lowercase variant
    # Otherwise just return list containing char

    # Idea is to create list of possible suffixes at each level,
    # then create all possible cobinations of suffic with next char
    def createPerms(self, s, i, lastI):
        # If no more characters, we donezo
        if i > lastI: return ['']

        # If it's a digit, no need to worry about other possibilities
        ch = s[i]
        possibilities = [ch]

        if self.isLetter(ch):
            # Add the opposite case to the possibilities list
            diff = ord('a') - ord('A')

            if ch < 'a':
                ch = chr(ord(ch) + diff) 

            else:
                ch = chr(ord(ch) - diff)

            # Add new case letter to possibilities
            possibilities.append(ch)

        output = list()

        for suffix in self.createPerms(s, i + 1, lastI):
            for letter in possibilities:
                output.append(letter + suffix) 

        return output

    def isLetter(self, c):
        # Since only possible chars are letters and digits,
        # we can do this easy comparison and ignore the rest
        return 'A' <= c <= 'z'

