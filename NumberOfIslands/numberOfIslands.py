#!/usr/bin/python3

"""
Given a 2D grid of 1s/0s, where 1 = land and 0 = water:

Count the number of islands

Island is land surrounded by water, assume area around grid is water

Diagonals don't count, only interested in horizontal/vertical neighbours

Questions to Interviewer:
    - Is land around grid assumed to be water?
    - Is Island definition only concerning vertical/horizontal squares? Diagonals too?
    - What's the max grid size? (stack overflow issues - to make sure recursion is on table or not)
    - What's the minimum grid size? Can grid be empty?
    - Surely grid will be completely filled? (i.e. no rows/columns with missing values)

Return int with number of islands

"""

#BFS - do one recursive and one iterative
import pdb

def checkValid(grid, y, x, val):
    rows = len(grid)
    cols = len(grid[0])

    return (0 <= y < rows and 0 <= x < cols and grid[y][x] == val)

def bfs(grid, visited, startX, startY):
    val = grid[startX][startY]

    q = list()

    q.append((startX, startY))

    while q:
        y, x = q.pop(0)
        if x in visited[y]: continue
        visited[y][x] = True

        # check for visited
        if checkValid(grid, y, x+1, val):
            q.append((y, x+1))

        if checkValid(grid, y+1, x, val):
            q.append((y+1, x))

        if checkValid(grid, y, x-1, val):
            q.append((y, x-1))

        if checkValid(grid, y-1, x, val):
            q.append((y-1, x))

    return int(val)


# Recursive DFS
def rDFS(grid, visited, x, y):
    # pdb.set_trace()
    if y in visited[x] or grid[x][y] == '0': return

    
    visited[x][y] = True

    if x - 1 >= 0: rDFS(grid,visited, x-1, y)
    if x + 1 < len(grid): rDFS(grid, visited, x+1, y)
    if y - 1 >= 0: rDFS(grid,visited, x, y-1)
    if y + 1 < len(grid[0]): rDFS(grid, visited, x, y+1)
    
    return 1

# Takes in 2D list of str, returns an int
def numIslands(grid):
    if grid == []: return 0

    visited = dict()
    for i in range(len(grid)):
        visited[i] = dict()

    # Start top left, check value, continue BFS until no more of said value  
    rows = len(grid)
    cols = len(grid[0])

    i = 0
    result = 0

    while i < rows:
        j = 0

        while j < cols:
            # Important note: You don't have to search all the 0's because they will return 0 anyway lmao
            if j in visited[i] or grid[i][j] == '0':
                j += 1
                continue

            result += rDFS(grid, visited, i, j) 
            j += 1


        i += 1
            
    return result

# numIslands([["1","0","0","0","1"],["0","1","0","1","0"],["0","0","1","0","0"],["0","1","0","1","0"],["1","0","0","0","1"]])
