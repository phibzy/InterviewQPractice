#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Feb 17, 2021 09:13:35 AEDT
  @file        : shortestPath

"""

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        # Djikstra's - but since all weights are 1, a BFS = Djikstra's
        # Can only go through 0 blocks
        # Return -1 if no path

        # Consts for length of dimensions
        Y_MAX = len(grid)
        X_MAX = len(grid[0])

        # Solution 1: BFS (iterative)
        # Keep track of which blocks we've visited
        visited = dict() 

        # Queue values will be tuples of x/y coords + total path weight thus far
        q = deque()
        q.append((0, 0, 0))

        while q:
            y, x, weight = q.popleft()

            # Check if it's a 0 value
            # Ignore it if way is blocked
            if grid[y][x] == 1 or (y,x) in visited: continue

            weight += 1

            # Return weight if we made it to the end
            if y == Y_MAX - 1 and x == X_MAX - 1:
                return weight

            # Add to visited
            visited[(y,x)] = 1

            # Add all neighbour nodes
            # Within bounds of grid dimensions
            # +2 used on second arg of range since range doesn't
            # include endpoints
            for nextY in range(max(0, y-1), min(y+2, Y_MAX)):
                for nextX in range(max(0, x-1), min(x+2, X_MAX)):
                    q.append((nextY, nextX, weight))

        return -1
