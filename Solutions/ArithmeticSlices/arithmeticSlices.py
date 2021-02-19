#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Feb 19, 2021 11:42:20 AEDT
  @file        : arithmeticSlices

"""

# So, a sequence has to have 3 numbers minimum?
# Will there always be at least 3 numbers?
# Range for numbers?
# All possible slices in a given array?
# When you say difference, do you mean i - j or j - i or either?

# Case to consider - how many slices are added when another added to current slice


"""
Basic Algo:

    For consecutive numbers i, j, k

    If j - 1 == k - j, then we increment our totalSequences and then our currentSequenceCount

    The reason for this is our next number is also part of the current sequence, then we now
    have an additional sequence of length 4 as well as a new one of length 3.

    If we then add another number to our sequence, we have a new sequence of length 3, 4 and 5

    So everytime we increase our total sequences, we increase it by currentSeq + 1

    When we encounter a number that's not part of slice/sequence, we set currentSeq to 0 before continuing

    TC: O(N) - We visit every number in array once
    SC: O(1) - Use same amount of space regardless of input

"""

class Solution:
    def numberOfArithmeticSlices(self, A):
        # If there's not enough items to make a sequence
        # return 0
        if len(A) < 3: return 0
        
        # Starting indices
        i, j, k = 0, 1, 2

        # Total arithmetic slices
        totalSeq = 0

        # Length of current sequence, used to increment our count
        currSeq = 0

        diff = A[1] - A[0]

        while k < len(A):
            nextDiff = A[k] - A[j]

            # Naive approach first
            if diff == nextDiff:
                totalSeq = totalSeq + 1 + currSeq
                currSeq += 1

            # Otherwise end currentSeq
            else:
                currSeq = 0
                diff = nextDiff

            # print(f"Current comparison: {A[i]}, {A[j]}, {A[k]}")
            # print(totalSeq, currSeq)

            i += 1
            j += 1
            k += 1

        return totalSeq

