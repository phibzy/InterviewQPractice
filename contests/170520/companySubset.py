#!/usr/bin/python3

from typing import List
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")


# Complexity
# Space: O(N) - where N is the number of elements in all sets
# Time: O( S^2 ) - where S is the number of sets (more or less N^2)

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        rList = list()
        
        sList = list()
        # Make list of sets
        for i in range(len(favoriteCompanies)):
            sList.append(set(favoriteCompanies[i]))
        
        j = 0
        while True:
            i = 0
            while i < len(sList):
                # logging.debug(f"i is {i}")
                # logging.debug(f"j js {j}")

                if i == j:
                    if j == len(sList) - 1:
                        rList.append(j)

                    i += 1
                    continue

                # logging.debug(f"sList[j] is {sList[j]}, sList[i] is {sList[i]}")
                if sList[j].issubset(sList[i]):
                    # logging.debug("Is a subset") 
                    break
               
                # Need condition for j == len(sList) - 1
                if i == len(sList) - 1: rList.append(j)
                    
                i += 1
            
            if j == len(sList) - 1: break
                
            j += 1

        return rList
