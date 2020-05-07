#!/usr/bin/python3

"""
Given a string, find the longest palindromic substring

E.g. "niceabaemate" -> "eabae"


Know solution for finding palindrome: Check character, then if next character pop previous char onto stack
        

"""

def isPalindrome(string):
   length = len(string)
   i = 0

   if string == '': return True

   while i <= length //2:
       if string[i] != string[length - i - 1]:
           return False
       i+=1

   return True



def longestPalSubstring (string):
    length = len(string)
    startW  = 0
    endW = 0
    longestSub = ''
    longestLength = 0

    #O (N**2) Solution
    for i in range(length):
        for j in range(length+1):

            if isPalindrome(string[i:j]):

                if len(string[i:j]) > longestLength:
                    longestSub = string[i:j]
                    longestLength = len(longestSub)

    # Improvement: Sliding window, check if length of original string is odd/even

    return longestSub
    



    # while endW < length:

        # if isPalindrome(string[startW], string[endW]) :

            # if endW - startW + 1 > len(longestSub):
                # longestSub = string[startW:endW]

            









