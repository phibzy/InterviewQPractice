#!/usr/bin/python3

"""
Test Cases:

1111
1111
1111
1111

1

0000
0000
0000
0000

0

X island cases

01
10

10001
01010
00100
01010
10001

00000
01110
01010
01110
00000

10
10






"""

from numberOfIslands import numIslands
import unittest

class testNumIslands(unittest.TestCase):

    def test1x1oneIsland(self):
        self.assertEqual(numIslands([["1"]]), 1, "Error - Fails 1x1 grid 1 island case")

    def test1x1zeroIsland(self):
        self.assertEqual(numIslands([["0"]]), 0, "Error - Fails 1x1 grid 0 island case")

    def test4x5oneIsland(self):
        self.assertEqual(numIslands([["1","1","1","1"],["1","1","1","1"],["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]), 1, "Error - Fails 1x1 grid 1 island case")

    def test4x5zeroIsland(self):
        self.assertEqual(numIslands([["0","0","0","0"],["0","0","0","0"],["0","0","0","0"],["0","0","0","0"],["0","0","0","0"]]), 0, "Error - Fails 4x5 grid 0 island case")

    def test5x5XIsland(self):
        self.assertEqual(numIslands([["1","0","0","0","1"],["0","1","0","1","0"],["0","0","1","0","0"],["0","1","0","1","0"],["1","0","0","0","1"]]), 9, "Error - Fails 5x5 grid X island case")


    def testFail(self):
        self.assertEqual(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]), 3, "Error - not passing leetcode test")
