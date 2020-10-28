#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Oct 28, 2020 19:24:13 AEDT
  @file        : addBinary

"""

import logging

logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

class Solution:
    def addBinary(self, a, b):
        # cheat solution
        # return bin(int(a,2) + int(b,2))[2:]
        
        
        # Go digit by digit, keep track of overflow for next digit(s)
        # Time Complexity: O(N^2) - since concatenation operation is O(N)
        
        # Handle different length case too
        # Assume a is longer string, swap them if not
        if len(b) > len(a):
            a, b = b, a
        
        i = 1
        remainder = 0
        output = ""
        
        # Move right to left, adding each digit together
        # use string b for while condition since it's smaller
        while i <= len(b):
            result = int(a[-i]) + int(b[-i]) + remainder
            
            # check for overflow
            if result > 1:
                output = str(result % 2) + output
                remainder = 1
            
            else:
                # Handles the 2 "0" and 1 "1" cases
                output = str(result) + output
                remainder = 0
                    
            i += 1
            
        # if any more remainder, go through rest of string a
        while i <= len(a) and remainder > 0:
            logging.debug(f"Second loop, i is {i} and a[-i] is {a[-i]}")
            logging.debug(f"Remainder is {remainder}")
            if a[-i] == "0":
                logging.debug("if")
                output = "1" + output
                remainder = 0
            
            else:
                logging.debug("else")
                output = "0" + output

            i += 1
        
        if remainder > 0: 
            output = "1" + output
            
        else:
            output = a[:(-i + 1)] + output
            
        return output

a = Solution()
a.addBinary("10", "101111")
            
        
            
