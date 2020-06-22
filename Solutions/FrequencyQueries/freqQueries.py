#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Jun 22, 2020 09:23:28 AEST
  @file        : freqQueries

"""

class freq:
    def __init__(self):
        # Have a value hash and a frequency hash
        # Val hash just stores whether value is in structure or not
        # Freq hash stores how many of each frequency
        self.valHash = dict()
        self.freqHash = dict()

    def insert(self, x):
        if x in self.valHash:
            if self.valHash[x] in self.freqHash:
                self.freqHash[self.valHash[x]] -= 1

                if self.freqHash[self.valHash[x]] == 0:
                    del self.freqHash[self.valHash[x]]

        self.valHash.setdefault(x, 0)
        self.valHash[x] += 1

        self.freqHash.setdefault(self.valHash[x], 0)
        self.freqHash[self.valHash[x]] += 1

    def remove(self, y):
        if y in self.valHash:
            self.freqHash[self.valHash[y]] -= 1
            if self.freqHash[self.valHash[y]] == 0:
                del self.freqHash[self.valHash[y]]

            self.valHash[y] -= 1
            if self.valHash[y] == 0:
                del self.valHash[y]

    def isPresent(self, z):
        return (z in self.freqHash)


# Complete the freqQuery function below.
def freqQuery(queries):
    s = freq()
    output = list()

    for op, val in queries:
        if op == 1:
            s.insert(val)
        
        elif op == 2:
            s.remove(val)

        elif op == 3:
            if s.isPresent(val):
                output.append(1)
            else:
                output.append(0)

    return output

