#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Saturday Nov 28, 2020 10:22:00 AEDT
  @file        : partition

"""

class Solution:
    def canPartition(self, nums):
        # Minimum length is 1, obv can't split a list of length 1
        if len(nums) == 1: return False

        """
        Algo:

        If largest number is greater than the sum of the rest of list, it's impossible to split
        If the sum of the list's elements are odd, then it's also impossible to have two equal valued partitions



        """
       
        part1Sum, part2Sum = sum(nums), 0
        
        # if sum of all elements is odd, we can't make two equal value partitions
        if part1Sum % 2 == 1: return False
        
        # The sum we're aiming for
        targetSum = part1Sum // 2

        nums.sort()
        last = len(nums) - 1

        part1Sum -= nums[last]
        part2Sum += nums[last]

        # Del last element so that we can easily
        # keep track of next largest element
        del nums[last]
        last -= 1

        # If the largest element is greater than the sum of the rest,
        # we can't possibly make up that difference
        if part2Sum > part1Sum: return False

        # Find largest num less than difference of partition2 and targetSum
        while part2Sum < targetSum:


            diff = targetSum - part2Sum
            nextNum = nums[last]
            nextSum = part2Sum + nextNum
            remainder = targetSum - nextSum

            # print(f"part1Sum: {part1Sum}, part2Sum: {part2Sum}")
            # print(f"targetSum: {targetSum}, diff: {diff}")
            # print(f"nextNum: {nextNum}")
            # print(''.rjust(30, '#'))

            while last >= 0 and (remainder != 0) and ((nextNum > diff) or (remainder < nums[0])):
                last -= 1
                nextSum = part2Sum - nextNum
                nextNum = nums[last]
                nextSum = part2Sum + nextNum
                remainder = targetSum - nextSum

                # print(f"nums[0]: {nums[0]}")
                # print(f"nextNum: {nextNum}, nextSum: {nextSum}")
                # print(f"diff: {diff}, remainder: {remainder}")


            # print(''.rjust(30, '#'))
            # print(f"nextNum: {nextNum}")

            if last < 0: return False

            part2Sum += nextNum
            part1Sum -= nextNum
            del nums[last]
            last -= 1

        return part1Sum == part2Sum

a = Solution()
print(a.canPartition([23,13,11,7,6,5,5]))
