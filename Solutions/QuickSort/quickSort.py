#!/usr/bin/python3

"""
Quick Sort implementation

"""

import pdb

def quickSort(items):
    if len(items) <= 1: return items

    l = 0
    r = len(items) - 1

    pivot = items[l + (r-l) //2]

    rQuickSort(items, l, r, pivot)

    return items


def rQuickSort(items, l, r, pivot):
    if l >= r: return
    oldL = l
    oldR = r

    # pdb.set_trace()

    while r > l:

        if items[l] < pivot:
            l += 1

        if items[r] >= pivot:
            r -= 1 

        if r > l:
            # Swap them
            temp = items[l]
            items[l] = items[r]
            items[r] = temp
            r -= 1
            l += 1

    rQuickSort(items, oldL, l - 1, items[oldL])
    rQuickSort(items, l, oldR, items[oldR])

# quickSort([5,-3,10,200,9,12,-9])
