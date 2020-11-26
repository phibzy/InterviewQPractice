#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Nov 26, 2020 10:14:04 AEDT
  @file        : smallestInt

"""

# TC: O(K) - we make max K iterations before we work out if an N exists or not

class Solution:
    def smallestRepunitDivByK(self, K):

        # Obviously if K is even, then it won't divide into
        # an odd number - i.e. every possible N
        if K % 2 == 0: return -1
        
        # Likewise, any N can't be divisible by 5
        # since a number has to end in 5 or 0 to be divisible by 5
        if K % 5 == 0: return -1

        """
        we're trying to solve:

        N % K == 0

        the next N we try is N*10 + 1, so let's try our equation again

        (N*10 + 1) % K = 0

        Expanding brackets we get:
        (Note that 1 % K will always be 1 for any K > 1)

        (N*10) % K + 1 % K = 0
        
        Expand again:

        N % K * 10 % K + 1 % K = 0

        (N % K) is simply our remainder, so we can rewrite as:

        remainder * 10 % K + (1 % K) = 0

        which is same as:

        (remainder * 10) % K + (1 % K) = 0

        which can be rewritten as:

        (remainder * 10 + 1) % K = 0


        Here we're dealing with remainders only and don't have to stress
        about overflow. So we solve for this equation instead

        """

        # Start as off at 1 then apply calculation at each iteration
        calc = 1 % K

        # we only have K possible remainders, which will cycle through each iteration
        # If we haven't found a matching N after K tries, it doesn't exist
        for i in range(1, K+1):
            if calc == 0: return i
            calc = (calc * 10 + 1) % K

        return -1

        # So for our remaining possible K values, we have numbers
        # ending in 1, 3, 7 or 9. All of whom are able to multiply
        # and give numbers ending in a 1 digit

        # This brute force solution passed, however it shouldn't have
        # since the minimal N isn't guaranteed to fit in a 64-bit int
        # and we could end up with constant overflow, thus infinite loop

        # We brute force our way to finding the longest number
        # since we know it exists
        # n = 1
        # while True:
            # if n % K == 0:
                # return len(str(n))
            
            # n = n*10 + 1

    
