#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Nov 17, 2020 12:33:26 AEDT
  @file        : longestMountain

"""

# Remember: return length of mountain if there is one

# TC: O(N) - We check all the elements
# SC: O(1) - We use same amount of space regardless of input

# Improvement: Have early exit if starting an ascension and there's
#              not enough remaining elements to overtake maxLength

class Solution:
    def longestMountain(self, A):
        # If there's less than 3 elements, it's impossible
        # to have a mountain
        if len(A) < 3: return 0

        maxLength = 0
        startIndex = 0

        # asc flag is used to mark when we're going up a peak
        # We need it in case we're just constantly descending or descending from
        # flat land
        asc = False

        # Flag to tell us if we're descending
        # Use it for resetting the starting index of the current subarray
        des = False

        i = 0

        # Use next index for calculating length
        while (i + 1) < len(A):
            nextVal = A[i+1]
            curr    = A[i]

            # If we're going up a slope
            if nextVal > curr:
                # if we were just descending, update our start index
                if des:
                    startIndex = i
                    des = False

                asc = True

            # We're on flat land, so reset our flags
            # startIndex = i+1 since i cannot be the start of a mountain
            elif nextVal == curr:
                asc, des = False, False
                startIndex = i + 1

            # Otherwise we're descending
            else:
                des = True

                # Only check for new max subarray length if we're coming down
                # from a peak
                if asc:
                    maxLength = max(maxLength, (i - startIndex + 2))            
         
            i += 1

        return maxLength

