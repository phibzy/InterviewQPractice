#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Mar 04, 2021 12:13:53 AEDT
  @file        : setMismatch

"""

"""
Questions:
    - Will set always have at least 2 numbers?
    - Empty set?
    - Always in the range 1 <= n?
    - Do numbers need to be returned in a particular order?
    - Returned in an array?
    - Max N?
"""

"""
    Brute Force-y:
        - Go through and find number that occurs twice
        - Sum numbers in set - duplicate, find difference between that and sum
          of what set should be

        O(N) TC and SC

    Better way (If nums always in order) - but they're not sooo....:
        - Instead of using dict, can just check if number is out of index - saves O(N) space
        - For out of place index, find difference between index and actual value in it

    Simpler Way:
        - Create set of numbers 1 to N
        - Convert nums to set
        - Do Union minus intersection
        - Or can just do A-B and B-A to get vals

"""



class Solution:
    def findErrorNums1(self, nums):
        # Sum of 1 to n
        realSum = sum(range(1, len(nums) + 1))
        setSum = sum(nums)

        # dict keeping track of unique elements
        uniq = dict()

        for num in nums:
            if num in uniq:
                duplicate = num
                break

            uniq[num] = 1

        return [duplicate, (realSum - (setSum - duplicate))]

    # Set version
    def findErrorNums(self, nums):
        realSet = set(range(1, len(nums) + 1))
        numSet = set(nums)
        missingNo = list(realSet - numSet)[0]

        return sorted([missingNo, missingNo + sum(nums) - sum(realSet)])

        
