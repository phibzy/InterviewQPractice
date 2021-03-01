#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Mar 01, 2021 12:23:54 AEDT
  @file        : divideTwoInts

"""

"""
Questions:
    - Two integers?
    - Can either be negative?
    - Range of vals?
    - Max range of result?
    - Will always be divisible? Or do we have to handle remainders too?
    - If not, do we floor/ceiling?
    - Will we have to deal with divide by 0?


"""

"""
    Algo:

    If dividend is less than divisor, result will truncate to 0

    Otherwise, we will keep subtracting divisor from dividend until
    dividend < divisor. We then return however many times we subtracted.

    For handling negatives, use a var neg = 1

    If first number is neg, *= -1
    If second number is neg, *= 1

    We will multiply result by neg at the end

    Need to be careful about overflow cases though...


"""

# TC: O(N) - Worst case we divide a number by -1 or 1,
#            requiring N steps

class Solution:
    def divide(self, dividend, divisor):
        neg = 1


        # Just realised can't do this because not allowed to use multiplication
        # if dividend < 0: neg *= -1
        # if divisor < 0:  neg *= -1

        # Make both numbers abs values
        # dividend, divisor = abs(dividend), abs(divisor)

        # For 1/-1 cases to avoid TLE
        # if abs(divisor) == 1: return dividend**divisor

        # Keep track of how many times we subtracted
        steps = 0
        addFlag = ((divisor < 0 and dividend >= 0) or (divisor > 0 and dividend < 0))

        # print(addFlag)

        while abs(dividend) >= abs(divisor):
            # If only one number is negative, then you want to add instead
            if addFlag :
                dividend += divisor
                steps -= 1

            else:    
                dividend -= divisor
                steps += 1
        
        # Condition for overflow here lol
        if steps < -2**31 or steps > 2**31 - 1: return 2**31-1

        return steps

