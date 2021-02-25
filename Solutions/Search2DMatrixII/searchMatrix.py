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
Better Solution - (logN * logM)?
    Find range of rows where target could be
    Find range of cols where target could be
    Use binary search for both

    Binary search result?


"""

class Solution:
    def searchMatrix(self, matrix, target):
        startRow = 0
        startCol = 0
        endRow = len(matrix) - 1
        endCol = len(matrix[0]) - 1

        while 0 <= startRow <= endRow and 0 <= startCol <= endCol:
            # If target in top left, we win!
            if matrix[startRow][startCol] > target: return True

            # If top left corner is greater than target, it's not in matrix
            if matrix[startRow][startCol] > target: return False

            # Likewise, if target is greater than bottom right we can stop
            if matrix[endRow][endCol] > target: return False

            # Eliminate row possibilities
            startRow, endRow = binSearchRow(startRow, endRow, startCol, target)

            # Do same for cols
            startCol, endCol = binSearchCol(startCol, endCol, startRow, target)
                
        return False
    
    # Want to search for highest number row target could be in
    def binSearchRow(self, startRow, endRow, startCol, target):
        ogStart = startRow
        ogEnd   = endRow
        
        # Want to make sure that target is greater than start of rows
        while startRow < endRow:
            middleRow = startRow + (endRow - startRow) // 2

            # If target found, just return 1 row search space
            if matrix[middleRow][startCol] == target: return (middleRow, middleRow)

            # If target is less than middle, can't be in middle row
            if matrix[middleRow][startCol] > target: 
                endRow = middleRow - 1 

            # Otherwise, it can be in middle row
            else:
                startRow = middleRow

        # Resulting endRow will be last row target could be in
        return (ogStart, endRow)

    # Want to search for highest number col target could be in
    def binSearchCol(self, startCol, endCol, startRow, target):
        ogStart = startCol
        ogEnd   = endCol
        
        # Want to make sure that target is greater than start of rows
        while startCol < endCol:
            middleCol = startCol + (endCol - startCol) // 2

            # If target found, just return 1 row search space
            if matrix[startRow][middleCol] == target: return (middleCol, middleCol)

            # If end is less than, that's our end

            # If target is less than middle, can't be in middle row
            if matrix[startRow][middleCol] > target: 
                endCol = middleCol - 1 

            # Otherwise, it can be in middle row
            else:
                startCol = middleCol

        # Resulting endRow will be last row target could be in
        return (ogStart, endCol)







