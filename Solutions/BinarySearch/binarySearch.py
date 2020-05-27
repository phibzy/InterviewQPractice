#!/usr/bin/python3

"""
Implementation of binary search

"""

def binarySearch(items, target):
    if not items: return False

    endI = len(items) 
    middle = len(items) // 2
    startI = 0

    if items[0] > target or items[-1] < target: return False

    while startI != middle:
        if items[middle] == target: return True

        if items[middle] > target:
            endI = middle
        else:
            startI = middle

        middle = (startI + endI + 1) // 2

        
    return items[middle] == target
