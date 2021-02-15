#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Feb 15, 2021 12:03:48 AEDT
  @file        : numSteps

"""

"""
Extra:
    If the question instead had an array of numbers which we had to calculate,
    we could use memoisation with a dict to speed up the process whenever we
    encounter a number we've seen before

"""

# Basic solution
class Solution:
    def numberOfSteps (self, num: int) -> int:
        # use mod to check if even/odd, then perform operation
        steps = 0
        
        while num != 0:
            if num % 2 == 0:
                num //= 2
            
            else:
                num -= 1
            
            steps += 1
                
        return steps

"""
Binary Analysis Solution:
    We can look at the binary representation of the number
    and work out how steps we need to take. To reach zero
    we would have to bit shift right (aka divide by 2) by a number
    of times equal to how many binary digits we have.

    However, every input number (except 0) will reach 1 on the penultimate
    step (because we're halving and binary number will start with 1). We also know
    that every time we bit shift and there's a 1 in the 2**0 column, we have an add number.

    Continuing this train of thought, we can look at the number of 1s in the binary number
    to see how many times we will have to do the -1 step.

    So our formula for a solution is: number of times we can halve it + number of times we need to minus 1

    In other words: Number of digits + number of 1 digits - 1 (since we can't shift the last digit, it will always be 1)

"""

# Binary analysis solution
class Solution:
    def numberOfSteps (self, num: int) -> int:
        # Count binary digits
        # Minus two for "0b" part, minus another one for not being able to
        # halve on the last step
        digits = len(bin(num)) - 3
        num1s = len([x for x in bin(num) if x == "1"])
        
        return digits + num1s

