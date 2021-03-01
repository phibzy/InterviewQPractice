#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Mar 01, 2021 11:01:52 AEDT
  @file        : valStack

"""

"""
Questions:
    - Pushed array: Does element order correspond to order they were pushed?
    - Can a value have been pushed more than once?
    - Same for pop list
    - Can either be empty?
    - Will they be always be equal lengths?
    - Any values in popped not in pushed?
    - Pushed always in order or nah?

"""

class Solution:

    # trying for O(1) space
    """
    Algo:
        No dicts, no stacks
        Use an offset variable on pushed list
        Use indices as in other solution

        Start at offset 0, increment pushedI until matches with element
        in poppedI.

        Then increment offset by 1 for each 'pop', if curr - offset doesn't
        equal next popped, add to stack as before by incrementing curr


    """
    # def validateStackSequences(self, pushed, popped):
        # pushI, popI = 0, 0
        # offset = 0

        # # We will get to end of pushed before end of popped, guaranteed
        # while pushI < len(pushed):

            # while pushI < len(popped) and popped[popI] != pushed[pushI]:
                # pushI += 1
                # if offset > 0: offset += 1

            # # If we didn't find it, it must be in the stack somewhere else
            # # therefore invalid
            # if pushI == len(popped): return False

            # while pushI - offset >= 0 and pushed[pushI - offset] == popped[popI]:
                # offset += 1
                # popI += 1

            # # Make sure offset doesn't go negative
            # if pushI - offset < 0: offset = 0
        
        # return True

    """
    Algo: TC = SC = O(N)

    Basically recreate the stack as you go
    Keep pushing pushed elements onto stack until the top element of stack
    equals the next index in popped list.

    Then pop element, increment popped index and repeat
    We can also use dict for "seen" elements in pushed, and if
    top element of stack doesn't equal nextPopped but we've seen it already,
    then we know it's an invalid permutation

    """
    def validateStackSequences(self, pushed, popped):
        # If lists are empty, then it's a valid combo
        # I.e. a stack that does nothing lol
        if not pushed: return True

        # Create stack and dict
        s = list()
        seen = dict()

        # Set starting indices
        pushI, popI = 0, 0

        while pushI < len(pushed) and popI < len(popped):
            # On next iteration, if next popped number has already been seen,
            # i.e. it's in the middle of the stack, then it's invalid
            if popped[popI] in seen: return False

            # Push onto empty stack if empty
            if not s: 
                seen[pushed[pushI]] = 1
                s.append(pushed[pushI])
                pushI += 1

            # While top of stack isn't equal to next element in popped
            while pushI < len(pushed) and s[-1] != popped[popI]:
                seen[pushed[pushI]] = 1
                s.append(pushed[pushI])
                pushI += 1

            while popI < len(pushed) and s and popped[popI] == s[-1]:
                s.pop()
                popI += 1

        # If we get to end of pushed, we need to check remnants of popped
        while s:
            if s.pop() != popped[popI]: return False
            popI += 1

        return True

