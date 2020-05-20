#!/usr/bin/python3

"""
Takes in a 2D list graph of 'X's and 'O's

Flip all 'O's that are surrounded by X's

A 'O' is surrounded if it is not connected horizontally or vertically
to a 'O' that is on the border of the graph

"""


class Solution:
    def solve(self, board):
        if board == []: return
        rows = len(board)
        cols = len(board[0])
        if rows <= 2 or cols <= 2:
            return

        visited = [ [False for _ in range(cols)] for _ in range(rows) ]
        
        for x in range(rows):
            for y in range(cols):
                if visited[x][y]: continue
                if board[x][y] == 'X':
                    visited[x][y] = True
                    continue
                
                s = list()
                history = list()
                s.append((x,y))
                borderFlag = False

                while s:
                    nx, ny = s.pop()
                    if visited[nx][ny]: continue
                    if board[nx][ny] == 'X':
                        visited[nx][ny] = True
                        continue

                    if (nx == 0 or nx == rows-1) or (ny == 0 or ny == cols-1):
                        borderFlag = True

                    if (nx - 1 >= 0): s.append((nx-1, ny))
                    if (nx + 1 < rows): s.append((nx+1, ny))
                    if (ny - 1 >= 0): s.append((nx, ny-1))
                    if (ny + 1 < cols): s.append((nx, ny+1))

                    history.append((nx,ny))
                    visited[nx][ny] = True

                if not borderFlag:
                    for nx, ny in history:
                        board[nx][ny] = 'X'






        
