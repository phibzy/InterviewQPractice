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
# class TreeAncestor:

    # def __init__(self, n, parent):
        # self.known  = dict()
        # self.parent = parent
        # self.size = n
        
        # i = self.size - 1
        
        # while i > 0:
            # children = list()
            # if i not in self.known:
                # self.known[i] = list()
                # self.populate(i, 0, children)
                
            # i -= 1
              
    # def populate(self, node, level, children):
        # nextNode = self.parent[node]
        # children.append(node)
        
        # for child in children:
            # self.known[child].append(nextNode)
            # if nextNode in self.known:
                # self.known[child] += self.known[nextNode]    
        
        # if (nextNode not in self.known) and nextNode != 0:
            # self.known[nextNode] = list()
            # self.populate(nextNode, level + 1, children)
            
            
        
    # def getKthAncestor(self, node, k):
        # if node == 0: return -1
        # if k > len(self.known[node]): return -1
        # k = k-1
        
        # # Use array, so change this to k-1 once it's going dawg
        # return self.known[node][k]

"""

Based off user ye15's solution

Time: O(NlogN). Preprocessing is NlogN and then lookup is logN
Space: O(NlogN) - N * logN sized DP matrix 


"""




import math
class TreeAncestor:

    def __init__(self, n, parent):
        maxA = int(math.log2(n)) + 1   
        self.known = [ [-1]*maxA for _ in range(n) ] # Ancestor will be at most logN, aka height of tree
        
        for j in range(maxA):
            for i in range(n):
                if j == 0: # First pass we calculate every node's first parent
                    self.known[i][j] = parent[i]
                
                # Before computing parents of parents, check that a parent exists
                elif self.known[i][j-1] != -1:
                    
                    # My jth parent  is my (j-1)th parent's (j-1)th parent
                    self.known[i][j] = self.known[self.known[i][j-1]][j-1]     
        
    def getKthAncestor(self, node, k):
        
        """
        Every node has logN entries in known matrix

        k <= n, which means that each given k will have at most log(n) bits in its binary representation
        This works since each number can be expressed as 2^k in binary, where n = 2^k is the highest value
        Solving for k we get k = log2(n)


        When jumping in the table, reading from left to right, we want to jump by the most significant 1 digit's power repeatedly
        We get most sig digit with log(k)

        On each iteration we subtract k << i (where i is log(k)), so the new k basically gets rid of all zeroes (if any) between 1 digits
        We have the condition k > 0 because minimum jump is 1. If node becomes -1 then ancestor doesn't exist.
        Won't have out of bounds issues since we pre-computed up to logN ancestors for each node        
        
        """
        
        while k > 0 and node != -1: 
            i = int(math.log2(k))
            node = self.known[node][i]
            k -= (1 << i)

        return node 
