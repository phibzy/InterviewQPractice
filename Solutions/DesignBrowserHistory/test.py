#!/usr/bin/python3

"""
   Test Cases:



"""

import unittest
from browserHistory import BrowserHistory

class testBHistory(unittest.TestCase):

    def testDefault(self):
        browserHistory = BrowserHistory("leetcode.com")
        self.assertEqual(browserHistory.visit("google.com")       , None, "Fails basic case")
        self.assertEqual(browserHistory.visit("facebook.com")     , None, "Fails basic case")
        self.assertEqual(browserHistory.visit("youtube.com")      , None, "Fails basic case")
        self.assertEqual(browserHistory.back(1)                   , "facebook.com", "Fails basic case")
        self.assertEqual(browserHistory.back(1)                   , "google.com", "Fails basic case")
        self.assertEqual(browserHistory.forward(1)                , "facebook.com", "Fails basic case")
        self.assertEqual(browserHistory.visit("linkedin.com")     , None, "Fails basic case")
        self.assertEqual(browserHistory.forward(2)                , "linkedin.com", "Fails basic case")
        self.assertEqual(browserHistory.back(2)                   , "google.com", "Fails basic case")
        self.assertEqual(browserHistory.back(7)                   , "leetcode.com", "Fails basic case")

    

