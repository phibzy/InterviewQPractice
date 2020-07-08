#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Jul 08, 2020 11:47:35 AEST
  @file        : browserHistory

"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
logging.disable(logging.DEBUG)



"""

Space Complexity: O(N) - where N is number of requests
Time Complexity of operations above each function definition

Faster Back/Foward Operation Solution: Dynamic array, set to max possible size
    Use pointer indexes for how far forward/back you can go, instead of constantly manipulating list
    On each visit simply make the current/next element (depending on implementation) the next page
    Reset forward pointer on each visit

    One disadvantage to this method is if number of page visits is huge, but worst case it will
    still have the same worst case space complexity as my solution. 

"""

class BrowserHistory:

    def __init__(self, homepage):

        logging.debug(f"INIT".center(30, '-'))
        
        # Will use stacks for keeping track of back/forward history
        self.currentPage = homepage
        
        self.backHistory = list()
        self.numBack = 0
        
        self.forwardHistory = list()
        self.numForward = 0


        self.printInfo()

       
    # O(1) - We always add a page to the backHistory and clear the forwardHistory
    def visit(self, url):

        logging.debug(f"VISIT: {url}".center(30, '-'))
        
        # Clear forward history
        self.forwardHistory = list()
        self.numForward = 0
        
        # Append to backHistory
        self.backHistory.append(self.currentPage)
        self.numBack += 1
        
        self.currentPage = url

        self.printInfo()

    # O(K) - Where K is size of backHistory 
    def back(self, steps):
        logging.debug(f"BACK {steps} steps, with numBack {self.numBack}".center(30, '-'))

        if self.numBack == 0: return self.currentPage
        
        if steps > self.numBack:
            steps = self.numBack
            
        self.forwardHistory.append(self.currentPage)
        self.currentPage = self.backHistory[-steps]
        steps -= 1

        logging.debug("End first half of back")
        self.printInfo()
        
        # Append back pages in reverse order to the forward history
        if steps > 0:
            self.forwardHistory += self.backHistory[-steps:][::-1]
        self.numForward += steps + 1
        
        # update backHistory + count
        self.backHistory = self.backHistory[:-(steps+1)]
        self.numBack -= steps + 1

        logging.debug("End of back")
        self.printInfo()
        
        return self.currentPage
        
    # O(K) - Where K is size of forwardHistory
    def forward(self, steps):
        logging.debug(f"FORWARD {steps} steps, with numForward {self.numForward}".center(30, '-'))
        if self.numForward == 0: return self.currentPage
        
        if steps > self.numForward:
            steps = self.numForward
        
        self.backHistory.append(self.currentPage)
        self.currentPage = self.forwardHistory[-steps]
        steps -= 1

        logging.debug("End first half of forward")
        self.printInfo()
        
        # Append forward pages in reverse order to back history
        if steps > 0:
            self.backHistory += self.forwardHistory[-steps:][::-1]
        self.numBack += steps + 1
        
        # update forwardHistory + count
        self.forwardHistory = self.forwardHistory[:-(steps+1)]
        self.numForward -= steps + 1

        logging.debug("End of forward")
        self.printInfo()
        
        return self.currentPage

    def printInfo(self):
        logging.debug(f"currentPage is {self.currentPage}")
        logging.debug(f"forwardHistory: {self.forwardHistory}, with length {self.numForward}")
        logging.debug(f"backHistory: {self.backHistory}, with length {self.numBack}")


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
