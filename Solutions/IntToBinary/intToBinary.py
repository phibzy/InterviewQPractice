#!/usr/bin/python3

"""
Given an integer, convert it into a binary string

Assume integer >= 0

Would ask interviewer max int size (in bits) - for today will assume 32

"""

def intToBinary(i):
    # Don't need multiplier because we're returning string
    result = ''

    if i == 0: return '0'

    # While number isn't zero, shift right
    # Get first binary digit using mask

    # This reverses binary digits LOL, wrong problem dude
    # while i != 0:
        # result += str(i&1)
        # i >>= 1

    # Extremely inefficent algorithm
    # Time complexity: O(N^2) - Has to allocate space for characters in each newly concatenated string
    # while i != 0:
        # result = str(i&1) + result
        # i >>= 1

    # Find highest power of two
    # Then subtract. If power of 2 goes into number then append '1'
    # If power of 2 greater than number at any iteration, append '0' instead

    # Time Complexity: O(D) - where D is the number of binary digits a number has
    j = i
    power = -1

    while j != 0:
        # print(f"j is {bin(j)}")
        j >>= 1
        power += 1

    while power >= 0:
        # print(f"power is {power}")
        # print(f"i is {i}")
        if (2**power) <= i: 
            result += '1'
            i -= 2**power

        else: result += '0'

        power -= 1

    return result
