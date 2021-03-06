#!/usr/bin/python3

"""
Basic tests for quicksort
"""

import unittest
from quickSort import quickSort

class testSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(quickSort([]), [], "Fails empty case")

    def testLength1(self):
        self.assertEqual(quickSort([1336]), [1336], "Fails empty case")

    def testCaseEvenLength(self):
        self.assertEqual(quickSort([5,-3,10,9,12,-9]), [-9,-3,5,9,10,12], "Fails basic case, even length")

    def testCaseOddLength(self):
        self.assertEqual(quickSort([5,-3,10,200,9,12,-9]), [-9,-3,5,9,10,12,200], "Fails basic case, odd length")
    
    def testAllNeg(self): 
        self.assertEqual(quickSort([-20,-3,-9,-4,-420,-8,-3]), [-420,-20,-9,-8,-4,-3,-3], "Fails all negative numbers case")
