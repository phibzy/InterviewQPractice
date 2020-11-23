#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Nov 23, 2020 14:01:43 AEDT
  @file        : uniqueWords

"""

# TC: O(S) - Where S is the sum of all the characters in all the strings
# SC: O(N) - Worst case all encoded words are unique and we have a set
#            with length equal to the number of input strings

class Solution:
    def uniqueMorseRepresentations(self, words):
        # Put all more code into a list for easy encoding
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."] 
        
        # Use dict or set to keep track of unique entries
        unique = set()

        # We go through each word in list and encode it
        # Then we add the encoded word in to the set
        # If an encoded word is already in there then the
        # set length won't change.
        for word in words:
            encodedWord = ""
            
            for char in word:
                # By using ascii values and subtracting the ascii
                # value of 'a', we end up with a range of 0-25 for alphabet
                # which matches up perfectly as an index for our code list
                encodedWord += code[(ord(char) - ord('a'))]

            unique.add(encodedWord)

        # Since a set can only contain unique elements,
        # the length of the set of encoded words is how many
        # unique encodings there are
        return len(unique)

