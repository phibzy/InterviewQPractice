#!/usr/bin/python3

class Solution:

    def arrangeWords(self, text: str) -> str:
        # split words into list
        wordList = text.split()
        
        lenList = list()
        for word in wordList:
            lenList.append((word.lower(), len(word)))

        lenList.sort(key=lambda word: word[1])
        
        rText = ''
        for i in range(len(lenList)):
            if i == 0:
                rText += lenList[i][0].title()
            else:
                rText += ' ' + lenList[i][0]
                
        return rText
