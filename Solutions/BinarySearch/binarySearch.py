#!/usr/bin/python3

"""
Implementation of binary search

"""

def binarySearch(items, target):
    if not items: return -1

    endI = len(items) - 1
    middle = len(items) // 2
    startI = 0

    if items[0] > target or items[-1] < target: return -1

    while endI >= startI:
        if items[middle] == target: return middle

        if items[middle] > target:
            endI = middle - 1
        else:
            startI = middle + 1

        middle = (startI + endI + 1) // 2

        
    return -1 
