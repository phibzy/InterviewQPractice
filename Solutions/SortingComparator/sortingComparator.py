#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Jun 25, 2020 15:17:22 AEST
  @file        : sortingComparator

"""

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        pass       

    # Normally would have self instead of a,
    # but I just went off the stub on HackerRank. Don't ask me lol
    def comparator(a, b):
        if a.score == b.score:
            if a.name < b.name:
                return -1

            elif b.name < a.name:
                return 1

            else:
                return 0

        if a.score < b.score: return 1

        if b.score < a.score: return -1
