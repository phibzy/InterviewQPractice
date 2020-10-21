#!/usr/bin/python3

"""
   Test Cases:

       - The next day from today
       - A week from today
       - A month (then with different numbers)
       - A year (Back and forward)
       - Leap years
       - Max span with no leap years
       - Multitple leap years
       - 1/1/1971
       - 31/12/2100


"""

import unittest
from dayOfWeek import Solution

class testDOW(unittest.TestCase):

   a = Solution()

   def testToday(self):
       self.assertEqual(self.a.dayOfTheWeek(21,10,2020), "Wednesday", "Fails today case")

   def testTomorrow(self):
       self.assertEqual(self.a.dayOfTheWeek(22,10,2020), "Thursday", "Fails tomorrow case")

   def testWeek(self):
       self.assertEqual(self.a.dayOfTheWeek(28,10,2020), "Wednesday", "Fails week case")

   def testWeekMinusOne(self):
       self.assertEqual(self.a.dayOfTheWeek(27,10,2020), "Tuesday", "Fails week minus 1 case")

   def testMonthAhead(self):
       self.assertEqual(self.a.dayOfTheWeek(21,11,2020), "Saturday", "Fails month ahead case")

   def testMonthBehind(self):
       self.assertEqual(self.a.dayOfTheWeek(21,9,2020), "Monday", "Fails month ahead case")



