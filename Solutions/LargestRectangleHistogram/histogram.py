#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Jan 01, 2021 14:38:18 AEDT
  @file        : histogram

"""

class Solution:
    def largestRectangleArea(self, heights):
        # Handle empty list
        if not heights: return 0

        # Use a stack to keep track of level,
        # and the index where that level started.
        # Start by placing first element in stack at index 0.
        heightStack = list()
        heightStack.append((heights[0], 0))

        # Start our area count using first rectangle
        lastHeight = largestArea = heights[0]

        # Check every height except first one
        for i in range(1, len(heights)):
            h = heights[i]

            # If higher than last rectangle, we add a new level to stack
            if h > lastHeight:
                heightStack.append((h, i))

            # If less than, we need to unwind stack and do calculations
            elif h < lastHeight:
                # Keep whittling down the stack until we're equal
                # levels or lower
                while heightStack and heightStack[-1][0] > h:
                    nextH, nextI = heightStack.pop()

                    # Update max if we have a new largest rectangle
                    # We calculate areas based on current index and
                    # index at which level started
                    # The difference between these indexes is the horizontal length
                    # This also handles the 0 height case
                    largestArea = max(largestArea, (nextH * (i - nextI)))
                
                # Add new entry to stack, using last unwound index
                # as starting index
                heightStack.append((h, nextI))

            # Don't need to do anyting if equal height
            # Just update lastHeight for next comparison
            lastHeight = h

        # Set lastIndex to length so calculations work properly
        lastIndex = len(heights)

        # Unwind whatever of stack remains
        while heightStack:
            nextH, nextI = heightStack.pop()
            largestArea = max(largestArea, (nextH * (lastIndex - nextI)))

        # Return largest area
        return largestArea

