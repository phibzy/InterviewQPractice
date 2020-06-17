#!/usr/bin/python3

"""
Given list of words from a Magazine and criminal's Note
Check if note can be written by cutting and pasting words from magazine

Note that case sensitivity is important, as is quantity of words
I.e. can't repeat word in note if it only appears once in magazine


"""


# Time Complexity: O(m + n) - worst case have to go through all words in both mag and note
# Space Complexity: O(m) - We create hash of size m, the words in magazine

# Algo: Go through magazine words, create hash of words. If word appears more than once increment its value
#       Then go through words in note, if word is in hash decrement it (delete if 0). Print "No" if there's
#       Ever a point where word is not in hash


# Improvement: if len(note) > len(magazine), it's impossible for the note to be replicated

def checkMagazine(magazine, note):
    if len(note) > len(magazine):
        print("No")
        return

    words = dict()

    for i in magazine:
        if i in words: words[i] += 1
        else: words[i] = 1

    for i in note:
        if i not in words:
            print("No")
            return

        words[i] -= 1
        if words[i] == 0:
            del words[i]

    print("Yes")
