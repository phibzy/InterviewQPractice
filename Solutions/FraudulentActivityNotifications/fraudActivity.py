#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Jun 25, 2020 16:27:27 AEST
  @file        : fraudActivity

"""

import math
import os
import random
import re
import sys
import pdb


"""
Algo:
    Have a list keeping track of order of days, new values appended onto end to maintain day order`
    Have another list that maintains sorted order of list, new values inserted with binary search

    Once required length of previous days reached, do fraudActivity formula on median of sorted list
    Count + 1 if >= formula
    Remove first element in dayOrder list, then remove value from sorted list using same binary search method as before

    Insert new days value into both lists, then repeat

    Time Complexity: O(NlogN) - Have to visit all values in expenditure then 2*logN operations for insert/deletion
    Space Complexity: O(d) - Two lists of size d are used

"""


def activityNotifications(expenditure, d):
    length = len(expenditure)
    if d == expenditure: return 0
    
    notifications = 0
    dayOrder = list()
    trailDays = list()
    odd = (d % 2 == 1)
    middle = d // 2

    i = 0

    while i < d:
        # print("Looping in first loop")
        dayOrder.append(expenditure[i])
        insert(expenditure[i], trailDays, i)
        i += 1

    while i < length:
        # print("Looping in second loop")
        if expenditure[i] >= 2*median(trailDays, odd, middle):
            notifications += 1
        
        remove(dayOrder, trailDays, d)
        dayOrder.append(expenditure[i])
        insert(expenditure[i], trailDays, d - 1)
        i += 1

    return notifications

def remove(li, order, length):
    target = li[0]
    del li[0]

    l, r = 0, length - 1 

    while r >= l:
        # print("Looping in remove")
        middle = l + (r-l) // 2

        if order[middle] == target:
            index = middle
            break

        elif order[middle] < target:
            l = middle + 1
        
        else:
            r = middle - 1

    del order[index]

def median(li, odd, middle):
    if odd:
        return li[middle]
    
    return (li[middle] + li[middle - 1]) / 2 


# Insert into list sorted, using binary search
# to find sorted index
def insert(v, li, length):
    place = 0
    l,r = 0, length - 1

    # print(f"list is {li}")
    # pdb.set_trace()
    while r >= l:
        # print("Looping in insert")
        # print(f"list is {li}")
        # print(f"val is {v}")
        middle = l + (r-l) // 2
        # print(f"middle is {middle}")
        if v == li[middle]:
            place = middle
            break

        elif v < li[middle]:
            r = middle - 1

        else:
            l = middle + 1
            place = l
    
    li.insert(place, v)

if __name__ == '__main__':
    fptr = open("test_out.txt", 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
