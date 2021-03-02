#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Mar 02, 2021 12:14:37 AEDT
  @file        : stack

"""

"""
Qs:
    - Always pop most freq element? Do we pop the latest most freq element or oldest?
    - Will there ever be a pop on empty stack? How to handle?
    - Will operations always be valid? Or do we need to check for invalid?
    - Range of numbers we're dealing with?
    - Number of operations we need to handle?
    - What if frequencies equal?

"""

"""
Brute force-y Solution:
    Push: O(1)
    Use an actual stack to represent the stack, push operation
    works the same.

    Pop: O(N) search with O(N) removal 
    Whenever we pop, go through the stack finding the most freq element.
    Use a dict to keep track of frequencies for each element.
    If >= current maxFrequency, grab index of that element. (handles tiebreakers)

    Return element at that index and then remove it from stack

    O(N) space is used here worst case

"""

"""
Better Solution:
    Have a dict with keys frequency -> a stack of vals
    Have another dict mapping a value with its frequency

    Whenever you add a value, check it's frequency level, then add it to the stack
    for that level + 1

    What this will mean is - say we have a number that occurs 5 times. It will have entries in
    the 1, 2, 3, 4, 5 frequency stacks.

    This is fine though, since it will maintain order amongst frequency levels and allow us to pop
    in constant time.

    Push will also be constant time.

    Then we just have a variable keeping track of max frequency

    We will end up using O(N) space in the worst case, that's the only tradeoff

"""


class FreqStack:

    def __init__(self):
        # Dict mapping to stacks keeping track of frequency levels
        self.freqLevel = dict()

        # Keeping track of frequency of particular values
        self.freq = dict()

        # Tells us what maximum frequency level is
        self.maxFreq = 0
        

    def push(self, x):
        # Add to freq dict first if needed, then increment freq value
        self.freq.setdefault(x, 0)
        self.freq[x] += 1

        # Add to stack for freqLevel
        # If nothing at this level, create stack first
        self.freqLevel.setdefault(self.freq[x], list())
        self.freqLevel[self.freq[x]].append(x)

        # Update maxFreq if necessary
        self.maxFreq = max(self.maxFreq, self.freq[x])

    def pop(self):
        # Guaranteed to never pop an empty stack, so maxFreq
        # will always be >= 1

        # First step, go to maxFreq stack level and pop the value
        val = self.freqLevel[self.maxFreq].pop()
        
        # Update freq for that val
        self.freq[val] -= 1
        if self.freq[val] == 0: del self.freq[val]

        # Then keep updating maxFreq until we find the next
        # maxFreq if necessary
        # Can do this easily by going down frequencies and 
        # checking for empty stacks
        while self.maxFreq > 0 and not self.freqLevel[self.maxFreq]:

            # We'll also delete empty stacks to free some space
            del self.freqLevel[self.maxFreq]
            self.maxFreq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
