#!/usr/bin/python3

"""
Implementation of Merge Sort

Advantages:    Time complexity is always NlogN

Disadvantages: Requires O(N) of space, which can be troublesome for huge N

"""

def mergeSort(items):
    length = len(items)
    if length <= 1: return items

    middle = length // 2
    
    left  = mergeSort(items[0:middle])
    right = mergeSort(items[middle:length])

    lenLeft = len(left)
    lenRight = len(right)

    # Merge them back together
    lI, rI, mI = 0,0,0

    while lI < lenLeft and rI < lenRight:
        if left[lI] < right [rI]:
            items[mI] = left[lI]
            lI += 1
        else:
            items[mI] = right[rI]
            rI += 1
        
        mI += 1

    if lI < lenLeft:
        items[mI:length] = left[lI:lenLeft]

    if rI < lenRight:
        items[mI:length] = right[rI:lenRight]

    return items
        
