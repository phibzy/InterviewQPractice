#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Jun 22, 2020 18:00:30 AEST
  @file        : kthAncestor


You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where
parent[i] is the parent of node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th
ancestor of the given node. If there is no such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.


"""


# Time Complexity: O(N^2)?
# Space Complexity: O(NlogN) - N nodes in hash, with at most logN elements in their list
#                            - You will have at most the height of the tree in each list
class TreeAncestor:

    def __init__(self, n, parent):
        self.known  = dict()
        self.parent = parent
        self.size = n
        
        i = self.size - 1
        
        while i > 0:
            children = list()
            if i not in self.known:
                self.known[i] = list()
                self.populate(i, 0, children)
                
            i -= 1
              
    def populate(self, node, level, children):
        nextNode = self.parent[node]
        children.append(node)
        
        for child in children:
            self.known[child].append(nextNode)
            if nextNode in self.known:
                self.known[child] += self.known[nextNode]    
        
        if (nextNode not in self.known) and nextNode != 0:
            self.known[nextNode] = list()
            self.populate(nextNode, level + 1, children)
            
            
        
    def getKthAncestor(self, node, k):
        if node == 0: return -1
        if k > len(self.known[node]): return -1
        k = k-1
        
        # Use array, so change this to k-1 once it's going dawg
        return self.known[node][k]
