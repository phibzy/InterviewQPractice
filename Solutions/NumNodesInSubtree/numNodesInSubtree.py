#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Sep 07, 2020 14:00:26 AEST
  @file        : numNodesInSubtree

"""

from operator import add
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
logging.disable(logging.DEBUG)

class Solution:

    def countSubTrees(self, n, edges, labels):
        retArray = [0 for _ in range(n)]
        graph = [ Node(labels[i]) for i in range(n) ]
        visited = dict()
        
        # create graph
        # NOTE: Tree representations are undirected graphs
        # Have to use visited
        # This problem is laid out so misleadingly, even if they specified undirected graph

        # Check parents during every DFS, set 0's parent to -1
        for start, end in edges:
            graph[start].addSubNode(end)
            graph[end].addSubNode(start)

        graph[0].parent = -1
        # dfs to bottom 
        _ = self.dfs(0, graph, retArray, labels, n, visited)


        return retArray

    def dfs(self, curr, graph, retArray, labels, n, visited):
        sums = [0] * 26

        logging.debug(f"curr is {curr}, labels[curr] is {labels[curr]}")
        logging.debug(f"ord val of curr is {ord(labels[curr])}, minus {ord('a')} is {ord(labels[curr]) - ord('a')}")

        sums[ord(labels[curr]) - ord('a')] += 1

        logging.debug(f"sums {curr} is {sums}")

        # for each subnode, add frequency list
        for adj in graph[curr].subNodes:
            if adj == graph[curr].parent: continue
            graph[adj].parent = curr
            l = self.dfs(adj, graph, retArray, labels, n, visited)
            sums = list(map(add, sums, l))

        retArray[curr] = sums[ord(labels[curr]) - ord('a')]


        logging.debug(f"sums {curr} is {sums} just before return")

        return sums


class Node:
    def __init__(self, label):
        self.label = label
        self.subNodes = list()
        self.parent = None
        self.sumLabels = dict()
        self.sumLabels.setdefault(self.label, 1)
    
    def addSubNode(self, n):
        self.subNodes.append(n)


a = Solution()

# a.countSubTrees(8, [[0,1],[1,2],[2,3],[1,4],[2,5],[2,6],[4,7]], "leetcode")

print(a.countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed"))
