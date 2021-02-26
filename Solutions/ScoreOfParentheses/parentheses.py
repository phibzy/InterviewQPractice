#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Feb 26, 2021 11:48:33 AEDT
  @file        : parentheses

"""

"""

Can string be empty?
Will parentheses always be balanced?
Only parentheses?
Max string size?

TC: O(N) - we look at each character in string
SC: O(N) - We have at most N/2 recursive calls

"""
class Solution:
    def scoreOfParentheses(self, s):
        # Use two stacks, one for adding and one for subtracting
        mult = list()
        add = list()

        total = 0
        i = 0
    
        # Very similar comparisons to before
        while i < len(s):

            # If there's a closing bracket, we've been in a nested
            # parentheses expression
            if s[i] == ")":
                total *= 2
                total += mult.pop()

            # Check for starting nested case
            else:
                if s[i+1] == ")":
                    total += 1
                    i += 1

                # Otherwise we're starting a nested case
                else:
                    mult.append(total)
                    total = 0

            i += 1

        return total

    # OG Recursive solution
    def scoreOfParentheses2(self, s):
        return self.calcScore(s, 0)[0]

    # Recursive function, returns tuple of inner total
    # and index of next element after it finishes
    def calcScore(self, s, i):
        # keeps track of total sum
        total = 0

        while i < len(s):
            # Check for ending bracket first
            # since this will eliminate index errors
            if s[i] == ")":
                return (total, i + 1)

            # Otherwise it's an open bracket
            # meaning we have at least one other char afterwards
            else:
                # If it immediately closes,
                # add 1 to total and skip next index
                if s[i+1] == ")":
                    total += 1
                    i += 2

                # Otherwise we're beginning another nested parentheses
                # expression, so make a recursive call
                else:
                    nextTotal, i = self.calcScore(s, i+1)
                    total += nextTotal*2

        return (total, i)
