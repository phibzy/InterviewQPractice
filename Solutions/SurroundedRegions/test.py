#!/usr/bin/python3

import unittest
from surroundedRegions import Solution

class testSRegions(unittest.TestCase):

    a = Solution()

    def testEmptyBoard(self):
        self.assertEqual(self.a.solve([]), [], "Fails empty board case")

    def test1x1Board(self):
        self.assertEqual(self.a.solve(['O']), ['O'], "Fails 1x1 board case")

    def test2x2Board(self):
        self.assertEqual(self.a.solve([['O','X'],['X','O']]), [['O','X'],['X','O']], "Fails 2x2 board case")

    def test3x3Board(self):
        self.assertEqual(self.a.solve([['X','X','X'],['X','O','X'],['X','X','X']]), [['X','X','X'],['X','X','X'],['X','X','X']], "Fails 3x3 board case")
