#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Jun 25, 2020 14:56:34 AEST
  @file        : markToys

"""

# Time Complexity: O(NlogN) - Must check every element of array, then insertion is logN
# Space Complexity: O(N) - Worst case all prices are in toys array

def maximumToys(prices, k):
    # Grab any toy with price < k, basically do insertion sort with grabbed toys
    # With resulting list, keep iterating until you can't buy any more
    # Use binary search at insertion to optimise

    toys = list()

    for p in prices:
        if p <= k:
            insert(p, toys)
    
    total = 0
    num = 0

    for t in toys:
        check = total + t
        if check > k:
            break
        total = check
        num += 1

    return num


def insert(v, li):

    place = 0
    l, r = 0, len(li) - 1
    while r >= l:
        middle = l + (r-l) // 2
        
        if v == li[middle]:
            place = middle
            break

        elif li[middle] < v:
            l = middle + 1
            place = l
        
        else:
            r = middle - 1

    li.insert(place, v)
