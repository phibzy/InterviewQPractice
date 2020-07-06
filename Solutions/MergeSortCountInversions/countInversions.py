#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Jul 06, 2020 17:34:36 AEST
  @file        : countInversions

"""

import math
import os
import random
import re
import sys

"""
NOTE TO SELF: TAKE DEBUG PRINTS OUT BEFORE SUBMISSION!
"""



# Complete the countInversions function below.
def countInversions(arr):
    # TL;DR just merge sort, except count how many places an item from the second comparison array moves

    start = 0
    end = len(arr) - 1

    count = mergeSort(arr, start, end)

    return count

def mergeSort(arr, l, r):
    if r <= l: return 0

    ogL = l
    middle = l + (r-l) // 2

    swaps = mergeSort(arr, l, middle) + mergeSort(arr, middle + 1, r)

    dummyArr = arr[l:r+1]
    # print(f"dummyArr is {dummyArr}")
    sortI, rI = 0, middle + 1
    while l <= middle and rI <= r:
        if arr[l] <= arr[rI]:
            dummyArr[sortI] = arr[l]
            l += 1

        else:
            dummyArr[sortI] = arr[rI]
            rI += 1
            swaps += middle + 1 - l

        sortI += 1

    if l > middle:
        dummyArr[sortI:] = arr[rI:r+1]

    else:
        dummyArr[sortI:] = arr[l:middle+1]

    # print(f"Swaps performed were {swaps}")
    # print(f"Updated subarray is {dummyArr}")

    arr[ogL:r+1] = dummyArr

    # print(f"Updated arr is {arr}")

    return swaps


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(result)


