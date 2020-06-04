#!/usr/bin/python3

"""
LRU Cache tests

"""

from lrucache import LRUCache
import unittest

class testCache(unittest.TestCase):

    def testCapacity1(self):
        c = LRUCache(1)
        self.assertEqual(c.get(1), -1, "Get on empty cache")
        c.put(1,1)
        self.assertEqual(c.get(1), 1, "Normal get on item")
        c.put(2,2)
        self.assertEqual(c.get(1), -1, "Get after deletion")
        self.assertEqual(c.get(2), 2, "Get after new insertion")
        
    def testCapacity2(self):
        c = LRUCache(2)
        c.put(1,1)
        c.put(2,2)
        self.assertEqual(c.get(1), 1, "Normal get on item")
        self.assertEqual(c.get(2), 2, "Normal get on item")
        c.put(3,3)
        self.assertEqual(c.get(3), 3, "Normal get on item")
        self.assertEqual(c.get(1), -1, "Get after deletion")
        c.put(4,4)
        self.assertEqual(c.get(2), -1, "Get after deletion")
        self.assertEqual(c.get(3), 3, "Normal get on item")
        self.assertEqual(c.get(4), 4, "Normal get on item")
        

    def testLeastRecentlyUsed(self):
        c = LRUCache(3)

        c.put(1,1)
        c.put(2,2)
        c.put(3,3)
        self.assertEqual(c.get(1), 1, "Normal get on item")
        c.put(4,4) 
        self.assertEqual(c.get(4), 4, "Normal get on item")
        self.assertEqual(c.get(2), -1, "Get after deletion, testing least recently used")

    def testReplaceValue(self):
        c = LRUCache(2)

        c.put(2, 1)
        self.assertEqual(c.get(2), 1, "Normal get on item")
        c.put(1, 1)
        self.assertEqual(c.get(1), 1, "Normal get on item")
        c.put(2, 3)
        self.assertEqual(c.get(2), 3, "Existing value not updated")
        c.put(4, 1)
        self.assertEqual(c.get(4), 1, "Normal get on item")
        self.assertEqual(c.get(1), -1, "Get on deleted item")
        self.assertEqual(c.get(2), 3, "Normal get on item")




