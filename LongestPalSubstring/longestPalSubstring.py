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

def isPalindrome(string):
   length = len(string)
   i = 0
   
   if string in resultHash or length <= 1: return True

   if string[0] == string[-1]:
       if isPalindrome(string[1:-1]):
           resultHash[string] = 1
           return True

   return False

def longestPalSubstring (string):
    length = len(string)
    startW  = 0
    endW = 1
    longestSub = ''
    longestLength = 0

    #O (N**2) * O(N) = O(N**3) - palindromic check is O(N) solution
    # for i in range(length):
        # for j in range(length+1):

            # if isPalindrome(string[i:j]):

                # if len(string[i:j]) > longestLength:
                    # longestSub = string[i:j]
                    # longestLength = len(longestSub)

    
    # Worst case: all unique chars, O(N**2) 
    # Best case: longest substring is whole string, O(N)
    # Avg case: 

    while startW < length:
        if endW > length: break
        while endW <= length:
            newString = string[startW:endW]
            if isPalindrome(newString):
                wLength = len(newString)
                if wLength > longestLength:
                    longestLength = wLength
                    longestSub = newString
            endW += 1
        startW += 1
        endW = startW + longestLength - 1

    return longestSub
    
    # Best solution - Expand around centre, give it a crack and we'll leave it at that

