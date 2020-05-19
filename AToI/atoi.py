#!/usr/bin/python3

"""
Takes a string and converts it to an integer

First discards all leading whitespace chars

Each string can have optional first char of '+' or '-' followed by numerical digits

If first char is not a digit, return 0

All chars after digits are ignored

If value is greater than max/minimum int value (32-bit signed range), return max/min int value instead

"""

# will only care about '0' <= '9'

class Solution:
    def myAtoi(self, s):
        total = 0
        negSign = 1
        multiplier = 1

        for i in range(len(s)):
            ch = s[i]
            if ch == ' ': continue
            if ch == '+' or ch == '-':
                i += 1
                ch = s[i]
                



        return total

