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


# Time Complexity: O(k + n) - We have to go through all queries, modifications are constant, then we iterate through
#                             n+1 sized list at the end
# Space Complexity: O(n) - We store an n-sized list

def arrayManipulation(n, queries):   
    # New approach: Increment start index by k, decrement b+1 by k
    # Only want to keep track of how levels change relative to each other
    # Think of it like a column graph or the height of beanstalks, or like staircase

    # First: make array of zeros
    # One extra spot at start but means easy indexing
    results = [ 0 for _ in range(n+1)]

    # For every k, increment a by k and decrement b+1 by k
    # Make sure b+1 isn't over the range though
    for a, b, k in queries:

        results[a] += k

        if b != n:
            results[b+1] -= k
        
    
    # At the end go through iteratively, max cumulative sum at any point is
    # What we return
    val = 0
    highest = 0
    for i in results:
        val += i
        if val > highest: highest = val
    
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
    
