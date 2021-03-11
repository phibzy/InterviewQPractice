#!/usr/bin/python3

"""
    Test Cases:
        - Empty hashmap
        - Multiple collisions
        - Removing when value doesn't exist
        - Removal of head of list
        - Getting value that exists/doesn't exist

"""

import unittest
from hashMap import MyHashMap, lNode

class test(unittest.TestCase):

    def testSimple(self):
        testMap = MyHashMap()
        testMap.put(1, 900)
        self.assertEqual(testMap.map[1], lNode((1,900)))
        testMap.put(10001, 900)
        testMap.put(20001, 180)
        self.assertEqual(testMap.map[1], list2Node([(1,900), (10001, 900), (20001, 180)]))
        self.assertEqual(testMap.get(10001), 900)
        self.assertEqual(testMap.get(1), 900)
        self.assertEqual(testMap.get(20001), 180)
        testMap.remove(10001)
        self.assertEqual(testMap.map[1], list2Node([(1,900), (20001, 180)]))
        self.assertEqual(testMap.get(20001), 180)
        self.assertEqual(testMap.get(10001), -1)
        self.assertEqual(testMap.get(10), -1)
        self.assertEqual(testMap.get(1), 900)
        testMap.put(1, 72)
        self.assertEqual(testMap.get(1), 72)
        testMap.remove(1)
        self.assertEqual(testMap.map[1], list2Node([(20001, 180)]))

    # Will construct list of collisions
    # Keep updating existing values, add more, update again and check gets
    # Will even use colliding values
    # It's adding in a duplicate!
    def testBreaking(self):
        testMap = MyHashMap()
        testMap.put(4834, 88459)
        testMap.put(84834, 60779)
        testMap.put(84834, 11102)
        self.assertEqual(testMap.get(84834), 11102)


def list2Node(l):
    if not l: return None

    head = lNode(l[0])
    curr = head

    for n in l[1:]:
        curr.next = lNode(n)
        curr = curr.next

    return head

