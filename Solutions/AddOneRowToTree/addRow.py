#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Mar 15, 2021 10:31:35 AEDT
  @file        : addRow

"""

"""
Qs:
    - What is defined as depth 1? Is there a depth 0?
    - Will tree always be non-empty?
    - Will row always be valid? e.g. will we ever get something impossible like row 3 in a 1 depth tree?
    - Will we add on the end or can the row be added anywhere? Do you want rest of tree preserved?
    - Range of values?
    - Max number of nodes? (may rule out recursive algo)

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Define eq as well for tests
    def __eq__(self, n):
        if not self and not n: return True

        if not self or not n: return False

        return self.val == n.val and \
                self.left == n.left and \
                self.right == n.right

"""
Algo:
    Recursive approach. Iterate to level depth-1, then add in new nodes - making
    sure set left/right pointers to existing children where appropriate.

    TC: O(N) - Worst case we visit last row for insertion and iterate over every node
    SC: O(N) - Worst case N/2 nodes will be on the stack at one time, in the case of a perfectly balanced tree
               at max depth

"""

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        # Will always have at least one node
        # Case for changing the root of whole tree
        if depth == 1:
            n = TreeNode(val, root)
            root = n
       
        # Otherwise handle recursive case
        else:
            self.rAddRow(root, val, 1, depth)

        return root

    # cDepth is current depth, tDepth is target depth 
    def rAddRow(self, root, val, cDepth, tDepth):
        # Handle null base case
        if not root: return

        # if row to be added is next row, add it in
        if cDepth == tDepth - 1:
            nextL = TreeNode(val, root.left)
            nextR = TreeNode(val, None, root.right)

            # Update root's children to new nodes
            root.left = nextL
            root.right = nextR

            # No more work needed here
            return
        
        # Otherwise, keep recursing
        self.rAddRow(root.left, val, cDepth + 1, tDepth)
        self.rAddRow(root.right, val, cDepth + 1, tDepth)

