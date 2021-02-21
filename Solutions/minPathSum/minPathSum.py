#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Feb 21, 2021 12:16:47 AEDT
  @file        : minPathSum

"""

from collections import deque

# We get given an adjacency matrix
# Can also only move down or right at any point in time

# Question for interview: negative values in grid? minimum size? m == n?

# Solution 1: typical Dijkstra's
class Solution1:
    def minPathSum(self, grid):
        # If 1x1, return weight of only square
        if len(grid) == len(grid[0]) == 1: return grid[0][0]

        # Otherwise, we'll run a modified Dijkstra's
        # Starting weight will be whatever starting square's value is
        pathWeight = 0 

        # Add coordinates to the queue with weight
        q = deque()

        # Use visited hash, which will store lowest path weight so far
        # to reach a given square
        visited = dict() 

        # q values will be coords with their current weight
        q.append((0,0,pathWeight))

        # If they ask for hash algo: x + y*1000
        visited[str((0,0))] = pathWeight

        # This should be while true tbh
        # This is safe since we know there will be a path
        while True:
            # Grab next item in queue
            y, x, pathWeight = q.popleft()

            # Add to visited
            visited[str((y,x))] = pathWeight

            # Update pathWeight with current square's value
            pathWeight += grid[y][x]

            # If we reach the bottom right corner, add the last
            # weight and return it
            if (y,x) == (len(grid) - 1, len(grid[0]) - 1):
                return pathWeight

            # Otherwise, we keep searching
            # Only need to check to the right and down though
            if y + 1 < len(grid):
                self.appendInOrder(q, y+1, x, pathWeight, visited)

            if x + 1 < len(grid[0]):
                self.appendInOrder(q, y, x+1, pathWeight, visited)

    # Append to q to maintain order of lowest pathweight first
    def appendInOrder(self, q, y, x, pathWeight, visited):
        if str((y,x)) in visited:
            # If we've found a shorter path to same spot,
            # we can ignore the current path
            if visited[str((y,x))] < pathWeight: return

        # Otherwise, add it to the q in the correct order
        k = 0
        while k < len(q) and pathWeight > q[k][2]:
            k += 1

        q.insert(k, (y, x, pathWeight))

# Solution 2 - DP, filling out squares with weights
class Solution:

    # Since we're only moving right and down, we can start
    # by filling the whole top row values and left column values
    # with how much it costs to reach that square. These values will
    # be the min weight to reach these points
    def minPathSum(self, grid):
        # Max dimensions
        maxY = len(grid)
        maxX = len(grid[0])

        # Step 1 - fill the the first row and column
        # Start at index 1 since we'll be adding whatever comes before
        for i in range(1, maxY):
            grid[i][0] += grid[i-1][0]

        # Fill top row as well
        for i in range(1, maxX):
            grid[0][i] += grid[0][i-1]

        # We then start at index 1,1
        # We add the minimum of the weights that are to the top and left or current position
        # Iterated across row and repeat for each row to fill grid with values
        for y in range(1, maxY):
            for x in range(1, maxX):
                grid[y][x] += min(grid[y][x-1], grid[y-1][x])

        # By the end of this, the value in the bottom right square
        # will be the cost of the shortest path
        return grid[-1][-1]





