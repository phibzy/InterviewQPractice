#!/usr/bin/python3

"""
Given a string, find the longest palindromic substring

E.g. "niceabaemate" -> "eabae"


Know solution for finding palindrome: Check character, then if next character pop previous char onto stack
        

"""

# Use DP for checking if something is a palindrome
resultHash = dict()

# Note: '::-1' in lists means "nothing for start arg, nothing for end arg, jump by intervals of -1"
#       Other Example: [::3] prints every third element of the list
import logging
import pdb
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logging.disable(logging.DEBUG)

def isPalindrome(string):
   length = len(string)
   i = 0
   
   if string in resultHash or length <= 1: return True

   if string[0] == string[-1]:
       if isPalindrome(string[1:-1]):
           resultHash[string] = 1
           return True

   return False

def maxlen(l, i, j):
   length = len(l)
   maxLen = 0

   # if i == 119:
   # pdb.set_trace()


   while (i >= 0 and j < length and l[i] == l[j]):
       maxLen = j - i + 1
       i -= 1
       j += 1

   return maxLen


def longestPalSubstring (string):
    length = len(string)
    startW  = 0
    #endW = 1
    rStart = 0
    rEnd = 0

    longestLength = 0
    longestSub = ''

    if length == 1: return string
    # if length == 2:
        # if string[0] == string[1]:
            # return string
        # else:
            # return string[0]

    # Expanding outward solution - no early exit
    while startW < length:
        m1 = maxlen(string, startW, startW)
        m2 = maxlen(string, startW, startW + 1)
        newMax = max(m1,m2)

        # logging.debug(f"startW is {startW}, string[startW] is {string[startW]}")
        # logging.debug(f"m1 is {m1}, m2 is {m2}, newMax is {newMax}")
        


        # TODO: Many issues with this, calculations for rStart/rEnd need fixing
        if newMax > longestLength:
            longestLength = newMax
            if m2 > m1: newMax -= 1

            rStart = startW - newMax // 2 # This line
            rEnd   = startW + newMax // 2

            if m2 > m1: rEnd   += 1

        startW += 1

    longestSub = string[rStart:rEnd+1]


    #Brute Force
    #O (N**2) * O(N) = O(N**3) - palindromic check is O(N) solution that happens O(N**2) times
    # for i in range(length):
        # for j in range(length+1):

            # if isPalindrome(string[i:j]):

                # if len(string[i:j]) > longestLength:
                    # longestSub = string[i:j]
                    # longestLength = len(longestSub)

    # O(N^2) solution with DP palindrome check 
    # Worst case: all unique chars, O(N**2) 
    # Best case: longest substring is whole string, O(N)
    # Avg case: 
    # while startW < length:
        # if endW > length: break
        # while endW <= length:
            # newString = string[startW:endW]
            # if isPalindrome(newString):
                # wLength = len(newString)
                # if wLength > longestLength:
                    # longestLength = wLength
                    # longestSub = newString
            # endW += 1
        # startW += 1
        # endW = startW + longestLength - 1

    return longestSub
    
    # Best solution - Expand around centre, give it a crack and we'll leave it at that

# longestPalSubstring("iptmykvjanwiihepqhzupneckpzomgvzmyoybzfynybpfybngttozprjbupciuinpzryritfmyxyppxigitnemanreexcpwscvcwddnfjswgprabdggbgcillisyoskdodzlpbltefiz")
