"""
LRU Cache Implementation:**
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size `n`, support retrieval of values by key, and the insertion of value pairs. 
When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

An LRU (Least Recently Used) cache is a cache eviction algorithm that discards the least recently used items first when the cache reaches its capacity. 
Here is how an LRU cache typically works:

Initialization: The cache is initialized with a maximum size n.
Insertion: A key-value pair is inserted into the cache. If the key already exists, its value is updated and the key becomes the most recently used.
Retrieval: When a value is retrieved by its key, the key becomes the most recently used.
Eviction: If inserting a new item will exceed the cache's capacity, the least recently used item is removed to make space for the new item.
Before creating test data, let's define the operations we want our LRU Cache to support:

put(key, value): Inserts a key-value pair into the cache. If the key already exists, the value is updated. If the cache is at capacity, the least recently used item is evicted.
get(key): Retrieves the value for a given key from the cache. Returns a special value (like -1) if the key is not found.
Here's some example test data for an LRU cache, including expected outcomes from a series of operations:

Test data for an LRU Cache with a capacity of 2.
test_data = [
    ('put', (1, 1)),   # Cache is {1=1}
    ('put', (2, 2)),   # Cache is {1=1, 2=2}
    ('get', (1), 1),   # Returns 1, Cache order is {2=2, 1=1}
    ('put', (3, 3)),   # LRU key 2 is evicted, Cache is {1=1, 3=3}
    ('get', (2), -1),  # Returns -1 (not found)
    ('put', (4, 4)),   # LRU key 1 is evicted, Cache is {3=3, 4=4}
    ('get', (1), -1),  # Returns -1 (not found)
    ('get', (3), 3),   # Returns 3, Cache order is {4=4, 3=3}
    ('get', (4), 4),   # Returns 4, Cache order is {3=3, 4=4}
    ('put', (4, 5)),   # Updates key 4's value, Cache is {3=3, 4=5}
    ('get', (4), 5),   # Returns 5
]

# The expected cache content and order after each operation would be as follows:
# 1. After 'put', (1, 1): Cache = {1=1}
# 2. After 'put', (2, 2): Cache = {1=1, 2=2}
# 3. After 'get', (1): Cache = {2=2, 1=1}
# 4. After 'put', (3, 3): Cache = {1=1, 3=3}
# 5. After 'get', (2): Cache = {1=1, 3=3} (no change since 2 was not found)
# 6. After 'put', (4, 4): Cache = {3=3, 4=4}
# 7. After 'get', (1): Cache = {3=3, 4=4} (no change since 1 was not found)
# 8. After 'get', (3): Cache = {4=4, 3=3}
# 9. After 'get', (4): Cache = {3=3, 4=4} (no change in order since 4 is already the most recently used)
# 10. After 'put', (4, 5): Cache = {3=3, 4=5} (value for key 4 is updated)
# 11. After 'get', (4): Cache = {3=3, 4=5} (no change in order since 4 is already the most recently used)

In the test data, the put and get actions are specified by tuples, where the first element is the action name and the second element is the action parameter 
(either a key-value pair for put or a key for get). 
For get actions, a third element represents the expected return value.

When testing an LRU cache implementation, you would iterate over test_data, perform the actions, and validate that the return values for get operations match the expected values, 
and that the internal state of the cache reflects the correctorder of items based on their recent use.

"""
import unittest
from collections import OrderedDict

class LRUcache:

    def __init__(self, capacity: int) -> None:
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key=key, last=True)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key=key, last=True)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

class TestLRUcache(unittest.TestCase):
    def test_lru_cache(self):
        cache = LRUcache(2)  # Initialize LRU Cache with capacity 2
        test_data = [
            ('put', (1, 1), None),   # Cache is {1=1}
            ('put', (2, 2), None),   # Cache is {1=1, 2=2}
            ('get', (1,), 1),   # Returns 1, Cache order is {2=2, 1=1}
            ('put', (3, 3), None),   # LRU key 2 is evicted, Cache is {1=1, 3=3}
            ('get', (2,), -1),  # Returns -1 (not found)
            ('put', (4, 4), None),   # LRU key 1 is evicted, Cache is {3=3, 4=4}
            ('get', (1,), -1),  # Returns -1 (not found)
            ('get', (3,), 3),   # Returns 3, Cache order is {4=4, 3=3}
            ('get', (4,), 4),   # Returns 4, Cache order is {3=3, 4=4}
            ('put', (4, 5), None),   # Updates key 4's value, Cache is {3=3, 4=5}
            ('get', (4,), 5),   # Returns 5
        ]

        for index, (operation, args, expected) in enumerate(test_data):
            print(f"Operation: {operation}, Args: {args}, Expected: {expected}")
            if operation == "put":
                cache.put(*args)
            elif operation == "get":
                result = cache.get(*args)
                self.assertEqual(result, expected, f"Failed at test case # {index}. Returned Result = {result} for TestCase ({args[0]}) whereas expected was {expected}")

if __name__ == "__main__":
    # Test data for an LRU Cache with a capacity of 2.
    test_data = [
        ('put', (1, 1)),   # Cache is {1=1}
        ('put', (2, 2)),   # Cache is {1=1, 2=2}
        ('get', (1,), 1),   # Returns 1, Cache order is {2=2, 1=1}
        ('put', (3, 3)),   # LRU key 2 is evicted, Cache is {1=1, 3=3}
        ('get', (2,), -1),  # Returns -1 (not found)
        ('put', (4, 4)),   # LRU key 1 is evicted, Cache is {3=3, 4=4}
        ('get', (1,), -1),  # Returns -1 (not found)
        ('get', (3,), 3),   # Returns 3, Cache order is {4=4, 3=3}
        ('get', (4,), 4),   # Returns 4, Cache order is {3=3, 4=4}
        ('put', (4, 5)),   # Updates key 4's value, Cache is {3=3, 4=5}
        ('get', (4,), 5),   # Returns 5
    ]

    # The expected cache content and order after each operation would be as follows:
    # 1. After 'put', (1, 1): Cache = {1=1}
    # 2. After 'put', (2, 2): Cache = {1=1, 2=2}
    # 3. After 'get', (1): Cache = {2=2, 1=1}
    # 4. After 'put', (3, 3): Cache = {1=1, 3=3}
    # 5. After 'get', (2): Cache = {1=1, 3=3} (no change since 2 was not found)
    # 6. After 'put', (4, 4): Cache = {3=3, 4=4}
    # 7. After 'get', (1): Cache = {3=3, 4=4} (no change since 1 was not found)
    # 8. After 'get', (3): Cache = {4=4, 3=3}
    # 9. After 'get', (4): Cache = {3=3, 4=4} (no change in order since 4 is already the most recently used)
    # 10. After 'put', (4, 5): Cache = {3=3, 4=5} (value for key 4 is updated)
    # 11. After 'get', (4): Cache = {3=3, 4=5} (no change in order since 4 is already the most recently used)
    unittest.main()