#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Nov 20, 2020 15:48:20 AEDT
  @file        : decodeString

"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

# TC: O(N) - We check each character in the string once
# SC: O(1) - Even in worst case recursive calls are not a factor of N 
            # Side Note: means that, funnily enough, it beats Stack solution SC wise
            #            since stack worst case has > N/2 elements on stack, giving it O(N) SC

class Solution:
    def decodeString(self, s):     
        # Use recursive sub function to keep track of index
        # on recursive calls
        return self.rDecode(s,0)[0]
    
    def rDecode(self, s, i):
        retString = ""

        # There can only be lowercase letters, digits or square brackets
        # I'm not going to care about open brackets since they will always
        # come directly after a digit       
        while i < len(s):
            # if it's a lowercase character, we append to new string
            if "a" <= s[i] <= "z":
                # logging.debug("letter prompt triggered")
                retString += s[i]

            # if we've come across a '[' that can only mean it's
            # the end of a recursive call
            elif s[i] == "]":
                return (retString, i)

            # Otherwise it's a number and we're starting a repeated sequence
            else:
                # store how many times we repeat sequence
                # need to get full length of repeat number
                repeats = 0
                
                # as long as current char is a digit (probably better way to do this but w/e)
                while "0" <= s[i] <= "9":
                    repeats = repeats*10 + int(s[i])
                    i += 1
               
                # Recursive call on repeated sequence
                # i + 1 because we're currently sitting on the '['
                # character and don't care about it
                repeatString, i = self.rDecode(s, i+1)
                retString += repeats*repeatString              
                
            i += 1
        
        # returned i value will tell us where recursive call
        # finished (if any)
        return (retString, i)

