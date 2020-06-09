#!/usr/bin/python3

"""
Given a queue of integers, find minimum amount of bribes
that could have resulted in current order

If state is invalid, print "Too chaotic"

Each person in queue can bribe person in front to swap positions
Each person can bribe at most two people


Will each value be unique?
Scope of values?
Minimum size of input? - E.g. will empty list be an option

"""

def minimumBribes(q):
    count = 0
    for i, val in enumerate(q):
        if (i - val + 1) > 2:
            print("Too chaotic")
        
        count += (i - val + 1)

    print(count)
