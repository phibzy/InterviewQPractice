#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Feb 17, 2021 09:13:35 AEDT
  @file        : shortestPath

"""

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        # Dijkstra's - but since all weights are 1, a BFS = Djikstra's
        # Can only go through 0 blocks
        # Return -1 if no path

        # Consts for length of dimensions
        Y_MAX = len(grid)
        X_MAX = len(grid[0])

        # Solution 1: BFS (iterative)
        # Keep track of which blocks we've visited
        visited = dict() 

        # For Dijkstra's, the value of each key in the visited
        # hash will be the smallest weight for that location
        # TL;DR if we've already been to a grid location using a quicker
        # path, then a longer path to the same location won't be the shortest
        # path to our eventual destination

        # Queue values will be tuples of x/y coords + total path weight thus far
        q = deque()
        q.append((0, 0, 0))

        while q:
            y, x, weight = q.popleft()

            # Check if it's a 0 value
            # Ignore it if way is blocked
            if grid[y][x] == 1 : continue

            # If we've visited before with a shorter path,
            # skip current path
            if (y,x) in visited:
                if visited[(y,x)] <= weight: continue

            # Add to visited
            visited[(y,x)] = weight

            weight += 1

            # Return weight if we made it to the end
            if y == Y_MAX - 1 and x == X_MAX - 1:
                return weight


            # Add all neighbour nodes
            # Within bounds of grid dimensions
            # +2 used on second arg of range since range doesn't
            # include endpoints

            # Find index for current weight insertion
            i = 0
            while i < len(q) and q[i][2] <= weight:
                i += 1

            for nextY in range(max(0, y-1), min(y+2, Y_MAX)):
                for nextX in range(max(0, x-1), min(x+2, X_MAX)):
                    # Insert at index according to weight value
                    # to maintain priority q
                    q.insert(i, (nextY, nextX, weight))

        return -1
