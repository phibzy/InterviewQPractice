#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Feb 17, 2021 15:26:43 AEDT
  @file        : isGraphBipartite

"""

from collections import deque

class Solution:
    # Each node numbered between 0 and 1
    # all unique vals
    # undirected graph, graph is list of list with connected vertexes
    # e.g. node 0 is connected to every node listed in graph[0]

    #TC: O(N^2) - We BFS (visit N nodes) from N different starting nodes
    #SC: O(N) - All nodes will be placed into a set

    def isBipartite(self, graph):
        # We will prove via contradiction
        # Create two sets, setA and setB
        # Do BFS from each node
        # Mark each node as being in either set A or set B by
        # placing val into hash
        # If a value is ever in both sets, we have a contradiction

        # Interesting case: isolated nodes - does that invalidate graph? No!
        
        # Create sets
        setA = dict()
        setB = dict()

        # Create references to each, which we will
        # be using in q and swapping around a bit
        pSet   = setA
        sSet = setB

        # Do BFS from every node
        for i in range(len(graph)):
            # If it has no edges, continue onto the next one
            if not graph[i]: continue

            pSet, sSet = setA, setB

            # If this node has already been placed in setB,
            # make setB the primarySet
            if i in setB:
                pSet, sSet = setB, setA

            # Create q and visited for BFS
            q = deque()
            visited = dict()
            q.append((i, pSet, sSet))

            # do BFS
            while q:
                nextNode, set1, set2 = q.popleft()

                # If isolated node, skip it
                if not graph[nextNode]: continue

                # If it's already in the other set, then can't be bipartite
                if nextNode in set2: return False

                # If we've already visited, we don't need to repeat
                # BFS from this node since it's in set1 already
                if nextNode in visited: continue

                # Add each connected node, make sure to swap sets around when
                # pushing to q to achieve alternating set checks
                for n in graph[nextNode]:
                    q.append((n, set2, set1))

                # Put value into set and mark as visited
                set1[nextNode] = 1
                visited[nextNode] = 1

        return True

