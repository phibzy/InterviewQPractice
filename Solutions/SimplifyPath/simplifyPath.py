#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Feb 05, 2021 20:41:26 AEDT
  @file        : simplifyPath

"""

import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Default canonical path
        cPath = "/"
        if not path: return cPath
        
        # Use a stack, have a default c-path of "/"
        # Split on multiple consecutive slashes,
        # get rid of any empty elements
        dirs = [ x for x in re.split(r"/+", path) if x != '' ]
        
        # stack keeping track of each dir in path
        s = list()
        
        for d in dirs:
            # If it's a single dot, ignore it
            if d == ".": continue
            
            # .. means we return to previous dir, so we pop
            # top off the dir stack. If no stack just ignore it too
            if d=="..":
                if s: s.pop()
            
            # Otherwise it's a dir, so push onto stack
            else:
                s.append(d)
        
        # If there's no stack just return root symbol
        if not s: return cPath
        
        # Otherwise join the stack up with the separator
        return cPath + "/".join(s)
