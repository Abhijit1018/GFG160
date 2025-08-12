# Python program to implement LRU Least Recently Used) using
# Built-in Doubly linked list
from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # Dictionary to store key-value pairs
        self.cache = {}

        # Deque to maintain the order of keys
        self.order = deque()

    def get(self, key: int) -> int:
        if key in self.cache:

            # Move the accessed key to 
            # the front of the deque
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.cache:

            # Update the value and move
            # the key to the front
            self.cache[key] = value
            self.order.remove(key)
            self.order.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:

                # Remove the least recently used item
                lru_key = self.order.pop()
                del self.cache[lru_key]

            # Add the new key-value pair
            self.cache[key] = value
            self.order.appendleft(key)


if __name__ == "__main__":
  
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
