#!/usr/bin/python3

from addTwoNumbers import addTwoNumbers

import unittest

"""
Question to interviewer:
    I'm assuming they can have different number of digits?

Cases:

    One number with more digits than another
    Addition of digits which requires a carry over
    Single digits only
    One of the numbers is 0
    Both of the numbers are 0
"""


class a2NTests(unittest.TestCase):

    def testTwoZeroes(self):
        self.assertEqual(addTwoNumbers([0],[0]), [0], "Two zeroes not equal to 0")

    def testOneZero(self):
        self.assertEqual(addTwoNumbers([0],[1,2,3]), [1,2,3], "One zero case fail")

    def testSingleDigitsNoCarry(self):
        self.assertEqual(addTwoNumbers([4],[5]), [9], "Fails basic single digit case (no carry)")

    def testSingleDigitsWithCarry(self):
        self.assertEqual(addTwoNumbers([5],[9]), [4,1], "Fails basic single digit case (with carry)")

    def testMoreDigitsThanAnother(self):
        self.assertEqual(addTwoNumbers([8,5,7,7],[8,9]), [6,5,8,7], "Fails differing length case (with carries)")

    def leetCodeCase(self):
        self.assertEqual(addTwoNumbers([2,4,3],[5,6,4]), [7,0,8], "Fails leetcode example case")
