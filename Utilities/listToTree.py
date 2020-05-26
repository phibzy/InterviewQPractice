#!/usr/bin/python3

"""
Utility for converting list to BTree

Used for helping with testing Leetcode input

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listToTree(l):
    # level order, so use queue
    if not l: return None

    head = TreeNode(l[0])

    s = list()
    s.append(head)

    i = 1
    while i < len(l):
        node = s.pop(0)
        if node is None: continue

        nextNode = TreeNode(l[i])
        node.left = nextNode
        s.append(nextNode)
        
        i += 1

        if i < len(l):
            nextNode = TreeNode(l[i])
            node.right = nextNode 
            s.append(nextNode)
            i += 1

    return head

def printTree(root):
    MAX_SIZE = 60
    if root is None: print("NULL".center(MAX_SIZE))

    currLevel = 1

    s = list()
    s.append((root, currLevel))

    while s:
        node, level = s.pop(0)
        if currLevel != level:
            print() # TODO: handle the slashes
            currLevel += 1
        
        if node is None:
            print("NULL".center(MAX_SIZE / level), end='')
        else:
            print(str(node.val).center(MAX_SIZE // level), end='')

        s.append((root.left, level+1))
        s.append((root.right, level+1))


printTree(listToTree([3,1,4,None,None,2]))



