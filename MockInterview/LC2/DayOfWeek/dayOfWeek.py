#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Oct 21, 2020 11:31:15 AEDT
  @file        : dayOfWeek

"""

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Use 1/1/1971 as our baseline - a Friday
        # First leap year is 1972
        
        dow = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
        
        # We first calculate how many years
        years = year - 1971
        
        # First leap year is 1972, so subtract one and then divide by 4 (every 4 years)
        
        if years > 1:
            leapYearDayCount = 1
        
        leapYearDayCount += (year-1973) // 4
        
        totalDays = years*365 + leapYearDayCount
        
        monthDays = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        for i in range(1,month):
            # for 29th feb
            if i == 2 and self.isLeapYear(year): totalDays += 1
            totalDays += monthDays[i]
            
        totalDays += (day - 1)
        
        return dow[(totalDays % 7)]
        #return totalDays
        
    def isLeapYear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or \
           (year % 400 == 0):
                return True
                
        return False





