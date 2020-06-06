#!/usr/bin/python3

"""
Prints zig zag level order traversal of nodes in Btree


"""
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # use a queue/stack hybrid
        q = list()
        level = 0
        
        rList = list()
        rList.append(list())
        
        q.append((root, level))
        
        while q:
            oddCheck = level % 2 # this is the problem, always breaks first of each row
            if oddCheck:
                node, nLevel = q.pop(0)
            else:
                node, nLevel = q.pop()
            # Alternatively, pop from end or beginning based on level
            # Odd level: pop front, insert at end
            # Even level: pop end, insert front
                       
            if not node: continue
            if level != nLevel:
                rList.append(list())
                level += 1
            
            rList[nLevel].append(node.val)

            if oddCheck:
                q.append((node.right, level + 1))
                q.append((node.left, level + 1))
            else:
                q.insert(0, (node.left, level + 1))
                q.insert(0, (node.right, level + 1))
            
        return rList
                
                
