#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Mar 25, 2021 11:34:23 AEDT
  @file        : encode

"""

"""
Qs:
    - Max length of either string? Does TinyUrl have to be certain length?
    - Character restrictions for tinyurl?
    - Max number of URL input?
    - Min?
    - URL guaranteed to be valid?
    - How to handle same URL being encoded again?
    - Will it always be https? Need to handle stuff like ftp?

"""

"""
Use a hash to keep track of tinyUrl -> longUrl mappings

"""

import re, random

class Codec:

    longUrls = dict()
    POSSIBLE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    NUM_CHARS = 62
    TINY_URL_BASE = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.

        For funsies lets just say that tinyurl has max 6 chars
        after '/'

        Encoding Algo:
            - Ignore initial "https" crap
            - Remove forward slashes
            - Find ord value of first len/6 chars of string
            - Resulting ord value mod number of valid chars is the index
              of string we'll use to find the char we use for encoded char
            - Have some condition for less than 6 chars

        """

        # Remove https:// and '/' characters
        modString = re.findall(r"^.*://(.*)$", longUrl)
        modString = re.sub(r"/", "", modString[0]) 

        # For string with len not divisible by 6, add all remaining chars for last encoded char
        i = 0
        endPoint = interval = len(modString) // 5 if len(modString) // 5 >= 1 else 1
        enString = ""
        nextCharVal = 0
        while i < len(modString):
            # If it's in next group, add to encode value
            if i < endPoint:
                nextCharVal += ord(modString[i])

            # Otherwise encode the string, change endpoint for next interval,
            # append the encoded char and then reset the charVal for next group
            else:
                enString += self.POSSIBLE_CHARS[nextCharVal % self.NUM_CHARS]
                endPoint += interval
                nextCharVal = 0
             
            i += 1

        # Bundle in the remainder chars (if any)
        if nextCharVal > 0:
            enString += self.POSSIBLE_CHARS[nextCharVal % self.NUM_CHARS]

        # If we have less than 6 chars, keep adding random numbers lol
        while len(enString) < 6:
            randIndex = random.randint(0, self.NUM_CHARS - 1)
            enString += self.POSSIBLE_CHARS[randIndex]

        # Remember to check if URL already exists
        while enString in self.longUrls:

            # Just increment the last char lol
            newChar = (ord(enString[5]) + 1) % self.NUM_CHARS
            enString = enString[:5] + self.POSSIBLE_CHARS[newChar]

        # Put longUrl in the dict, with encoded string as key
        self.longUrls[enString] = longUrl

        return self.TINY_URL_BASE + enString

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
           

           Only thing to maybe add here would be stripping https://tinyurl... part

        """
        modString = re.findall(r"^http://tinyurl.com/(.*)$", shortUrl)
        return self.longUrls[modString[0]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

