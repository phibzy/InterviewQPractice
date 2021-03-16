#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Mar 16, 2021 10:26:57 AEDT
  @file        : intToRoman

"""

"""
Qs:
    - What is the range of the input? Will we have to deal with zero?
    - Anything beyond the thousands?
    
    Range of input: 1 <= num <= 3999

    Check for 4s and 9s

"""

"""
Algo: O(D) space - where D is number of digits
    
    Have a multiplier for calculating digit values, starting at 1

    Start at LSD, multiply by multiplier, and convert to roman numeral, then add to queue
    Multiply multiplier by 10, then keep going along, repeating and adding to queue

    Should end up with a queue with roman numerals, with most significant value first
    Concatenate elements of queue and return

Other Algo: O(1) space

    Floor divide number by 1000, then convert result*1000 to roman
    Subtract the result from the original number, then repeat for 100 etc.
    Append each result to an output string

    
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
                1:  "I",
                4:  "IV",
                5:  "V",
                9:  "IX",
                10: "X",
                40: "XL",
                50: "L",
                90: "XC",
                100: "C",
                400: "CD",
                500: "D",
                900: "CM",
                1000: "M"
            }


        val     = 1000
        checker = 5000

        # The output string
        output = ""

        while val > 0:
            nextN = num // val
            checkVal = nextN*val

            # Just append it straight on if it's
            # one of the keys in dict
            if checkVal in d:
                output += d[checkVal]

            # Otherwise, it's of the form XXX or LXXX etc.
            elif checkVal != 0:
                # Check if it's greater than the "5" value,
                # appending it if so
                if checkVal > checker:
                    output += d[checker]
                    checkVal -= checker

                # Then append the number of roman digits remaining
                output += (checkVal // val) * d[val]

            # Subtract most significant digit from number
            # Have to use nextN*val since we updated checkVal value in elif
            num -= nextN*val 

            # Divide val and checker by 10, ready for next digit
            val //= 10
            checker //= 10

        return output 
