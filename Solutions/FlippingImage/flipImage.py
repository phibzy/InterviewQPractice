#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Nov 11, 2020 10:37:03 AEDT
  @file        : flipImage

"""


# TC: O(N^2) - We go through N/2 elements in N rows
class Solution:
    def flipAndInvertImage(self, A):
        """
        Basic gist - compare mirror elements in each row


        If the elements being compared are not equal, we
        don't need to change them since they'll be inverted
        after the swap anyway. Only invert them if they're equal
        """

        for row in range(len(A)):
            start, end = 0, len(A) - 1
            while end > start:
                # flip bits if they're equal
                if A[row][start] == A[row][end]:
                    A[row][start] ^= 1
                    A[row][end] ^= 1

                start += 1
                end -= 1
            
            # for odd lengths we need to flip the middle bit
            if end == start: A[row][start] ^= 1

        return A




