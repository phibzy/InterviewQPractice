#!/usr/bin/python3

"""
Implementation of Merge Sort

Advantages:    Time complexity is always NlogN

Disadvantages: Requires O(N) of space, which can be troublesome for huge N

"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
logging.disable(logging.DEBUG)

# Index method - less space used
def mergeSort(array):
    temp = array[0:len(array)]
    rMergeSort(array, temp, 0, len(array) - 1)
    return array

def rMergeSort(array, temp, start, end):
    logging.debug(f"start is {start}, end is {end}")

    if start >= end: return # case of len <= 1

    middle = start + (end - start) // 2
    logging.debug(f"middle is {middle}")

    rMergeSort(array, temp, start, middle)
    rMergeSort(array, temp, middle + 1, end)

    lI, rI, mI = start, (middle+1), start

    while lI <= middle and rI <= end:
        logging.debug(f"mI is {mI}")
        logging.debug(f"lI is {lI}, rI is {rI}")
        logging.debug(f"array[lI] = {array[lI]}, array[rI] = {array[rI]}")
        if array[rI] < array[lI]:
            logging.debug("rI value is smaller")
            temp[mI] = array[rI]
            rI += 1
        else:
            logging.debug("lI value is smaller")
            temp[mI] = array[lI]
            lI += 1
        mI += 1

    logging.debug(f"temp is: {temp} before adding end")

    if lI <= middle: temp[mI:end+1] = array[lI:middle+1] # append rest of leftside
    if rI <= end: temp[mI:end+1] = array[rI:end+1] # append rest of rightside

    logging.debug(f"temp is: {temp} after adding end")
    logging.debug(f"array before {array}")

    array[start:end+1] = temp[start:end+1]

    logging.debug(f"array after {array}")

# The slice method
def mergeSort1(items):
    length = len(items)
    if length <= 1: return items

    middle = length // 2
    
    # Because I make slices on every recursive call, we end up with NlogN space
    left  = mergeSort1(items[0:middle])
    right = mergeSort1(items[middle:length])

    lenLeft = len(left)
    lenRight = len(right)

    # Merge them back together
    lI, rI, mI = 0,0,0

    while lI < lenLeft and rI < lenRight:
        if left[lI] < right [rI]:
            items[mI] = left[lI]
            lI += 1
        else:
            items[mI] = right[rI]
            rI += 1
        
        mI += 1

    if lI < lenLeft:
        items[mI:length] = left[lI:lenLeft]

    if rI < lenRight:
        items[mI:length] = right[rI:lenRight]

    return items
        

# print(mergeSort([5,-3,10,200,9,12,-9]))
