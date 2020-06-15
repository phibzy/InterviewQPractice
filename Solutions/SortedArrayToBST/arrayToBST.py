#!/usr/bin/python3

"""
Given a sorted array, convert it into a height balanced BST


Cases:
    - Empty array
    - Length 1 array
    - Even array
    - Odd array

Algo:
    Recursion. Take middle element, then make its left branch middle element of left elements,
    vice versa for right elements

Complexity:
    Space: O(logN) - AKA tree height, stack maxes out at all left branch calls
    Time:  O(N) - You have to grab each element in the array

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        # start middle, add, then add middle of each subsection for l/r branches
        length = len(nums)
        if length == 0: return None
        # Cases: 1 item, 2 items, even/odd
        
        return self.rBST(nums, 0, length - 1)
        
    def rBST(self, nums, l, r):
        if l > r: return None
        
        middle = (l + (r-l) // 2)
        
        return TreeNode(nums[middle], self.rBST(nums, l, middle - 1), self.rBST(nums, middle+1, r))
            
