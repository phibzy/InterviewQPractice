#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Nov 04, 2020 13:11:03 AEDT
  @file        : conChar

"""

class Solution:
    def maxPower(self, s):
        # Start with braindead O(N) solution
        maxPower = 1
        power = 0
        checkChar = s[0]

        for i in s:
            if i == checkChar:
                power += 1
                maxPower = max(maxPower, power)

            else:
                checkChar = i
                power = 1

        return maxPower

        # Improvement: we only need to check next substrings of greater length than maxPower
        start = 0
        end = 1

        while end <= len(s):
            # Check if endpoints are equal, iterate inwards


        # Another idea, sort substring and check if endpoints equal


