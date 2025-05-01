'''
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:

Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)
'''
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cachedict = {} # Map the value to Nodes
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)

        # left = LRU and right = MRU
        self.left.next, self.right.prev = self.right, self.left
        
    # Remove from list        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert at rightmost position
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        

    def get(self, key: int) -> int:        
        if key in self.cachedict.keys():
            # self.mru += 1
            # self.cachedict[key][1] = self.mru
            self.remove(self.cachedict[key]) # Remove from List
            self.insert(self.cachedict[key]) # Add at MRU ie rightmost position
            return self.cachedict[key].value
        return -1            
        

    def put(self, key: int, value: int) -> None:
        # if len(self.cachedict) <= self.capacity:
        #     self.cachedict[key][0] = value
        #     self.cachedict[key][1] = 1
        if key in self.cachedict.keys():
            self.remove(self.cachedict[key])
            self.cachedict[key] = Node(key=key, value=value)
            self.insert(self.cachedict[key])
        
        if len(self.cachedict) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cachedict[key]

