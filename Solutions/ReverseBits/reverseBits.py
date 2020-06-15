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

        for _ in range(8):
            n = ((n << 1) & 8589934591) | (n >> 31)
            logging.debug(f"bin n is {bin(n)}")
        
        return n



a = Solution()
print(a.reverseBits(43261596))
