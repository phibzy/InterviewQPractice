#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Nov 05, 2020 12:54:14 AEDT
  @file        : minHeight

"""

import logging, sys
from collections import deque

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
# logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logging.disable(logging.DEBUG)

class Solution:
    def findMinHeightTrees(self, n, edges):
        # handle the no edges case
        if not edges: return [0]
        
        # If only one edge, then minimum trees are both indices in that edge
        if len(edges) == 1: return edges[0]
        
        # Pruning leaves solution
        # We only care about those nodes of highest degree
        # There will always be at most two root nodes that produce the minHeight tree
        # We simply prune away leaves (i.e. nodes of degree 1) until we have <= 2 nodes left
        
        # Step 1 - create adj list for graph        
        graph = [dict() for _ in range(n)]

        for i, j in edges:
            graph[i][j] = 1
            graph[j][i] = 1


        # Create queue and add the first batch of leaves
        newQ = deque()
        for i in range(len(graph)):
            # Leaves are nodes connected to only one other node
            # I.e. of degree 1
            if len(graph[i]) == 1:
                newQ.append(i)

        # While number of nodes left is greater than 2
        # Prune leaves
        while n > 2: 
            q = newQ
            newQ = deque()
            while q:
                nextNode = q.popleft()

                # Delete edge connected to leaf node
                for edge in graph[nextNode]:
                    del graph[edge][nextNode]

                    # Check if newly pruned edge neighbour is now a leaf
                    # Add to next batch of leaves if it is
                    if len(graph[edge]) == 1:
                        newQ.append(edge)
            
                n -= 1
        
        return list(q)
