#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Mar 09, 2021 10:16:22 AEDT
  @file        : averageLevels

"""

"""
Qs:
    - Will tree ever be empty?
    - Return output?
    - Max amount of levels?
    - Max amount of nodes?
    - Range of values? Ints or floats?
    - Average to be float?

    If huge depth/nodes -> maybe not recursive method

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, x):
        if not x and not self: return True

        if not self or not x: return False

        if self.val == x.val:
            return self.left == x.left and self.right == x.right

        return False

"""
Algo 1:
    Use 2 queues. The first one keeps track of nodes on the current
    level, the second one keeps track of nodes on the next level.

    Keep adding numbers on level until queue is empty. Add each node's 
    kids to second queue. Once first queue empty, divide by number of vals
    to get average and add to list.

    At end of loop swap the firstQ and secondQ pointers and repeat.

    TC: O(N) - have to visit every node
    SC: O(N) - Will have at most the width of the tree inside Qs,
               which is a factor of N

"""

from collections import deque

class Solution:
    def averageOfLevels1(self, root):
        # Make qs
        q1 = deque()
        q1.append(root)

        # List we will return
        output = list()

        while q1:
            q2 = deque()
            valSum = 0
            numNodes = len(q1)

            # Swap queues around
            q1, q2 = q2, q1

            while q2:
                node = q2.popleft()

                valSum += node.val
                if node.left: q1.append(node.left)
                if node.right: q1.append(node.right)

            output.append(valSum / numNodes)

        return output

    vals = list()
    num = list()

    def averageOfLevels(self, root):
        self.vals = list()
        self.num = list()
        self.rAverage(root, 0)
        return self.vals

    def rAverage(self, root, level):
        if not root: return

        if level >= len(self.vals):
            self.vals.append(root.val)
            self.num.append(1)

        else:
            self.vals[level] = self.vals[level] * self.num[level]
            self.num[level] += 1

            self.vals[level] = (self.vals[level] + root.val) / self.num[level]

        self.rAverage(root.left, level + 1)
        self.rAverage(root.right, level + 1)
        
        # print(self.vals)
        # print(self.num)












