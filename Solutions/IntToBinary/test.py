#!/usr/bin/python3

"""
Cases:
    0
    1
    Max 32-bit number
    Negative number - leave this out for now
    Odd number
    Some random number of choosing

"""

import unittest
import intToBinary

class testItoB(unittest.TestCase):

    def test0(self):
        self.assertEqual(intToBinary.intToBinary(0), '0', "Fails zero case")

    def test1(self):
        self.assertEqual(intToBinary.intToBinary(1), '1', "Fails 1 case")

    def testMax32(self):
        self.assertEqual(intToBinary.intToBinary(2**32 - 1), '11111111111111111111111111111111', "Fails max 32 case")

    def testOdd(self):
        self.assertEqual(intToBinary.intToBinary(547), '1000100011', "Fails odd case")

    def testRandom(self):
        self.assertEqual(intToBinary.intToBinary(555666), '10000111101010010010', "Fails odd case")

