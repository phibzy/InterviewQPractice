#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Feb 23, 2021 12:50:12 AEDT
  @file        : romanToInt

"""

class Solution:
    def romanToInt(self, s):
        # First, create a dict of Roman Numeral values
        val = { 
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
              }

        # The number we return
        output = 0 

        # Go through each char index
        # Convert it's value and then add to output

        # Look ahead to see if next char value is greater than
        # current char's value - this will be the IX cases etc.
        # For these cases, add val[next] - val[curr] to output then
        # skip next index
        i = 0
        while i < len(s):
            if i + 1 < len(s) and val[s[i]] < val[s[i+1]]:
                output += (val[s[i+1]] - val[s[i]])
                i += 2

            # Otherwise just convert and add
            else:
                output += val[s[i]]
                i += 1

        return output

