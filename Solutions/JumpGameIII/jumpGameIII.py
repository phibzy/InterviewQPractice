#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Nov 30, 2020 18:05:13 AEDT
  @file        : jumpGameIII

"""

# TC: O(N) - Worst case the only path available is one that visits each element
# SC: O(N) - Same as above, resulting in N recursive calls on the stack

class Solution:
    def canReach(self, arr, start):
        # DFS, using visited dict 
        visited = dict()

        return self.reachDFS(arr, start, visited)

    def reachDFS(self, arr, start, visited):
        # If we've been to this index before, dw
        if start in visited: return False

        # Otherwise if we've found 0, we're done!
        if arr[start] == 0: return True

        # Add to visited
        visited[start] = True

        # We're not allowed to go beyond ends of array,
        # so check bounds before making search calls
        l = False
        if start + arr[start] < len(arr): 
            l = self.reachDFS(arr, start + arr[start], visited)

        r = False
        if start - arr[start] >= 0: 
            r = self.reachDFS(arr, start - arr[start], visited)

        # Return if we find a path in either direction
        return l or r

