#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Jul 08, 2020 11:47:35 AEST
  @file        : browserHistory

"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
logging.disable(logging.DEBUG)

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
