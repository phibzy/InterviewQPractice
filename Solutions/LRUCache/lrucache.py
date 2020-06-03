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


    # Think about this more - stack is probably better?
    # You rushed into this like a madman. Breathe, do tests first, THEN tackle problem
    # Ordered dict is way to go - implement yourself with following:
        # Dict with key/value pairs
        # Dict with Key/Index pairs
        # List of keys representing order

    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.currCapacity = 0
        self.dict = collections.OrderedDict()        

        logging.debug("INIT".center(30, '-'))
        logging.debug(f"maxCapacity is {self.maxCapacity}, currCapacity is {self.currCapacity}")
        logging.debug(f"dict is {self.dict}")
        logging.debug("INIT".center(30, '-'))
        logging.debug("")

    def get(self, key: int) -> int:
        logging.debug("GET BEFORE".center(30, '-'))
        logging.debug(f"key is {key}")
        logging.debug(f"maxCapacity is {self.maxCapacity}, currCapacity is {self.currCapacity}")
        logging.debug(f"dict is {self.dict}")
        logging.debug("")

        if key in self.dict:
            val = self.dict[key]
            del self.dict[key]
            self.dict[key] = val

            return val
        
        return -1

    def put(self, key: int, value: int) -> None:
        logging.debug("PUT BEFORE".center(30, '-'))
        logging.debug(f"maxCapacity is {self.maxCapacity}, currCapacity is {self.currCapacity}")
        logging.debug(f"dict is {self.dict}")
        logging.debug("")


        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value    
        
        else:
            logging.debug("not in dict")
            if self.maxCapacity == self.currCapacity:
                self.dict.pop
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
