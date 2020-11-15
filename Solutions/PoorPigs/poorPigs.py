#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Nov 15, 2020 11:14:00 AEDT
  @file        : poorPigs

"""

class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        # First - work out how many tries we have
        maxTries = minutesToTest // minutesToDie

        # Base case: if maxTries >= number of buckets,
        # we only need to use one pig since that pig
        # has enough time to try all the buckets by themselves

        # Also applies if we only have one more bucket than maxTries,
        # since we can try n-1 buckets then deduce the last one is poisoned
        if maxTries >= (buckets - 1): return 1

        #NOTE: Need to keep track of remaining pigs

        # For each call of "binary search" that finds region
        # with poisoned bucket, we need a new pig to replace the dead one
        
        # We do the try/buckets check at every division
        # because the aim is to use as little pigs as possible
        currTries = maxTries


        # For starting division, if groups of 2 need to try both
        # For divisions after that, we only need to try one of the pair
        # IGNORE DIS
        



