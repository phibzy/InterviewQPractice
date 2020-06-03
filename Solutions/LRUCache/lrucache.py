#!/usr/bin/python3

"""
Data structure for an LRU cache

My implementation uses a dict for accessing keys
Also uses queue for keeping track of most/least recently used keys

"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
# logging.disable(logging.DEBUG)

class LRUCache:

    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.currCapacity = 0
        self.lruQ = list()
        self.dict = dict()        

        logging.debug("INIT".center(30, '-'))
        logging.debug(f"maxCapacity is {self.maxCapacity}, currCapacity is {self.currCapacity}")
        logging.debug(f"lruQ is {self.lruQ}")
        logging.debug(f"dict is {self.dict}")
        logging.debug("INIT".center(30, '-'))
        logging.debug("")

    def get(self, key: int) -> int:
        logging.debug("GET BEFORE".center(30, '-'))
        logging.debug(f"key is {key}")
        logging.debug(f"maxCapacity is {self.maxCapacity}, currCapacity is {self.currCapacity}")
        logging.debug(f"lruQ is {self.lruQ}")
        logging.debug(f"dict is {self.dict}")
        logging.debug("")

        if key in self.dict:
            self.lruQ.append(self.lruQ.pop(self.lruQ.index(key)))
            return self.dict[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        logging.debug("PUT BEFORE".center(30, '-'))
        logging.debug(f"maxCapacity is {self.maxCapacity}, currCapacity is {self.currCapacity}")
        logging.debug(f"lruQ is {self.lruQ}")
        logging.debug(f"dict is {self.dict}")
        logging.debug("")


        if key in self.dict:
            logging.debug("is in the dict")
            self.dict[key] = value    
            self.lruQ.append(self.lruQ.pop(self.lruQ.index(key)))
        
        else:
            logging.debug("not in dict")
            if self.maxCapacity == self.currCapacity:
                oldKey = self.lruQ.pop(0)
                del self.dict[oldKey]
                self.currCapacity -= 1
            
            self.lruQ.append(key)
            self.dict[key] = value
            self.currCapacity += 1

        logging.debug(f"maxCapacity is {self.maxCapacity}, currCapacity is {self.currCapacity}")
        logging.debug(f"lruQ is {self.lruQ}")
        logging.debug(f"dict is {self.dict}")

cache = LRUCache( 2 );

print(cache.put(2, 1))
print(cache.put(1, 1))
print(cache.put(2, 3))
print(cache.put(4, 1))
print(cache.get(1))
print(cache.get(2))
