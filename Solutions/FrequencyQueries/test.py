#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Jun 22, 2020 09:23:43 AEST
  @file        : test


Test Cases:
    - Insert 1 value
    - Insert 1 value multiple times, making sure frequency changes
    - Remove on empty structure
    - Removing value of x frequency, when another value of x freq exists

"""

import unittest
from freqQueries import freq, freqQuery

class TestFreq(unittest.TestCase):

    def testInsert1Val(self):
        a = freq()
        a.insert(1)
        self.assertEqual(a.valHash[1], 1)
        self.assertEqual(a.isPresent(1), 1)

    def testInsertManyOfSame(self):
        a = freq()
        a.insert(1)
        self.assertEqual(a.valHash[1], 1)
        self.assertEqual(a.isPresent(1), 1)

        a.insert(1)
        self.assertEqual(a.valHash[1], 2)
        self.assertEqual(a.isPresent(1), 0)
        self.assertEqual(a.isPresent(2), 1)

        a.insert(1)
        self.assertEqual(a.valHash[1], 3)
        self.assertEqual(a.isPresent(1), 0)
        self.assertEqual(a.isPresent(2), 0)
        self.assertEqual(a.isPresent(3), 1)

        a.insert(1)
        self.assertEqual(a.valHash[1], 4)
        self.assertEqual(a.isPresent(1), 0)
        self.assertEqual(a.isPresent(2), 0)
        self.assertEqual(a.isPresent(3), 0)
        self.assertEqual(a.isPresent(4), 1)

        a.insert(1)
        self.assertEqual(a.valHash[1], 5)
        self.assertEqual(a.isPresent(1), 0)
        self.assertEqual(a.isPresent(2), 0)
        self.assertEqual(a.isPresent(3), 0)
        self.assertEqual(a.isPresent(4), 0)
        self.assertEqual(a.isPresent(5), 1)

    def testRemoveBasic(self):
        a = freq()
        a.remove(5)
        self.assertEqual((5 in a.valHash), False)

        a.insert(5)
        self.assertEqual(a.valHash[5], 1)
        self.assertEqual(a.isPresent(1), 1)

        a.remove(5)
        self.assertEqual((5 in a.valHash), False)
        self.assertEqual(a.isPresent(1), 0)

    def testRemoveEqualFreq(self):
        a = freq()
        a.insert(1)
        a.insert(1)
        a.insert(1)

        a.insert(2)
        self.assertEqual(a.isPresent(1), 1)
        self.assertEqual(a.isPresent(3), 1)

        a.insert(2)
        self.assertEqual(a.isPresent(1), 0)
        self.assertEqual(a.isPresent(2), 1)
        self.assertEqual(a.isPresent(3), 1)

        a.insert(2)
        self.assertEqual(a.isPresent(1), 0)
        self.assertEqual(a.isPresent(2), 0)
        self.assertEqual(a.isPresent(3), 1)

        a.remove(1)  
        self.assertEqual(a.isPresent(1), 0)
        self.assertEqual(a.isPresent(2), 1)
        self.assertEqual(a.isPresent(3), 1)
        self.assertEqual((1 in a.valHash), True)

        a.remove(1)  
        self.assertEqual(a.isPresent(1), 1)
        self.assertEqual(a.isPresent(2), 0)
        self.assertEqual(a.isPresent(3), 1)
        self.assertEqual((1 in a.valHash), True)

        a.remove(1)  
        self.assertEqual(a.isPresent(1), 0)
        self.assertEqual(a.isPresent(2), 0)
        self.assertEqual(a.isPresent(3), 1)
        self.assertEqual((1 in a.valHash), False)

