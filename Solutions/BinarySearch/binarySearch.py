#!/usr/bin/python3

"""
Implementation of binary search

"""

### IMPORTANT NOTE ###
# middle = l + r / 2 is a bug that was present
# in many binary search implementations, including Java's.
# Reason it's a bug is because when l/r are huge, it causes
# an overflow and results in negative middle index.
# To fix this, use middle = l + ((r - l) /2). 


def binarySearch(items, target):
    if not items: return -1

    # endI = len(items) - 1
    # middle = len(items) // 2
    # startI = 0

    # if items[0] > target or items[-1] < target: return -1

    # while endI >= startI:
        # if items[middle] == target: return middle

        # if items[middle] > target:
            # endI = middle - 1
        # else:
            # startI = middle + 1

        # middle = (startI + endI + 1) // 2

        
    # return -1 


    # Recursive solution:
    index = rBinarySearch(items, target, 0, len(items) - 1)

    return index

def rBinarySearch(items, target, l, r):
    
    if r >= l:
        mI     = l + ((r-l) // 2)
        middle = items[mI] 
        
        if target == middle: return mI

        if target > middle:
            return rBinarySearch(items, target, mI + 1, r)
        
        if target < middle:
            return rBinarySearch(items, target, l, mI - 1)

    return -1 


