#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Feb 23, 2021 11:48:12 AEDT
  @file        : minRemove

"""

# Only parentheses? Letters/numbers as well?
# Length of string? Empty string? Max length?
# Guaranteed to be at least one parenthese?
# Any rules regarding starting with open/closing parentheses?

# Are we returning the minimum number we need to remove?
# Or are we returning the actual valid string?


"""
    Algo:
        
        Go through string. Whenever you encounter an open bracket, add its index to stack.
        If you encounter a closed bracket and we have a non-empty stack, pop top element off.
        Basically we're checking that each open bracket has a matching closing bracket.

        If we encounter a closed bracket and there's no stack, then add its index to closeBrackets list.

        If we don't have anything on the stack or in closedBrackets list, the string is valid.
        Otherwise, remove all indices in the two lists from original string, returning result.

        TC: O(N) - We go through string twice, once to find wrong parentheses, the other time to 
        concatenate resulting string

        SC: O(N) - Worst case every character in original string is invalid, and we have to store all of them
        in lists




"""

class Solution:
    def minRemoveToMakeValid(self, s):
        # If empty string, just return it straight back
        if not s: return s

        # Create a stack for keeping track of parentheses
        stack = list()
        closedBrackets = list()

        # Otherwise, go through whole list 
        for i in range(len(s)):
            nextChar = s[i]

            # If open bracket, put index on stack
            if nextChar == "(":
                stack.append(i)

            if nextChar == ")":
                # If matching open bracket, pop it off stack
                if stack: 
                    stack.pop()

                # Otherwise, add to closedBrackets list
                else:
                    closedBrackets.append(i)

        # # If no stack or closedBrackets, string doesn't need to be changed
        # if not stack and not closedBrackets: return s
        # print(stack, closedBrackets)

        # Order the lists into one deque
        toRemove = self.combineLists(stack, closedBrackets)
        # print(toRemove)

        # Remove all given indices
        output = ""
        lastIndex = 0
        for i in toRemove:
            output += s[lastIndex:i]
            lastIndex = i + 1

        # Add remainder of list to output
        output += s[lastIndex:]

        return output

    # Helper function to combine lists
    def combineLists(self, stack, closedBrackets):
        i, j = 0, 0

        # Put indices in order
        toRemove = list()
        while i < len(stack) and j < len(closedBrackets):
            if stack[i] < closedBrackets[j]:
                toRemove.append(stack[i])
                i += 1
            
            else:
                toRemove.append(closedBrackets[j])
                j += 1

        # If we run out of one list, add the rest of
        # the other on the end
        if i < len(stack):
            toRemove += stack[i:]

        if j < len(closedBrackets):
            toRemove += closedBrackets[j:]

        return toRemove

