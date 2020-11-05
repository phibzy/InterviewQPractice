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
        
        # O(N^3) solution
        # Check every possible root, DFS/BFS based on height
        
        minRoots = list()
        minHeight = n
        
        for root in range(n):

            logging.debug(f"Root is {root}")
            # Make copy of edges for search
            searchList = edges[:]
            nextMinHeight = 0
            
            # Keep track of height
            nextNode = [(root,0)]
            heightExceed = False
            nextHeight = 0
            
            # early exit if height exceeds minHeight
            while searchList and heightExceed == False:
                i = 0
                logging.debug(f"searchList is {searchList}")

                while i < len(searchList):
                    logging.debug(f"i is {i}")
                    logging.debug(f"Nextnode[0] is {nextNode[0]}")
                    logging.debug(f"searchList[{i}] is {searchList[i]}")

                    if searchList[i][0] == nextNode[0][0]:
                        logging.debug("First if")
                        nextHeight = nextNode[0][1] + 1
                        nextNode.append((searchList[i][1], nextHeight))
                        del searchList[i]
                                        
                    elif searchList[i][1] == nextNode[0][0]:
                        logging.debug("Second if")
                        nextHeight = nextNode[0][1] + 1
                        nextNode.append((searchList[i][0], nextHeight))
                        del searchList[i]

                    else:
                        i += 1

                    nextMinHeight = max(nextMinHeight, nextHeight)

                    logging.debug(f"nextHeight is {nextHeight}")
                    logging.debug(f"nextMinHeight is {nextMinHeight}")
                    logging.debug(f"minHeight is {minHeight}")
                    
                    # Don't bother continuing if already exceeded a previous minHeight tree
                    if nextHeight > minHeight:
                        logging.debug("And I'm about to break!")
                        heightExceed = True
                        break

                del nextNode[0]

            logging.debug(f"minRoots is {minRoots}")
                           
            if nextMinHeight < minHeight:
                minHeight = nextMinHeight
                minRoots = [root]
            
            elif nextMinHeight == minHeight:
                minRoots.append(root)
            
                    
        return minRoots

a = Solution()

print(a.findMinHeightTrees(5, [[0,1],[0,2],[0,3],[3,4]]))
