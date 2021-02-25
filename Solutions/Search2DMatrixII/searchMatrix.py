#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Feb 25, 2021 10:47:38 AEDT
  @file        : searchMatrix

"""

# What's the min/max size of matrix? Can dimensions be unequal?
# Can there be an empty matrix?
# Is there any order to the elements? I.e. rows are sorted? Cols sorted?
# Range of values? Can we have negative numbers
# Do we return coordinates to the target? No, we return if it exists

# Values can be negative
# Min size will be 1x1
# Is target guaranteed to be in the matrix?
# Will values be unique in rows/cols?

"""
Brute Force:
    Search through every entry in matrix for target value,
    returning true if found.

    TC: O(N*M)

"""

"""
Better Solution - Focus on top left and bottom right vals

    Do binary search based on top left/bottom right vals, i.e. min/max vals
    Keep reducing matrix until of size 2*2 or less
    Then just check if it's in elements of remaining matrix


TC: O(log (N+M)) - we reduce the search space of each dimension by half
SC: O(1) - No extra space needed

"""

class Solution:
    def searchMatrix(self, matrix, target):
        startRow = 0
        startCol = 0
        endRow = len(matrix) - 1
        endCol = len(matrix[0]) - 1

        # Condition for empty matrix
        if not matrix or not matrix[0]: return False

        # If < lowest element or > largest element, we can stop too
        if target < matrix[0][0] or target > matrix[-1][-1]: return False

        # Reduce to 2x2 case
        while endRow - startRow + 1 > 2 and endCol - startCol + 1 > 2 :
            middleRow = startRow + (endRow - startRow) // 2
            middleCol = startCol + (endCol - startCol) // 2

            # If target in middle, we win!
            if matrix[middleRow][startCol] == target: return True

            # If in top left partition, reduce to that partition
            if matrix[startRow][startCol] <= target <= matrix[middleRow][middleCol]:
                endRow, endCol = middleRow, middleCol

            # Otherwise, reduce to bottom right partition
            else:
                startRow, startCol = middleRow, middleCol

        # Then check if in 2x2 or less matrix 
        return target in [x for y in matrix for x in y]
