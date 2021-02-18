#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Feb 18, 2021 10:56:16 AEDT
  @file        : kWeakestRows

"""
# Empty matrix case?
# Range of input for m and n?
# Only have 1s and 0s, that's it?
# Range of values for k? Is k=0 a possibility?
# Will k ever be larger than number of rows?


"""

Solution 1 O(N * M):

Go row by row, adding up total soldiers in each row,
then find the smallest k of those totals


"""

"""

Because soldiers will always be at the 'front' of each list,
we can search column by column through all rows starting at the first row.

Whenever we encounter a civilian, we append that row index to an output list
This means that even if all rows have equal power, the lower index will be lowest
in the list.

Along the way keep checking if we have k items in the list

If we've still got < k elements in output list once iterated through everything,
then go through matrix from row 0 and add any row index not already in list
until we have k elements

Use a hash to keep track of who's in list

TC: O(N*M)
SC: O(N)

"""

class Solution:
    def kWeakestRows(self, mat, k):
        # Output list
        output = list()

        # Keep track of valid rows, remove once
        # we don't need to check them anymore
        validRows = [i for i in range(len(mat)) ]

        # Move through column by column, row by row
        for col in range(len(mat[0])):
            i = 0

            # While there's still rows left to check
            while i < len(validRows):
                # Get the real index of the next row to check
                rowI = validRows[i]

                # If it's a civilian, then it's the next
                # weakest row. Append to list and remove
                # from rows we need to check
                if mat[rowI][col] == 0:
                    output.append(rowI)
                    del validRows[i]

                    # Early exit check
                    if len(output) == k: return output

                # Otherwise keep checking remeaining rows
                else:
                    i += 1

        # If we haven't returned yet, then len(output) < k
        # Keep adding validRows indices until we've got k indices
        i = 0
        while len(output) < k:
            output.append(validRows[i])
            i += 1

        return output

                










