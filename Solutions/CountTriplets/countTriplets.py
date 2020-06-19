#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Jun 19, 2020 15:44:01 AEST
  @file        : countTriplets

"""

def countTriplets(arr, r):

###### ORIGINAL APPROACH #################################
    # Approach: Go through array placing all values in hash
    # Hash values will be lists containing indices of hashed values
    # If in hash: append index to end of list, else: create list then append

    # Iterate through values again, check val*r exists in hash, then check if
    # val*r*r exists - if so for each value val*r*r check if indices are in order
    # in hash LL check if that value*r exists in hash

    # Can optimise: List will be sorted by index, so binary search can be performed
    # to find valid index. Can also check if 

    # Space Complexity: O(N) - at most N values in hash, combined length of 
    #                          all linked lists will be N

    # Time Complexity: O(N^2logN) - For each value in array, do binary search, then
    #                               for worst case basically N/2 elements do binary
    #                               search again. N * N/2 * logN = N^2logN


###### IMPROVED APPROACH #################################
    # The better approach I came up with based on user's hint:
    # TL;DR: THINK FORWARD

    # For each element v, set vals[v*r] += 1
    # This basically says "We've seen v/r already, so all we need is the last of the triplet
    # If vals[v*r] exists already, we set pairs[v*r] += vals[v]
    # Why? Because if there's many of same value already, then there will be that many
    # triplets once the set of 3 numbers is complete
    # Basically telling the future value "we've already seen two previous values, so if
    # you exist then we have a triplet

    # Then when we first check each element, we check if in vals, then if in pairs
    # if val is in pairs we increment result by pairs[v]

    # Time Complexity: O(N)  - we go through all elements once
    # Space Complexity: O(N) - Both hashes have at most 2N elements
    if len(arr) < 3: return 0
    result = 0

    vals = dict()
    pairs = dict()

    for v in arr:
        if v in vals:
            if v in pairs:
                result += pairs[v]

            pairs.setdefault(v*r, 0)
            pairs[v*r] += vals[v]

        vals.setdefault(v*r, 0)
        vals[v*r] += 1

    return result

