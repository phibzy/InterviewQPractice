#!/usr/bin/python3


"""
Takes a string and a number of rows and prints out the zigzagged
version on a single line. E.g.

convert(s, numRows) = convert("PAYPALISHIRING", 3)

Output: PAHNAPLSIIGYIR

(pictured)

P   A   H   N
A P L S I I G
Y   I   R

"""


# Prints out zigzag output of given string/rows
def printZigZag(s, numRows):
    pass



def convert(s, numRows):
    i = 0
    row = 0
    add = 1
    length = len(s)

    if numRows == 1: return s

    outputRows = [ '' for j in range(numRows) ]

    # Time Complexity  = O(N + numRows)
    # Space Complexity = O(numRows)
    while i < length:
        outputRows[row] += s[i]
        row += add
        if row == 0 or row == (numRows - 1):
            add *= -1
        i += 1

    result = ''.join(outputRows)

    return result 
