#!/usr/bin/python3

"""
Shifts elements of an array d spaces

Can a be empty?
Max n?
Minimum d?
Can d be longer than the length of array?




"""
# Solution 1 - allowing modifications to list size
def rotLeft(a, d):
    if len(a) == 1 or len(a) == d: return a

    endA = a[:d]
    a = a[d:]
    a += endA

    return a

# Other solution - make temp array, find new index with i + d % n - 1.
# Put into new array at new index

# # Solution 2 - We change it in place, swaps only
# def rotLeft2(a, d):
    # if len(a) == 1 or len(a) == d: return a
    
    
