#!/usr/bin/python3

"""
Data structure for an LRU cache

My implementation uses a dict for accessing keys
Also uses queue for keeping track of most/least recently used keys

"""

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
logging.disable(logging.DEBUG)


class dllNode:

    def __init__(self, val = None):
        self.next = None
        self.prev = None
        self.val = val


class dLinkedList:

    def __init__(self):
        self.start = None
        self.end   = None
        self.length = 0

    def append(self, node):
        logging.debug(f"Order before append: {self.printList()}")
        logging.debug(f"Reverse order before append: {self.printListReverse()}")
        if self.length == 0:
            logging.debug("Length is 0")
            self.start = node
            node.prev = None
            node.next = None
            self.end = node

        else:

            logging.debug(f"end is {self.end} with value {self.end.val}")
            self.end.next = node
            logging.debug(f"self.end is {self.end.val}, self.end.next is {self.end.next.val}, node is {node.val}")
            node.prev = self.end
            logging.debug(f"self.end is {self.end.val}, self.end.next is {self.end.next.val}, node is {node.val}, node.prev is {node.prev.val}")
            self.end = node
            logging.debug(f"self.end is {self.end.val}, self.end.next is {self.end.next}, node is {node.val}, node.prev is {node.prev.val}, self.end.prev is {self.end.prev.val}")

        self.length += 1

    def pop(self):
        if self.length == 0: return
        node = self.start

        if self.end == node: self.end = node.prev
        self.start = self.start.next
        
        node.prev = None
        node.next = None

        if self.start: self.start.prev = None
        self.length -= 1

        return node
   
    # Remove a given node from the list - O(1) time operation
    # Takes in reference to node, so if it's not in the list then no worries
    def remove(self, node):
        if self.start == node: self.start = node.next
        if self.end == node: self.end = node.prev
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next

        node.next = None
        node.prev = None
        self.length -= 1

        return node

    # Debug print function
    def printList(self):
        curr = self.start
        rStr = "--- "
        while curr:
            # logging.debug(f"curr is {curr}, next is {curr.next}")
            rStr += f"{curr.val} --- "
            curr = curr.next

        return rStr

    def printListReverse(self):
        curr = self.end
        rStr = "--- "
        while curr:
            # logging.debug(f"curr is {curr}, next is {curr.next}")
            rStr += f"{curr.val} --- "
            curr = curr.prev

        return rStr

class LRUCache:


    # Think about this more - stack is probably better?
    # You rushed into this like a madman. Breathe, do tests first, THEN tackle problem
    # Ordered dict is way to go - implement yourself with following:
        # Dict with key/value pairs
        # Dict with Key/Index pairs
        # List of keys representing order

    def __init__(self, capacity):
       self.maxCapacity = capacity 
       self.currCapacity = 0

       # Dict/hash for key/value pairs
       self.values = dict()

       # List ordered with LRU at front, MRU at back
       self.order = dLinkedList()

       # Dict/hash for key/node pairs, allows constant access of list
       # TODO: Note, can store key and values in nodes and thus remove need for self.values
       self.nodes = dict()


    def get(self, key):
        logging.debug('')
        logging.debug(f"GET CALL on key: {key}".center(30,'-')) 
        logging.debug(f"dict: {self.values} before get")
        logging.debug(f"Order before update: {self.order.printList()}")
        logging.debug(f"Reverse order before update: {self.order.printListReverse()}")

        if key in self.values:
            logging.debug("Key is in the dict")
            node = self.order.remove(self.nodes[key])
            self.order.append(node)
            return self.values[key]

        logging.debug("Key NOT in the dict")
        return -1

    def put(self, key, value):
        logging.debug('')
        logging.debug(f"PUT CALL on key: {key} and value: {value}".center(30,'-')) 
        logging.debug(f"values dict before put: {self.values}")
        logging.debug(f"Order before update: {self.order.printList()}")
        logging.debug(f"Reverse order before update: {self.order.printListReverse()}")

        if key in self.values:
            logging.debug("Key is in the dict")

            node = self.order.remove(self.nodes[key])
            self.order.append(node)
            self.values[key] = value

        else:

            if self.currCapacity == self.maxCapacity:
                
                node = self.order.pop()

                # Note that "val" of nodes is actually the key in the LRU Cache
                k = node.val
                del self.nodes[k]
                del self.values[k]

                self.currCapacity -= 1

            self.values[key] = value
            node = dllNode(key)
            self.nodes[key] = node
            self.order.append(node)
            self.currCapacity += 1



        logging.debug(f"values dict after put: {self.values}")
        logging.debug(f"Order after update: {self.order.printList()}")
        logging.debug(f"Reverse order after update: {self.order.printListReverse()}")


# c = LRUCache(3)
# c.put(1,1)
# c.put(2,2)
# c.put(3,3)
# print(c.get(1))
# c.put(4,4) 
# print(c.get(4))
# print(c.get(2))
