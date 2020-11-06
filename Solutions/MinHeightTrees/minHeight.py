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
        
        for i, j in edges:
            degrees[i][1] += 1
            degrees[j][1] += 1
        
        # Prune until <= 2 nodes
        # THINK RECURSION - THINK ABOUT CASE N = 1 and N = 2 and tackle tomorrow :)

        # Need to check edges instead...
        while len(degrees) > 2:
            # Use list of what to update because we only want
            # to prune leafs for each pass. If we update during pass
            # we will prune waaaaay too many nodes
            updateDegrees = list()
           
            i = 0
            while i < len(degrees):
                # Will always be a leaf node in our tree since no cycles
                if degrees[i][1] == 1:
                    while j < len(edges):
                        if edges[j][0] == i:
                            updateDegrees.append(edges[j][1])
                            del edges[j]
                            
                        elif edges[j][1] == i:
                            updateDegrees.append(edges[j][0])
                            del edges[j]
                            
                        else:
                            j += 1
                    
                    del degrees[i]

                i += 1
            
            for n in updateDegrees:
                degrees[n][1] -= 1
                
        return [ i for i, _ in degrees ] 
