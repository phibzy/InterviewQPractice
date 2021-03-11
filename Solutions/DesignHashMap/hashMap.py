#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Mar 11, 2021 09:52:02 AEDT
  @file        : hashMap

"""

"""
Qs:
    - Any space restrictions on underlying structure?
    - Range of keys/values?
    - How many requests will I have to deal with?
    - How to handle invalid requests? E.g. getting key which doesn't exist

    Chaining is the name of the other strat btw

"""


class lNode:
    def __init__(self, v, n=None):
        self.val = v
        self.next = None

    def __eq__(self, n):
        if not self and not n: return True

        if not self or not n: return False

        return (self.val == n.val) and \
            (self.next == n.next)

    def printMe(self):
        print("-->", end=" ")
        
        curr = self

        while curr:
            print(f" {curr.val} -->", end=" ")
            curr = curr.next

        print()


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        
        We'll have at must 10000 put requests, so will create underlying
        list of length 10000.

        Set them to since we'll be using chaining on each element

        """
        self.MAPSIZE = 10000
        self.map = [ None for _ in range(self.MAPSIZE) ]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.

        Will use int value modded by map size to store values.

        Values will be stored as key/value pairs, with chaining to resolve collisions

        Cases:
            - Rewriting key already in hash
            - Key doesn't exist
            - Collision

        """

        index = self.hash(key)

        # If there's no other values here, just chuck it in!
        if not self.map[index]:
            self.map[index] = lNode((key, value))

        # Otherwise, we either need to rewrite 
        # existing node or chuck on end of list - i.e. we have collision
        else:
            # Check head first since we'll need curr.next
            curr = self.map[index]

            # rewrite value if it exists
            if curr.val[0] == key:
                curr.val = (key, value)

            # Otherwise chuck on end of list
            else:
                while curr.next:

                    # Forgot condition here...
                    if curr.next.val[0] == key:
                        curr.next.val = (key, value)
                        return

                    curr = curr.next

                curr.next = lNode((key,value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.hash(key)
        curr = self.map[index]

        # Search through list
        while curr:
            # If the value in list matches key, return value
            if curr.val[0] == key: return curr.val[1]
            curr = curr.next

        # If it doesn't exist, return -1
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        
        Extra case for head of the list, otherwise we gucci and can repeat similar to before

        Have to check next pointer instead though since we need to manipulate pointers

        """
        
        index = self.hash(key)

        # If list doesn't exist just return
        if not self.map[index]: return

        # If it's the head of list, manipulate pointers
        if self.map[index].val[0] == key:
            self.map[index] = self.map[index].next
            return

        curr = self.map[index]

        # Search through list
        while curr.next:
            # If the value in list matches key, manipulate list
            if curr.next.val[0] == key: 
                curr.next = curr.next.next
                return

            curr = curr.next

        # Otherwise if it's not in list do nothing

    # Our simple hash function
    def hash(self, key):
        return key % self.MAPSIZE
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
