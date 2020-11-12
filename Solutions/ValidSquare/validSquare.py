#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Nov 12, 2020 12:36:37 AEDT
  @file        : validSquare

"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
# logging.disable(logging.DEBUG)

import math


"""
TC: O(1) - Runtime will always be the same since we always get 4 points
SC: O(1) - " "


"""

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        # Locals is a dict containing all the passed in args
        # We want the points so we'll delete the 'self' arg from this dict
        p = locals()
        del p['self']
        points = list(p.values())
    
        # Sort points to make calculations easier
        # Sorts by x value and then y value if x is equal
        points.sort(key=lambda x: (x[0],x[1]))

        # If any points are equal we can't have a square
        # Must do this sanity check since 4 equal points will return
        # true when we check length of sides/diags
        if points[0] == points[1]: return False

        # A square is a shape with equal sides and equal diagonals
        # We must check for equal diagonals as well, since equal sides
        # could mean a rhombus
        equalSides = (self.dist(points[0], points[1]) == self.dist(points[1], points[3]) == \
                     self.dist(points[2], points[3]) == self.dist(points[2], points[0]))

        equalDiags = (self.dist(points[0], points[3]) == self.dist(points[1], points[2]))

        # Return true if both these checks pass
        return equalSides and equalDiags

    # Helper function for calculating distance between two points
    def dist(self, x, y):
        return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

