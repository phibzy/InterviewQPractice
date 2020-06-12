#!/usr/bin/python3

"""
Given an unordered array of length N with unique values 1 ... N,
return the minimum amount of swaps to make the array ordered.

Algo:
    - Change array values so that checking order is super easy
    - From i .. N - 1
    - If arr[i] is out of place, swap it with value in proper index and swaps++
    - Only increment i once arr[i] == i

Time Complexity: O(N), we go through array once changing values, then go through
                 once again swapping values
Space Complexity: O(1)


"""

def minimumSwaps(arr):
    # Change values so they match up with indices
    arr = [ i - 1 for i in arr ]
    count = 0
    i = 0

    while i < len(arr):
        if i != arr[i]:
            temp = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = temp
            count += 1

        else:
            i += 1

    return count
