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


# Time Complexity: O (N)
def minimumBribes(q):
    q = [ i-1 for i in q]
    count = 0

    for i, val in enumerate(q):
        # No one can move more than 2 places forward, since can only bribe twice
        if (val - i) > 2:
            print("Too chaotic")
            return
       
        # If a value bribes past an index, it can at most only get to newIndex -1
        # Since it bribes to get their index, then can only do one more bribe after
        for j in range(max(0, val-1), i):
            if q[j] > val: count += 1


    print(count)

# Which numbers are missing from in front of a given index?
# 1 2 5 3 7 8 6 4


# 0 1 4 2 6 7 5 3


