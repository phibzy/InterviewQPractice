#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Nov 25, 2020 11:44:11 AEDT
  @file        : basicCalcII

"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

class Solution:
    def calculate(self, s):
        return self.rCalculate(s, 0)

    def rCalculate(self, s, i):
        # Grab first number, put it into result
        # then go from there
        i, result = self.getNum(s, i)

        while i < len(s):
            # Check what our operator is
            sign = s[i]

            # A number MUST follow an operator otherwise it's invalid
            i, num = self.getNum(s, i+1)

            # Don't need to worry about order of ops for multiplication/division
            if sign == "*":
                result = result * num

            elif sign == "/":
                result = result // num

            # We do for addition/subtraction though 
            else:
                # Check if next operator is * or /
                # Keep making calculation until you either reach
                # end of string or the next operator isn't / or *
                while i < len(s):
                    nextSign = s[i]
                    if (nextSign != "*") and (nextSign != "/"): break

                    i, nextNum = self.getNum(s, i+1)

                    if nextSign == "*":
                        num *= nextNum

                    else:
                        num //= nextNum

                # num will now be the result of any more important operations
                # so we can now add or minus it from our result without worry
                if sign == "+": result += num
                else: result -= num

        return result

    # Grabs the next number and skips over any whitespace before next operator
    # Returns the number and the new index of string pointer
    def getNum(self, s, i):
        num = 0
        while i < len(s) and ("0" <= s[i] <= "9" or s[i] == " "):
            if s[i] != " ":
                num = num*10 + int(s[i])

            i += 1

        return (i, num)

