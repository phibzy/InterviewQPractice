#!/usr/bin/python3

"""
Prints zig zag level order traversal of nodes in Btree


"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
# logging.disable(logging.DEBUG)


# Maybe use two separate data structures, then one one's empty you know it's a new row or whatever
class Solution:
    def zigzagLevelOrder(self, root):
        # Use two stacks
        eQ = list()
        oQ  = list()
        stack = [oQ, eQ]
        
        rList = list()
        
        oQ.append((root, 0))
        curr = 0   
        nonCurr = 1

        while eQ or oQ:
            # Switch up if current stack is empty
            if not stack[curr]:
                curr, nonCurr = nonCurr, curr

            node, level = stack[curr].pop()
            logging.debug(f"node is {node} at level {level}")
            if not node: continue

            if level >= len(rList): rList.append(list())

            rList[level].append(node.val)

            # Even level - left first, into odd stack
            if nonCurr:
                stack[nonCurr].append((node.left, level+1))
                stack[nonCurr].append((node.right, level+1))

            # Opposite for odd level
            else:
                stack[nonCurr].append((node.right, level+1))
                stack[nonCurr].append((node.left, level+1))
            
        return rList
                
a = Solution()
print(a.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))


