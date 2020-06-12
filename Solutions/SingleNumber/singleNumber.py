#!/usr/bin/python3

"""
In given array of integers, every number appears once except for 1 number

Find that number

"""


class Solution:
    def singleNumber(self, nums):
        
        # Basic solution - Use hash or set
        # Put number into hash or set
        # If already in set, take it out of set
        # Last remaining number in set is odd one out
        # Time Complexity: O(N)
        # Space Complexity: O(N/2) -> O(N). You will have at most half+1 of all list elements in set at once
        
        
        #s = set()
        
        #for i in nums:
        #    if i in s:
        #        s.remove(i)
        #    
        #    else:
        #        s.add(i)
        
        #return list(s)[0]
        
        # One way of doing it without extra memory - sort in place, then go through linearly and check pairs of numbers
        # Time complexity would be: NlogN (assuming Merge Sort)
        
        # Another way would be using XOR:
        
        # XOR works like multiplication in that regardless of the order of consecutive XORS, it will get the same result
        # Also we know that a ^ a = 0
        # Since there's only 1 odd number out, every other number has a pair, meaning that said pair will XOR to 0
        # So given array 2, 3, 5, 2, 5; we would have:
        # 2 ^ 3 ^ 5 ^ 2 ^ 5, which can be rewritten as:
        # 2 ^ 2 ^ 5 ^ 5 ^ 3, which simplifies to:
        # 0 ^ 0 ^ 3, which equals 3 the missing number
        
        # Time Complexity: O(N) since we go through array once only
        # Space Complexity: O(1) - no matter how big array is we're only using 1 variable to XOR everything
        
        a = 0
        
        for i in nums:
            a ^= i
            
        return a
