#!/usr/bin/python3

"""
Quick Sort implementation

"""

import pdb
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
# logging.disable(logging.DEBUG)

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

    while r >= l:

        while items[l] < pivot:
            l += 1

        while items[r] > pivot:
            r -= 1 

        logging.debug(f"l is {l}, r is {r}")
        logging.debug(f"items[l] is {items[l]}, r is {items[r]}, pivot is {pivot}")


        if r >= l:
            # Swap them
            temp = items[l]
            items[l] = items[r]
            items[r] = temp
            r -= 1
            l += 1

    rQuickSort(items, oldL, l - 1, items[oldL])
    rQuickSort(items, l, oldR, items[oldR])

print(quickSort([5,-3,10,-200,9,12,-9]))
