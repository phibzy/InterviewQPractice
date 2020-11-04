#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Nov 04, 2020 13:11:03 AEDT
  @file        : conChar

"""

class Solution:
    def maxPower(self, s):
        # # Start with braindead O(N) solution
        maxPower = 1
        # power = 0
        # checkChar = s[0]

        # for i in s:
            # if i == checkChar:
                # power += 1
                # maxPower = max(maxPower, power)

            # else:
                # checkChar = i
                # power = 1

        # return maxPower

        # Improvement: we only need to check next substrings of greater length than maxPower
        start = 0
        end = 0

        while end < len(s):
            # Check if endpoints are equal, iterate inwards
            if self.checkSubStr(s, start, end):
                while end < len(s) and s[end] == s[start]:
                    maxPower = max(maxPower, (end - start + 1))
                    end += 1

                if end >= len(s): break

                # New end is end + maxPower, which is 1 length greater than current
                # largest substring
                start, end = end, end + maxPower

            else:
                start += 1
                end += 1


        return maxPower
    
    def checkSubStr(self, s, start, end):
        checkChar = s[start]

        while end >= start:
            if s[end] != checkChar or s[start] != checkChar:
                return False

            end -= 1
            start += 1

        return True

