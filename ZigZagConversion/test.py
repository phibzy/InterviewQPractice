#!/usr/bin/python3

from zigzag import convert
import unittest


"""
Test Cases:
    - One row
    - Two rows
    - Odd number decent size
    - Even number decent size
    - Many rows, enough that whole string fits in one column
    - "      ", except it stops before base row in next column
    - Num rows > length

"""


class testZigZag(unittest.TestCase):

    def test1Row(self):
        self.assertEqual("paypalishiring", "paypalishiring", "Error - Fails 1 row case")

    def test2Row(self):
        self.assertEqual(convert("paypalishiring", 2), "pyaihrnaplsiig", "Error - Fails 2 row case")

    def testOddNumberDecentSize(self):
        self.assertEqual(convert("paypalishiring", 5), "phasiyirpligan", "Error - Fails 5 row case")

    def testEvenNumberDecentSize(self):
        self.assertEqual(convert("chocolatestarfish", 8), "cihfsorhcaotlsaet", "Error - Fails 8 row case")

    def testAllInOneColumn(self):
        self.assertEqual(convert("chocolatestarfish", 100), "chocolatestarfish", "Error - Fails all in one column case")

    def testJustShortofBaseRow(self):
        self.assertEqual(convert("paypalishiring", 8), "pagynpiarliihs", "Error - Fails just short of base row case")


