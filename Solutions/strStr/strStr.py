#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Sep 04, 2020 13:33:53 AEST
  @file        : strStr

"""
class Solution:
    def strStr(self, haystack, needle):
        if not needle: return 0
        
        endIndex = len(needle)
        if endIndex > len(haystack): return -1
        
        startIndex = 0
        while endIndex <= len(haystack):
            if needle == haystack[startIndex:endIndex]:
                return startIndex
            startIndex += 1
            endIndex +=1
            
        return -1
        

