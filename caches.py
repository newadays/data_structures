# LRU Cache
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
# The LRUCache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.
#
# Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least recently used” item is the one with the oldest access time.

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.ls = {}
        self.stack = []
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key in self.ls:
            value = self.ls[key]
            self.stack.remove(key)
            self.stack.append(key)
            return value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

        if key not in self.ls:
            if len(self.ls.keys()) >= self.capacity:
                if self.stack:
                    removal_key = self.stack[0]
                    self.ls.pop(removal_key)
                    self.ls[key] = value
                    self.stack.remove(removal_key)
                    self.stack.append(key)

            else:
                self.ls[key] = value
                self.stack.append(key)
                # // key exist in stack at least position  you need to change its position to first position
        else:
            self.stack.remove(key)
            self.stack.append(key)
            self.ls[key] = value