#!/usr/bin/python3

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")

# logging.disable(logging.DEBUG)

class Solution:
    def reverseBits(self, n):
        # a = list(bin(n)[2:].zfill(32))
        # end = 31
        
        # for i in range(16):
            # # logging.debug(f"i is {i}, end is {end}")
            # # logging.debug(f" a is {a}, of length {len(a)}")
            # temp = a[i]
            # a[i] = a[end]
            # a[end] = temp
            # end-= 1
        
        # return int(''.join(a), 2)
        logging.debug(f"bin n is {bin(n)}")

        for i in range(32):
            n = (((n << 1) & ((2 ** 32) - 1)) | (n >> 31))
            logging.debug(f"n is {n}")
            logging.debug(f"i is {i}")
            logging.debug(f"bin n is {bin(n)}")
            logging.debug(f"Real length is {len(bin(n)) - 2}")
            logging.debug("".center(25, '-'))
        
        return n


a = Solution()
print(a.reverseBits(43261596))
