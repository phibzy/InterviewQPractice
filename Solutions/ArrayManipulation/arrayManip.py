#!/usr/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self, r, val):
        self.r   = r
        self.val = val


def arrayManipulation(n, queries):   
    ranges = [Node([1,n], 0)] # We only care about which ranges are affected 
    #results = [ 0 for _ in range(n+1)]
    highest = 0 # k Will never be negative


# Be careful of 1-indexed array for this approach
    # Simple/obvious approach: Add to each element a-b inclusive k
    # Check highest value after each operation
    
    # Old version Time Complexity: O (m * n) - worst case the range of each query will be every element
    # This solution doesn't pass the time test
    for a,b,k in queries:
        if k == 0: continue # don't need to bother doing anything

        # First find lowest applicable range
        # Want ranges to have unique boundaries - i.e. no range shares any elements
        i = 0
        start = None
        end = None
        # Can optimise with binary search
        # Do 2 separate ones for start and end
        while(True):
            # printRanges(ranges)

            if (not start) and ranges[i].r[0] <= a <= ranges[i].r[1]:
                print(f"a is {a}, ranges[i].r[0] is {ranges[i].r[0]}")

                if a != ranges[i].r[0]:
                   # Check if equal to range end, if so make new range of single number
                    if a == ranges[i].r[1]:
                        ranges.insert(i+1, Node([a, a], ranges[i].val))

                    else:
                        ranges.insert(i+1, Node([a, ranges[i].r[1]], ranges[i].val))
                        ranges[i].r[1] = a - 1

                    i += 1 
                
                start = i   

            if ranges[i].r[1] >= b:
                # Edit this too
                if b != ranges[i].r[1]:
                    ranges.insert(i+1, Node([b+1, ranges[i].r[1]], ranges[i].val))
                    ranges[i].r[1] = b

                end = i     
                break

            i += 1
        printRanges(ranges)

        for i in range(start, end+1):
            # printRanges(ranges)
            ranges[i].val += k
            if ranges[i].val > highest:
                highest = ranges[i].val         

        printRanges(ranges)

    return highest


def printRanges(ranges):
    for i in ranges:
        print(f"--- [{i.r[0]}, {i.r[1]}], {i.val} ", end='')
    print()

f = open("test")
line = f.readline().strip()
n, q = map(int, line.split(' '))
queries = list()
for _ in range(q):
    a,b,k = map(int, f.readline().strip().split(' '))
    queries.append((a,b,k))

print(arrayManipulation(n, queries))
    
