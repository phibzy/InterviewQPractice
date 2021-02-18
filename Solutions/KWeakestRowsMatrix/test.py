#!/usr/bin/python3

"""
    Test Cases:
        - All 0s or all 1s
        - Unique power for each row
        - Size 2*2
        - Unequal dimensions
        - Leftover valid rows at end
        - k == 1
        - k == m
        - k somehwere in between


"""

import unittest
from kWeakestRows import Solution

class test(unittest.TestCase):
    
    a = Solution()

    def testAll1s0s(self):
        self.assertEqual(self.a.kWeakestRows([[0,0,0],[0,0,0],[0,0,0]], 3), [0,1,2])
        self.assertEqual(self.a.kWeakestRows([[0,0,0],[0,0,0],[0,0,0]], 1), [0])
        self.assertEqual(self.a.kWeakestRows([[1,1,1],[1,1,1],[1,1,1]], 3), [0,1,2])
        self.assertEqual(self.a.kWeakestRows([[1,1,1],[1,1,1],[1,1,1]], 2), [0,1])

    def testUniqueRowPower(self):
        self.assertEqual(self.a.kWeakestRows([[1,0,0],[1,1,1],[1,1,0]], 3), [0,2,1])
        self.assertEqual(self.a.kWeakestRows([[1,0,0],[1,1,1],[1,1,0]], 1), [0])
        self.assertEqual(self.a.kWeakestRows([[1,0,0,0],[1,1,1,0],[1,1,0,0],[0,0,0,0]], 1), [3])

    def testEqualPowers(self):
        self.assertEqual(self.a.kWeakestRows([[1,0,0,0],[1,1,1,0],[1,1,0,0],[1,1,1,0],[0,0,0,0],[1,1,1,0]], 5), [4,0,2,1,3])

