#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Sep 07, 2020 14:00:26 AEST
  @file        : numNodesInSubtree

"""

from operator import add

class Solution:

    def countSubTrees(self, n, edges, labels):
        retArray = [0 for _ in range(n)]
        graph = [ Node(labels[i]) for i in range(n) ]
        
        # create graph
        for start, end in edges:
            graph[start].addSubNode(end)
            graph[end].parent = start
           
        # dfs to bottom 
        _ = self.dfs(0, graph, retArray, labels, n)

        return retArray

    def dfs(self, curr, graph, retArray, labels, n):
        sums = [0] * n

        sums[ord(labels[curr]) - ord('a')] += 1

        # for each subnode, add frequency list
        for adj in graph[curr].subNodes:
            l = self.dfs(adj, graph, retArray, labels, n)
            sums = list(map(add, sums, l))

        retArray[curr] = sums[ord(labels[curr]) - ord('a')]

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

