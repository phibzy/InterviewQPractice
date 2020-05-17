#!/usr/bin/python3


"""
Takes int list of start times and endtimes, plus integer

Returns number of students studying at given integer time, boundary inclusive

"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        
        return count
