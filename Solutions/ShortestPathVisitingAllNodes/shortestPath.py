#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Feb 22, 2021 11:54:30 AEDT
  @file        : shortestPath

"""

from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        # One approach (brute forcy):
        """
        Pure Brute force
        
        Dijkstra's from every starting position
        Use set to keep track of visited positions
        
        Early exit if next smallest path is already greater than weight of
        current shortest path
        
        Way to mark dead ends? Use hash
        
        """
        
        # Conidition for one node graph or one edge graph
        # Optimal path will either be itself or one node to the next
        # node
        if len(graph) <= 2:
            return len(graph) - 1
        
        shortestWeight = float('inf')
        
        for i in range(len(graph)):
            q = deque()
            # print(''.rjust(10, '-'))
            # print(f"Starting from node {i}")
            # print(''.rjust(10, '-'))
            # print()
            # print()
            
            # Append starting index, weight, path taken and starting visited set
            q.append((i, 0, dict(), set([i])))
            
            # Keep going until we have a path that's visited
            # all nodes
            while True:
                # print(''.rjust(10, '*'))
                # print("Next iteration")
                # print(f"Current q: {q}")
                # print(''.rjust(10, '*'))
                # print()

                n, weight, deadEnds, seen = q.popleft()
                numDead = 0
                # print(f"Currently at node: {n}")
                
                # If next smallest path is greater than current
                # shortest path length, no point continuing
                if weight >= shortestWeight: break
                    
                # Add current node to set
                seen.add(n)
                
                # If visited every node, we can stop this check
                if len(seen) == len(graph):
                    shortestWeight = weight
                    break
                
                # Add to dead ends if we've reached end of a direction
                if len(graph[n]) == 1:
                    deadEnds[n] = 1

                # If only one option that's not a dead end, then
                # this node also becoomes a dead end
                numDead = len([x for x in graph[n] if x in deadEnds])

                if len(graph[n]) - numDead == 1:
                    deadEnds[n] = 1
                    
                for neighbour in graph[n]:
                    if neighbour not in deadEnds:
                        self.addToQ(neighbour, weight + 1, deadEnds.copy(), seen.copy(), q)
                
        return shortestWeight
            
    def addToQ(self, n, w, d, seen, q):
        k = 0
        
        while k < len(q) and q[k][1] <= w:
            k += 1
            
        q.insert(k, (n, w, d, seen))        
