#!/usr/bin/python3

"""
Find Median of two sorted arrays of size N and M respectively

Overall runtime complexity should be O(log (m+n))

Both arrays cannot be empty


Initial thoughts:
    O(log(m+n)) screams binary search

    Probably involves calculating it based on two medians


"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
# logging.disable(logging.DEBUG)

def findMedianSortedArrays(nums1, nums2):
    # Get lengths, odd/even lengths v. important
    #General Algo:
        # Find median of each array
        # Divide into all values that are m1 <= v <= m2
        # Repeat until solution

    length1 = len(nums1)
    length2 = len(nums2)

    logging.debug(f"nums1 is {nums1}, nums2 is {nums2}")
    logging.debug(f"length1 is {length1}, length2 is {length2}")

    if length1 == length2 == 1:

        return ((nums1[0] + nums2[0]) / 2)

    # elif length1 == 1 and length2 == 2:

        # if nums1[0] > nums2[1]:
            # return nums2[1]
        # else:
            # return max(nums1[0], nums2[0])

    # elif length1 == 2 and length2 == 1:

        # if nums2[0] > nums1[1]:
            # return nums1[1]
        # else:
            # return max(nums1[0], nums2[0])

    elif 

    elif length1 == length2 == 2:
        if nums1[1] < nums2[0]:
            return findMedianSortedArrays([nums1[1]], [nums2[0]])

        

        return ((nums2[0] + nums2[1]) / 2) + ((nums2[0] + nums2[1]) / 2)

    else:


        m1 = length1 // 2
        m2 = length2 // 2

        logging.debug(f"m1 is {m1}, m2 is {m2}")

        # Slide the window Luke!
        
        logging.debug(f"nums1[m1] is {nums1[m1]}, nums2 is {nums2[m2]}")

        if nums1[m1] <= nums2[m2]:
            nums1 = nums1[m1:]
            nums2 = nums2[:m2+1]

        else:
            nums1 = nums1[:m1+1]
            nums2 = nums2[m2:]


        logging.debug(f"-----------------------------------------")

        return findMedianSortedArrays(nums1, nums2) 

