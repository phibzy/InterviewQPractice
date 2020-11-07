#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Nov 05, 2020 12:54:14 AEDT
  @file        : minHeight

"""

import logging, sys

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
        
        # Step 1 - get degrees of each node
        degrees = [ [i, 0] for i in range(n)]
        maxDegreeNode = 0
        maxDegree = 0
        
        for i, j in edges:
            degrees[i][1] += 1
            degrees[j][1] += 1

            if degrees[i][1] > maxDegree:
                maxDegree = degrees[i][1]
                maxDegreeNode = i

            if degrees[j][1] > maxDegree:
                maxDegree = degrees[j][1]
                maxDegreeNode = j
        
        # Prune until <= 2 nodes
        # THINK INDUCTION - THINK ABOUT CASE N = 1 and N = 2 and tackle tomorrow :)
        while len(edges) > 1:
            toPrune = dict()
            for i, d in degrees:
                if d == 1: toPrune[1] = True

            j = 0
            while j < len(edges):
                logging.debug(f"edges is {edges}")
                logging.debug(f"degrees is {degrees}")
                logging.debug(f"j is {j}")
                logging.debug(f"edges[j][0] is {edges[j][0]}")
                logging.debug(f"edges[j][1] is {edges[j][1]}")

                if (edges[j][0] in toPrune) or (edges[j][1] in toPrune):
                    degrees[edges[j][0]][1] -= 1
                    degrees[edges[j][1]][1] -= 1

                    del edges[j]

                else:
                    j += 1

        if not edges:
            return [maxDegreeNode]

        return edges[0]

a = Solution()
print(a.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
