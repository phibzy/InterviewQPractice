#!/usr/bin/python3

"""
Adds two numbers, given as linked lists in reverse order
Returns number in same format

"""

def addTwoNumbers(num1, num2):

    len1 = len(num1)
    len2 = len(num2)

    # This will work because python deals in references
    # with mutable objects. Any changes to retList will be seen in num1 etc.
    retList = num1
    maxL = len2
    carry = 0

    # Start from back, add up - mod answer by 10 and carry on to next addition
    if len2 > len1:

        retList = num2
        maxL = len1

    elif len1 == 1 and len1 == len2:
        total = num1[0] + num2[0]
        if total >= 10:
            return [int(str(total)[2]), int(str(total)[0])]
        else:
            return [total]

    for i in range(maxL):
        total = num1[i] + num2[i] + carry

        if total >= 10:

            carry = 1
            total = total % 10

        # V important lol
        else:
            carry = 0

        retList[i] = total


    i = maxL

    while carry > 0:
        total = retList[i] + carry

        if total >= 10:

            carry = 1
            total = total % 10

        # V important lol
        else:
            carry = 0

        retList[i] = total

    return retList
