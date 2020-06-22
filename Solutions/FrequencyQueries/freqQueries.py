#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Jun 22, 2020 09:23:28 AEST
  @file        : freqQueries

"""

import math
import os
import random
import re
import sys


"""
Complexity:

Time:
    - Overall: O(q) - where q is the number of queries
    - Insert, Remove, isPresent: O(1) - Do same constant time operations regardless of input

Space:
    - O(q) - Where q is the number of queries
           - Worst case all numbers inserted are unique, or all present numbers have unique freq

Improvement:
    Don't need to check if something is in freqHash when inserting and updating new/old frequencies
    Assuming it's tested working, it will 100% be in there

"""

class freq:
    def __init__(self):
        # Have a value hash and a frequency hash
        # Val hash just stores whether value is in structure or not
        # Freq hash stores how many of each frequency
        self.valHash = dict()
        self.freqHash = dict()

    def insert(self, x):
        if x in self.valHash:
            self.freqHash[self.valHash[x]] -= 1

            if self.freqHash[self.valHash[x]] == 0:
                del self.freqHash[self.valHash[x]]

        self.valHash.setdefault(x, 0)
        self.valHash[x] += 1

        self.freqHash.setdefault(self.valHash[x], 0)
        self.freqHash[self.valHash[x]] += 1

    def remove(self, y):
        if y in self.valHash:
            self.freqHash[self.valHash[y]] -= 1
            if self.freqHash[self.valHash[y]] == 0:
                del self.freqHash[self.valHash[y]]

            self.valHash[y] -= 1

            if self.valHash[y] == 0:
                del self.valHash[y]

            else:

                self.freqHash.setdefault(self.valHash[y], 0)
                self.freqHash[self.valHash[y]] += 1

    def isPresent(self, z):
        return int(z in self.freqHash)


# Complete the freqQuery function below.
def freqQuery(queries):
    s = freq()
    output = list()

    for op, val in queries:
        if op == 1:
            s.insert(val)
        
        elif op == 2:
            s.remove(val)

        elif op == 3:
            output.append(s.isPresent(val))

    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
